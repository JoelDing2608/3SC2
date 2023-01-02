import numpy as np
test_matx = np.array([[1,2,3],[0,1,4],[5,6,0]])

#création de la matrice de rotation 
def create_giv(x,y,A):
    n,m = np.shape(A)
    c = (A[x][x]/(np.sqrt(((A[x][x])**2)+((A[y][x])**2))))
    s = (A[y][x]/(np.sqrt(((A[x][x])**2)+((A[y][x])**2))))
    G = np.zeros((n,n))
    np.fill_diagonal(G,1)
    G[n-1][n-1] = c
    G[n-1][n-2] = -s
    G[n-2][n-2] = c
    G[n-2][n-1] = s
    return G

def deco_QR(A):
    n,m = np.shape(A)
    print(A)
    for i in range (n-1):
        print(i)
        for j in range(i+1,n):
            print(j)
            G = create_giv(i,j,A)
            print(G)
            A = np.dot(G,A)
            print (A)
        print(A)
    print (A)
deco_QR(test_matx)