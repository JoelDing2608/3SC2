# -*- coding: utf-8 -*-
# python version 3.4 
 
import scipy as sc
import numpy as np 
from random import randint 
"""factorisation QR méthode de Givens""" 
###implémentation itérative 
 
def c(p,q,A): 
    """cosinus theta""" 
    if A[p,p]==0 and A[q,p]==0: 
        return 1 
    else: 
        return A[p,p]/np.sqrt(A[p,p]*A[p,p]+A[q,p]*A[q,p]) 
 
def s(p,q,A): 
    """sinus theta""" 
    if A[p,p]==0 and A[q,p]==0: 
        return 0 
    else: 
        return A[q,p]/np.sqrt(A[p,p]*A[p,p]+A[q,p]*A[q,p]) 
 
def G(q,p,A): 
    """Selon l'algo""" 
    G=np.eye(len(A)) #identité 
    G[p,p]=c(p,q,A) 
    G[p,q]=s(p,q,A) 
    G[q,p]= -s(p,q,A) 
    G[q,q]= c(p,q,A) 
    return sc.matrix(G) 
 
def q(A): 
    """calcule la transposée (donc l'inverse) du facteur Q""" 
    n=len(A) 
    q=np.eye(n) 
    for i in range(0,n): 
        for j in range(0,i): 
            q=G(i,j,A)*q 
            A=G(i,j,A)*A 
    return q 
 
def main(): 
    n=3 
    A = np.array([[1,1,1],[1,2,3],[1,3,6]])
    print (A) 
    Q=q(A) 
    R=Q*A 
    print (R)
    for i in range(0,n): 
        for j in range (0,i): 
            R[i,j]=0 #si résultat non exact 
    print(R)
 
'''    Q=Q.transpose() 
    print ("Q=") 
    print (Q) 
    print ("R=") 
    print (R) 
    print (Q*R) '''
 
if __name__ == '__main__': 
    main() 