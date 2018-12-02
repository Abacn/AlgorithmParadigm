import numpy as np
def buildLaplacian(adj_matrix): 
	D = [sum(row) for row in adj_matrix]
	n = len(D)
	L = np.zeros((n, n))
	for i in range(n): 
		L[i][i] += D[i]
		for j in range(n): 
			L[i][j] -= adj_matrix[i][j]
	return L
	
"""Find the first k smallest non-zero eigenvalue of L"""
def smallEigenV(M, k): 
	w, v = np.linalg.eig(M)
	w = w.real
	v = v.real
	lambda_s = min(x for x in w if x > 10e-9)
	"""Find the eigenvector corresponding to the smallest nonzero eigenvalue"""
	v_s = v[int(np.argwhere(w==lambda_s))]
	return lambda_s, v_s
	
def cutConductance(S, adj_matrix): 
	D = [sum(row) for row in adj_matrix]
	vol_S = sum([D[i] for i in S])
	vol_aS = sum(D) - vol_S
	delta = 0
	for s in S: 
		for i in range(len(D)): 
			if adj_matrix[s][i] and i not in S: 
				delta += 1
	print(len(S), delta, min(vol_S, vol_aS))
	phi = delta/min(vol_S, vol_aS)
	return phi
	
def buildCut(V, adj_matrix, begin, end): 
	sorted_V = np.sort(V)
	S = []
	conductance = []
	for i, v in zip(range(len(V)), sorted_V[:-1]): 
		S.append(int(np.argwhere(V==v)))
		conductance.append(cutConductance(S, adj_matrix))
	min_conductance = min(conductance[begin-1, end])
	cut_size = int(np.argwhere(conductance==min_conductance))+1
	return min_conductance, cut_size
	
