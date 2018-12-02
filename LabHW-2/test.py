#!/usr/bin/env python3
import numpy as np
from MinSketch import minSketch

def readData(filename): 
	with open(filename, 'r') as fin: 
		line = fin.read()
		data = [int(i) for i in line.split(',')]
		return data

if __name__ == '__main__': 
	data = readData('data.txt')
	k = 100		# Aim to find elements more than T/k occurences in the data
	n = 256 	# Size of each hash table
	p = 557		# p is a prime number larger than n
	n_hash = 3
	mode_list = ['own', 'standard', 'conserv_update']
	stream_list = ['Forward', 'Reverse', 'Uniform']
	data_stream = [0 for i in range(len(stream_list))]
	data_stream[0] = data	# forward stream
	data_stream[1] = list(reversed(data))	# reversed stream
	data_stream[2] = np.random.permutation(data)	# uniform random stream
	n_ave = 5
	ave_hitter = [[0 for i in range(len(mode_list))] for j in range(len(stream_list))]
	for i in range(len(stream_list)): 
		for j in range(n_ave): 
			n_hitter = [len(minSketch(mode, data_stream[i], k, n, p, n_hash)) for mode in mode_list]
			ave_hitter[i] = [sum(x) for x in zip(ave_hitter[i], n_hitter)]
		ave_hitter[i] = [i_hitter/n_ave for i_hitter in ave_hitter[i]]
	for i in range(len(stream_list)): 
		print('%s stream: \n%s\t%d\t%s\t%d\t%s\t%d\n' %(stream_list[i], mode_list[0], ave_hitter[i][0], mode_list[1], ave_hitter[i][1], mode_list[2], ave_hitter[i][2]))
