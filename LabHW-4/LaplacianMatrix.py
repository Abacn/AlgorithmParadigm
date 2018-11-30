import numpy as np
def buildLaplacian(adj_matrix): 
	D = [sum(row) for row in adj_matrix]
	L = adj_matrix
	for i in range(len(D)):  
		L[i][i] -= D[i]
	return L
