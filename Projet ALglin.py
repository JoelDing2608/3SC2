from sympy import *
import numpy as np


A = Matrix([2, 12, -3, 1, -6, -3, 2, 0, 18]).reshape(3, 3)
B = Matrix([2, 12, 1, -3, 2, 8]).reshape(3, 2)
t = Matrix([2,5,12]).reshape(3,1)


def G(n,i,j,c,s):
    M = eye(n)
    M[i,i] = M[j,j] = c
    M[i,j] = -s
    M[j,i] = s
    return M


def qr_givens(A):
    n, m = A.shape
    R = Matrix(A[:,:])
    Q = eye(n)

    for j in range (m-1):
        for i in range(j+1,n):

            l1 = i
            l2 = i-1
            r = sqrt(R[l1,j]**2+R[l2,j]**2)
            g = G(n,l1,l2, R[l2,j]/r,R[l1,j]/r) 
            R = g*R
            Q = g.T
            #pprint(R)
    #pprint (Q)
    #pprint(R)
    return (Q, R)


def ResolGivens(A,b):
    Q,R = qr_givens(A)
    y = Q.T*b
    rt = R.inv()
    #pprint(rt)
    f = linsolve((R,y))
    pprint(f)
    return f

def ResolGivens2(A,b):
    A_aug = Matrix.hstack(A,b)
    #pprint(A_aug)
    n, m = A_aug.shape
    R_aug = Matrix(A_aug[:,:])
    for j in range (m-1):
        for i in range(j+1,n):

            l1 = i
            l2 = i-1
            r = sqrt(R_aug[l1,j]**2+R_aug[l2,j]**2)
            g = G(n,l1,l2, R_aug[l2,j]/r,R_aug[l1,j]/r) 
            R_aug = g*R_aug
            
    b_aug = R_aug[:,-1]
    #pprint(R_aug)
    x = linsolve((R_aug[:,:-1],b_aug))
    pprint(x)
    return (x)

ResolGivens2(A,t)
ResolGivens(A,t)

