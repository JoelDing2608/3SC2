import numpy as np
test_matx = np.array([[2,12,-3],[1,-6,-3],[2,0,18]])
def qr_givens(A):
    """
    Décompose la matrice A en QR avec la méthode de Givens.
    Retourne les matrices Q et R.
    """
    n, m = A.shape
    Q = np.eye(n)
    for j in range(m):
        for i in range(n-1, j, -1):
            G = np.eye(n)
            r = np.hypot(A[i-1, j], A[i, j])
            c = A[i-1, j] / r
            s = A[i, j] / r
            G[[i-1, i], [i-1, i]] = [c, s]
            G[[i, i-1], [i-1, i]] = [-s, c]
            A = G @ A
            Q = Q @ G.T
    R = A
    print(Q)
    print(R)
    print(Q@R)
    return Q, R
    
qr_givens(test_matx)