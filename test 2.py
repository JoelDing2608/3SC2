import numpy as np
mat = np.array([[2,12,-3],[1,-6,-3],[2,0,18]])
def ResolGivens(A):
    """
    A est une matrice carrée de taille n, inversible
    b est une matrice de taille (1,n)
    On cherche a résoudre le système Ax = b avec l'algorithme de Givens
    """

    n = len(A)
    x = np.zeros(n)
    R = np.zeros((n,n))
    Q = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            Q[i][j] = A[i][j]
            R[i][j] = A[i][j]
    for i in range(n):
        for j in range(i+1, n):
            c = R[i][i]/np.sqrt(R[i][i]**2 + R[j][i]**2)
            s = R[j][i]/np.sqrt(R[i][i]**2 + R[j][i]**2)
            G = np.zeros((n,n))
            np.fill_diagonal(G, 1)
            G[i][i] = c
            G[j][j] = c
            G[i][j] = s
            G[j][i] = -s
            R = np.dot(G, R)
            Q = np.dot(Q, G.T)
            print(R)
            print(Q)
ResolGivens(mat)


