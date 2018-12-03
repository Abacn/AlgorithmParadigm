#!/usr/bin/env python3

import numpy as np
import random
from ReadGraph import *
from SpectralClustering import *

def randomSample(size, nv): 
    sample = random.sample(range(size), nv)
    return sample
    
if __name__ == '__main__': 
    number_samples = 5
    number_vertices = 200
    adj_matrix, dep_label = readData()
    size = np.shape(adj_matrix)[0]
    conductance = []
    for i in range(number_samples): 
        conductance.append(cutConductance(randomSample(size, number_vertices), adj_matrix))
    ave_cond = sum(conductance)/len(conductance)
    print('The average conductance of %d ransom sample is %.6f' %(number_samples, ave_cond))
    L = buildLaplacian(adj_matrix)
    lambda_s, V = smallEigenV(L)
    print(buildCut(V, adj_matrix, 100, 400))
