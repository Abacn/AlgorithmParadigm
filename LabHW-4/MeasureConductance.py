#!/usr/bin/env python3
"""Test 1-3"""
import numpy as np
import random
from ReadGraph import *
from SpectralClustering import *

def randomSample(size, nv): 
    sample = random.sample(range(size), nv)
    return sample
    
def buildCut(V, adj_matrix, size_i, size_f): 
    print(min(V), max(V))
    sorted_V_index = sorted(range(len(V)), key=lambda k: V[k])
    return lowConductanceCut(sorted_V_index, adj_matrix, size_i, size_f)

if __name__ == '__main__': 
    number_samples = 5
    number_vertices = 200
    adj_matrix, dep_label = readData()
    size = np.shape(adj_matrix)[0]
    L = buildLaplacian(adj_matrix)
    
    """Ten smallest eigenvalues of Laplacian"""
    small_eig_vals, small_eig_vecs = smallEigenV(L, 10)
    print("The ten smallest eigenvalues of Laplacian: ")
    print (", ".join("%.3f" % vals for vals in small_eig_vals))

    """Calculate conductance for several random generated samples"""
    conductance = [cutConductance(randomSample(size, number_vertices), adj_matrix) for i in range(number_samples)]
    ave_cond = sum(conductance)/len(conductance)
    print('The average conductance of %d ransom sample is %.6f' %(number_samples, ave_cond))
    
    lambda_s, v_s = smallEigenV(L, 1)
    lambda_s = lambda_s[1:]
    v_s = v_s[:, 1:]
    small_cond, cut_size = buildCut(v_s, adj_matrix, 100, 400)
    print('The smallest conductance is %.3f, the size of the corresponding cut is %d' %(small_cond, cut_size))
