from sympy import *
from sympy import Integral, pprint
import numpy as np
A = Matrix([2, 12, -3, 1, -6, -3, 2, 0, 18]).reshape(3, 3)
def G(n,i,j,c,s):
    M = eye(n)
    M[i,i] = M[j,j] = c
    M[i,j] = -s
    M[j,i] = s
    return M
def qr_givens(A):
    n = A.shape[0]
    R = Matrix(A[:,:])
    Q = eye(n)

    for j in range (n-1):
        for i in range(n-1,j,-1):

            l1 = i
            l2 = i-1
            r = sqrt(R[l1,j]**2+R[l2,j]**2)
            g = G(n,l1,l2, R[l2,j]/r,R[l1,j]/r) 
            R = g*R
            Q = g.T
    pprint (Q)
    pprint(R)
    return (Q, R)
qr_givens(A)