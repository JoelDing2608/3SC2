import numpy as np
test_matx = np.array([[1,2,3],[0,1,4],[5,6,0]])
def givens_qr(A):
   m, n = A.shape
   Q = np.eye(m)
   R = A.copy()
   for j in range(n):
    for i in range(m-1, j, -1):
            G = np.eye(m)
            r = np.hypot(R[i-1, j], R[i, j])
            c = R[i-1, j]/r
            s = R[i, j]/r
            G[i-1:i+1, i-1:i+1] = [[c, s], [-s, c]]
            R[:, [i-1, i]] = np.dot(G, R[:, [i-1, i]])
            Q[:, [i-1, i]] = np.dot(Q[:, [i-1, i]], G.T)
    return Q, R

print(givens_qr(test_matx))
