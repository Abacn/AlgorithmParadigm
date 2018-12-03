import numpy as np
import scipy.sparse.linalg as splinalg

def buildLaplacian(adj_matrix): 
    D = [sum(row) for row in adj_matrix]
    n = len(D)
    L = np.zeros((n, n))
    for i in range(n): 
        L[i][i] += D[i]
        for j in range(n): 
            L[i][j] -= adj_matrix[i][j]
    return L
    
"""Find the 1 to (k+1)-th smallest non-zero eigenvalue of L"""
def smallEigenV(M, k): 
    w, v = splinalg.eigs(M, k+1, which='SR')
    w = w.real
    v = v.real
    """Find the eigenvector corresponding to the smallest nonzero eigenvalue"""
    # lambda_s = min(x for x in w if x > 10e-9)
    # v_s = v[int(np.argwhere(w==lambda_s))]
    lambda_s = w[1:]
    v_s = v[:, 1:]
    return lambda_s, v_s
    
def cutConductance(S, adj_matrix): 
    D = [sum(row) for row in adj_matrix]
    nS = sum(D[i] for i in S)
    naS = sum(D) - nS
    delta = 0
    for s in S: 
        for i in range(len(D)): 
            if adj_matrix[s][i] and i not in S: 
                delta += 1
    phi = delta/min(nS, naS)
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
    

