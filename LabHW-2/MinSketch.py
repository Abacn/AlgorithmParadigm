#!/usr/bin/env python3
import numpy as np
import math
import hashlib

def buildHashFunction(x, m, p, a, r): 
	binary_x = list(map(int, format(x, '0{}b'.format(r)))) 	# Convert x to r-bit binary number in the format of a list
	abar = sum([i*j for i,j in zip(a, binary_x)]) # sum of a_i * k_i
	return (abar % p) % m

def minSketch(mode, arr, k, n, p, n_hash): 
	T = len(arr)
	arr_max = max(arr)
	n_bit = int(math.log2(arr_max)+1) # The number of bits for the largest binary value
	CMS = [[0 for i in range(n)] for j in range(n_hash)]
	bloom_filter = [[0] * n] * n_hash
	a = [[np.random.randint(n) for i in range(n_bit)] for j in range(n_hash)] # random matrix to build hash function
	heavy_hitter = []
	# min_hash = 0
	for i_hitter in arr: 
		h_x = []
		for i_hash in range(n_hash): 
			if mode == 'own': 
				h_ix = buildHashFunction(i_hitter, n, p, a[i_hash], n_bit)
			else: 
				h = hashlib.md5(b'%d' %i_hitter).hexdigest()
				h_ix = int(h[i_hash*2:i_hash*2+2], 16) # take the i-th hash to be the i-th bit of the digest
			h_x.append(h_ix)
			if mode != 'conserv_update': 
				CMS[i_hash][h_ix] += 1
		if mode == 'conserv_update': 
			min_hash = min([CMS[i][h_x[i]] for i in range(n_hash)]) # find the minimum in corresponding CMS
			for i_hash in range(n_hash): 
				CMS[i_hash][h_x[i_hash]] = max(CMS[i_hash][h_x[i_hash]], min_hash+1) # only update the minimum one
		f_x = min([CMS[i][h_x[i]] for i in range(n_hash)]) # choose the minimum from the CMS as the frequency
		n_BF = sum([bloom_filter[i][h_x[i]] for i in range(n_hash)])
		# We can also use bloom filter to check if i_hitter is in the heavy hitter here (if f_x >= T/k and n_BF != n_hash: ), which is faster, but may cause error. 
		if f_x >= T/k and i_hitter not in heavy_hitter: # the frequency of the heavy hitter is larger than T/k
			heavy_hitter.append(i_hitter)
			for i_hash in range(n_hash): 
				bloom_filter[i_hash][h_x[i_hash]] = 1
	return heavy_hitter # a list of heavy hitters

