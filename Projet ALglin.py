import numpy as np
test_matx = np.array([[1,1,1],[1,2,3],[1,3,6]])

#décomposition QR
def deco_QR(R):
    n,m = np.shape(R)
    Q = np.eye(n)
    print(R)
    for j in range (1,n-1):
        print(j)
        for i in range (j+1,n-1):
            print(i)
            r = np.sqrt(R[j,j]**2+R[i,j]**2)
            if r != 0:
                c = R[j,j]/r
                s = R[i,j]/r
                g = G(n,i,j,c,s)
                print(g)
                R = np.dot(g,R)
                Q = Q*g.T
                print (R)
            else:
                R = R
                Q = Q
    print(Q)
    print (R)

def G(n,i,j,c,s):
    M = np.eye(n)
    M[i,i] = M[j,j] = c
    M[i,j],M[j,i] = -s, s
    return M
deco_QR(test_matx)
A = np.random.rand(n, n) #matrice aléatoire 
    for i in range(0,n): 
        for j in range (0,n): 
            A[i,j]=randint(0,9)-4 