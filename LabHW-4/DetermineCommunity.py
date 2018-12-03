#!/usr/bin/env python3
"""Test 4-5"""
import numpy as np
import math
from ReadGraph import * 
from SpectralClustering import *

def vectorDistance(v1, v2): 
    d = 0.
    for i, j in zip(v1, v2): 
        d += (i - j) ** 2
    return math.sqrt(d)

def vertexRepresentation(M, k=20): 
    ver_rep = []
    lambda_s, v_s = smallEigenV(M, k)
    """Discard the eigenvalue zero,as in Test 1, we find there is only one eigenvalue 0"""
    lambda_s = lambda_s[1:]
    v_s = v_s[:, 1:]
    for rp in range(k):
        ver_rep.append(v_s[:, rp])
    ver_rep = list(map(list, zip(*ver_rep)))
    return ver_rep

"""Find the fisrt m closest vertices to the given vertex g, and then find the lowest conductance cut from m vertices"""
def closestVertices(L, g, m, adj_matrix): 
    ver_rep = vertexRepresentation(L)
    distance_g = [vectorDistance(ver_rep[g], ver) for ver in ver_rep]

    """Index of the clostest m vertices to g (include the index of g)"""
    clostest_m = sorted(range(len(distance_g)), key=lambda k: distance_g[k])[:m]
    min_conductance, cut_size = lowConductanceCut(clostest_m, adj_matrix, 10, 110)
    community = clostest_m[:cut_size]
    return community
    
if __name__ == '__main__': 
    adj_matrix, dep_label = readData()
    size = np.shape(adj_matrix)[0]
    L = buildLaplacian(adj_matrix)

    """Find the community that the researcher 0 belongs to"""
    community_0 = closestVertices(L, 0, 110, adj_matrix)
    actual_community_0 = [researcher for researcher in community_0 if dep_label[researcher] == dep_label[0]]
    fraction_0 = len(actual_community_0) / len(community_0)
    print("The size of the community that researcher 0 belongs to is %d" %len(community_0))
    print("The fraction of the correct prediction for researcher 0 is %.6f" %fraction_0)
    print("Community 0: ")
    print(", ".join("%d" %researcher for researcher in community_0))
    
    """Find the community that the researcher 7 belongs to"""
    community_7 = closestVertices(L, 7, 110, adj_matrix)
    actual_community_7 = [researcher for researcher in community_7 if dep_label[researcher] == dep_label[7]]
    fraction_7 = len(actual_community_7) / len(community_7)
    print("\nThe size of the community that researcher 7 belongs to is %d" %len(community_7))
    print("The fraction of the correct prediction for the researcher 7 is %.6f" %fraction_7)
    print("Community 7: ")
    print(", ".join("%d" %researcher for researcher in community_7))
    
