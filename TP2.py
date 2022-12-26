# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 09:01:59 2022

@author: User
"""

import numpy as np

A=np.array([[6,6,16],[-3,-9,-2],[6,-6,-8]],float)
def DecompositionGS (A):
	n,m=A.shape

	Q,R=np.zeros((n,m)),np.zeros((n,m))

	R[0,0]=np.linalg.norm(A[:,0])
	Q[:,0]=A[:,0]/R[0,0]

	for i in range(1,n):
		for j in range(i):
			R[j,i]=np.dot(A[:,i],Q[:,j])

		somme =0
		for t in range(i):
			somme += R[t,i]*Q[:,t]
		W=A[:,i]- somme

		R[i,i]=np.linalg.norm(W)

		Q[:,i] = W/R[i,i]

	return Q,R,np.dot(Q,R)

def ResolTriSup(T,b):
    """ Resolution d'un systeme Tx=b
    avec T triangulaire superieure et b un vecteur.
    La solution x est rendue de meme format que b """
    
    frm=b.shape
    n,m=T.shape
    x=np.zeros(n)
    for i in range(n-1,-1,-1):
        S=T[i,i+1:]@x[i+1:]
        x[i]=(b[i]-S)/T[i,i]
    return x.reshape(frm)


def ResolGS(A,b):
	Q,R,P=DecompositionGS(A)
	Y = np.dot(Q.T,b)
	X=ResolTriSup(R,Y)
	return X




def DecompositionLU(A):
    """ Calcul de la decomposition LU d'une matrice carree A"""
    U=np.array(A,float)
    n,m=U.shape
    if n !=m:
        raise Exception('Pas une matrice carree')
    L=np.eye(n)
    for i in range(n-1):
        if U[i,i]==0:
            raise Exception('Un pivot est nul')
        for j in range(i+1,n):
            g=U[j,i]/U[i,i]
            L[j,i]=g
            U[j,:]=U[j,:]-g*U[i,:]
    return (L,U)
