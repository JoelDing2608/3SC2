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
    
    # détermination de la taille de A 
    n, m = A.shape

    R = Matrix(A[:,:])
    Q = eye(n)

    # boucle pour les colonnes de R augmentée
    for j in range (m-1):

        #boucle pour les lignes de R augmentée
        for i in range(j+1,n):

            l1 = i
            l2 = i-1
            r = sqrt(R[l1,j]**2+R[l2,j]**2)
            g = G(n,l1,l2, R[l2,j]/r,R[l1,j]/r) 

            #mise  à  jour de R
            R = g*R

            #mise  à  jour de Q
            Q = g.T
            #pprint(R)
    return (Q, R)


def ResolGivens(A,b):

    # décomposition QR de A
    Q,R = qr_givens(A)

    #calcul de y
    y = Q.T*b

    #résolution de Rx = y
    #pprint(rt)
    f = linsolve((R,y))
    pprint(f)
    return f


def ResolGivens2(A,b):

    #création de la matrice augmentée
    A_aug = Matrix.hstack(A,b)
    #pprint(A_aug)

    # détermination de la taille de A augmentée
    n, m = A_aug.shape
    R_aug = Matrix(A_aug[:,:])

    # boucle pour les colonnes de R augmentée
    for j in range (m-1):

        #boucle pour les lignes de R augmentée
        for i in range(j+1,n):

            l1 = i
            l2 = i-1
            
            r = sqrt(R_aug[l1,j]**2+R_aug[l2,j]**2)

            #calcul des coefficents et de la matrice G
            g = G(n,l1,l2, R_aug[l2,j]/r,R_aug[l1,j]/r) 

            #mise  à  jour de R augmentée
            R_aug = g*R_aug

    #extraction de b  dans R augmentée
    b_aug = R_aug[:,-1]
    #pprint(R_aug)

    #résolution de Rx = b
    x = linsolve((R_aug[:,:-1],b_aug))
    pprint(x)
    return (x)

ResolGivens2(A,t)
ResolGivens(A,t)

