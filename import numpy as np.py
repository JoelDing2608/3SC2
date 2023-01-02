import numpy as np

# Matrice de Givens 1
G1 = np.array([[1, 0], [0, 1]])

# Matrice de Givens 2
G2 = np.array([[np.cos(np.pi/4), np.sin(np.pi/4)], [-np.sin(np.pi/4), np.cos(np.pi/4)]])
print(G2)
# Produit des deux matrices
G3 = np.dot(G1, G2)
print (G3)

# Vérification que le produit n'est pas une matrice de Givens
if not all(np.abs(G3[:, 0]) == 1) or not all(G3[:, 1] == 0):
    print("Le produit des deux matrices n'est pas une matrice de Givens")
else:
    print("Le produit des deux matrices est une matrice de Givens")