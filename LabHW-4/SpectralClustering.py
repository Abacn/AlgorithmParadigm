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
    
"""Find the first k+1 smallest eigenvalues (including 0) of L"""
def smallEigenV(M, k): 
    w, v = splinalg.eigs(M, k+1, which='SR')
    w = w.real
    v = v.real
    return w, v

"""Compute the conductance of a cut""" 
def cutConductance(S, adj_matrix): 
    D = [sum(row) for row in adj_matrix]
    vol_S = sum(D[i] for i in S)
    vol_VS = sum(D) - vol_S
    delta = 0
    for s in S: 
        for i in range(len(D)): 
            if adj_matrix[s][i] and i not in S: 
                delta += 1
    phi = delta/min(vol_S, vol_VS)
    return phi
    
"""Compute the lowest conductance cut with size size_i to size_f"""
def lowConductanceCut(S, adj_matrix, size_i, size_f): 
    conductance = [cutConductance(S[size_i-1:j], adj_matrix) for j in range(size_i, size_f+1)]
    min_conductance = min(conductance)
    cut_size = size_i + conductance.index(min_conductance)
    return min_conductance, cut_size

