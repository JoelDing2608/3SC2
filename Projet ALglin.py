import numpy as np
import scipy as sc
test_matx = np.array([[2,12,-3],[1,-6,-3],[2,0,18]])

def deco_qr(A):
    n = A.shape[0]
    Q = np.eye(n)
    
    for j in range (n-1):
        for i in range(n-1,j,-1):
            lign1 = i
            lign2 = i-1
            r = np.sqrt(A[lign1,j]**2+A[lign2,j]**2)
            g = G(n,lign1,lign2,A[lign2,j]/r,A[lign1,j]/r)
            A = g*A
            Q = Q*np.transpose(g)

    m = n-1
    if A[m,m] < 0:
        A[m,m] = -A[m,m]
        Q[:,2] = -Q[:,2]
    print(Q)
    print(A)
    print(Q*A)

    return (Q, A)
def G(n,i,j,c,s):
    M = np.eye(n)
    M[i,i] = M[j,j] = c
    M[i,j],M[j,i] = -s, s
    return M
deco_qr(test_matx)