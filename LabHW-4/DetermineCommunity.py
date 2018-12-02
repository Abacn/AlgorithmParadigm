#!/usr/bin/env python3

import numpy as np
import math
from ReadGraph import * 
from SpectralClustering import *

def vectorDistance(v1, v2): 
	d = 0.
	for i, j in zip(v1, v2): 
		d += (i - j) ** 2
	return math.sqrt(d)

def vertexRepresentation(M): 
	ver_rep = []
	for k in range(20): 
		lambda_s, v_s = smallEigenV(M, k)
		ver_rep.append(v_s)
	ver_rep = list(map(list, zip(*ver_rep)))
	return ver_rep

"""Find the fisrt m closest vertices to the given vertex g"""
def closestVertices(L, g, m, adj_matrix): 
	ver_rep = vertexRepresentation(L)
	distance_g = [vectorDistance(ver_rep[g], ver) for ver in ver_rep]

	"""Index of the clostest m vertices to g (include the index of g)"""
	# sorted_distance_g = np.sort(distance_g)
	# print(min(distance_g))
	clostest_m = sorted(range(len(distance_g)), key=lambda k: distance_g[k])[:m]
	#clostest_m = [int(np.argwhere(distance_g==distance)) for distance in sorted_distance_g[:m]]
	S = []
	conductance = []
	print(clostest_m)
	for ver in clostest_m: 
		S.append(ver)
		conductance.append(cutConductance(S, adj_matrix))
	min_conductance = min(conductance[9:])
	min_index = conductance.index(min_conductance)
	print(min_index)
	community = S[:min_index+1]
	return community
	
if __name__ == '__main__': 
	adj_matrix, dep_label = readData()
	size = np.shape(adj_matrix)[0]
	L = buildLaplacian(adj_matrix)
	"""Find the community that the 0 researcher belongs to"""
	community_0 = closestVertices(L, 0, 110, adj_matrix)
	actual_community_0 = [researcher for researcher in community_0 if dep_label[researcher] == dep_label[0]]
	fraction_0 = len(actual_community_0) / len(community_0)
	print("The fraction of the researcher 0 is %.6f" %fraction_0)
	
	"""Find the community that the researcher 7 belongs to"""
	community_7 = closestVertices(L, 7, 110, adj_matrix)
	actual_community_7 = [researcher for researcher in community_7 if dep_label[researcher] == dep_label[7]]
	fraction_7 = len(actual_community_7) / len(community_7)
	print("The fraction of the researcher 0 is %.6f" %fraction_7)
	
