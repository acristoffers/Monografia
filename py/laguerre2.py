def laguerre_phi(m, A, B, L):
    mp = np.linalg.matrix_power
    return np.sum((mp(A, m - i - 1) @ B @ L[i].T for i in range(m))).T


def omega_psi(Q, RL, A, B, L, Np):
    mp = np.linalg.matrix_power
    phis = [0] + [laguerre_phi(m, A, B, L) for m in range(1, Np + 1)]
    omega = np.sum((phis[m] @ Q @ phis[m].T for m in range(1, Np + 1))) + RL
    psi = np.sum((phis[m] @ Q @ mp(A, m) for m in range(1, Np + 1)))
    return omega, psi