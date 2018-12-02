import numpy as np
import csv
from time import time
from SpectralClustering import *

def readData(adj_fname='adj.csv', dep_fname='dep.csv'):
    """Read csv format data into an array"""
    adj_matrix = []
    with open(adj_fname, 'r') as fin:
        adj_reader = csv.reader(fin, delimiter=',')
        for row in adj_reader: 
        	adj_matrix.append(list(map(int, row)))
    with open(dep_fname, 'r') as fin:
        dep_label = [int(i) for i in fin.readlines()]
    return adj_matrix, dep_label

if __name__ == '__main__': 
	time_start = time()
	adj_matrix, dep_label = readData()
	L = buildLaplacian(adj_matrix)
	lambda_s, V = smallEigenV(L)
	print(buildCut(V, adj_matrix))
	time_end = time()
	print(time_end - time_start)
