import numpy as np
import csv
from LaplacianMatrix import *

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
	adj_matrix, dep_label = readData()
	buildLaplacian(adj_matrix)
