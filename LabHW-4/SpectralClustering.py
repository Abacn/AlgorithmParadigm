import numpy as np
def buildLaplacian(adj_matrix): 
	D = [sum(row) for row in adj_matrix]
	n = len(D)
	L = np.zeros((n, n))
	for i in range(n): 
		L[i][i] += D[i]
		for j in range(n): 
			L[i][j] -= adj_matrix[i][j]
	return L, D
	
"""Find the smallest non-zero eigenvalue of L"""
def smallEigenV(M): 
	w, v = np.linalg.eig(M)
	lambda_s = min(x for x in w if x > 10e-9)
	"""Find the eigenvector corresponding to the smallest nonzero eigenvalue"""
	v_s = v[int(np.argwhere(w==lambda_s))]
	return lambda_s, v_s
	
def cutConductance(S, adj_matrix): 
	D = [sum(row) for row in adj_matrix]
	nS = sum(D[i] for i in S)
	naS = sum(D) - nS
	if nS == 0: 
		print("ns is 0")
		return 0
	if naS == 0: 
		print("nas is 0")
		return 0
	delta = 0
	for s in S: 
		for i in range(len(D)): 
			if adj_matrix[s][i] and i not in S: 
				delta += 1
	phi = delta/min(nS, naS)
	return phi
	
def buildCut(V, D, adj_matrix): 
	sorted_V = np.sort(V)
	S = []
	conductance = []
	for v in sorted_V[:-1]: 
		S.append(int(np.argwhere(V==v)))
		conductance.append(cutConductance(S, adj_matrix))
	return min(conductance)
