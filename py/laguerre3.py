def restrictions_laguerre(G, umin, umax, dumin, dumax, ymin, ymax, x, u, L, N):
    # ΔU
    M1 = np.vstack((-L[0:N].T[0], L[0:N].T[0]))
    N1 = np.vstack((-dumin * np.ones((N, 1)), dumax * np.ones((N, 1))))
    # U
    a = [np.sum((L[i].T for i in range(n)), axis=0) for n in range(1, N + 1)]
    M2 = np.vstack((-np.vstack(a), np.vstack(a)))
    N2 = np.vstack((-umin * np.ones((N, 1)) + u, umax * np.ones((N, 1)) - u))
    # Y
    A, B, C, D = G
    M3 = np.vstack((-C @ B @ L[0].T, C @ B @ L[0].T))
    N3 = np.vstack((-ymin + C @ A @ x, ymax - C @ A @ x))
    #
    M = np.vstack((M1, M2, M3))
    N = np.vstack((N1, N2, N3))
    return M, N