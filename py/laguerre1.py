def lagd(a, N):
    ''' Retorna as matrizes A1 e L0 usadas no cálculo dos coeficientes '''
    toeplitz = sp.linalg.toeplitz
    beta = 1 - a * a
    A1 = np.tril(toeplitz([a] + [(-1)**i * a**i * beta for i in range(N - 1)]))
    L0 = np.sqrt(beta) * np.array([(-1)**i * a**i for i in range(N)])
    return A1, L0.reshape(N, 1)

def lagfit(sys, a, N, N_sim):
    '''
    Retorna os coeficientes e matriz L para esta simulação

    sys = sistema (ver help(sp.signal.dimpulse))
    a = peso ajustável
    N = número de variáveis para descrever o sistema
    N_sim = número de pontos na simulação
    '''
    ts, (ys, ) = sp.signal.dimpulse(sys, n=N_sim)
    A1, L0 = lagd(a, N)
    L = np.zeros((N_sim, N, 1))
    L[0, :] = L0
    for k in range(1, N_sim):
    L[k, :] = A1 @ L[k - 1, :]
        cs = [L[:, i].reshape(1, N_sim) @ ys for i in range(N)]
    return cs, L
