import numpy as np
from sympy import *
A = Matrix([2, 12, -3, 1, -6, -3, 2, 0, 18]).reshape(3, 3)

def G(n,i,j,c,s):
    M= np.eye(n)
    M[i,i] = M[j,j] = c
    M[i,j],M[j,i] = -s, s
    return M
n,m = shape(A)
Q = np.eye(n)
r = sqrt(A[0,0]**2+A[2,0]**2)
g = G(3,2,0,A[0,0]/r,A[2,0]/r)
R = g*A
Q = Q*g.T
print(R)
print(Q)
