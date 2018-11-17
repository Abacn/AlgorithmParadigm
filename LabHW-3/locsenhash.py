from __future__ import division, print_function
from time import time
import numpy as np

from common import *


def generateVectors(k, dim):
    """generate k random unit vectors"""
    v = np.random.normal(size=(k, dim))
    ssq = np.sum(v**2, axis=1)
    for rp in range(k):
        v[rp,:] = v[rp,:]/ssq[rp]
    return v


def cdotSparseDense(a, v):
    """dot product of a sparse vector (a) and dense vectors (v)"""
    result = np.zeros(v.shape[0])
    for idx, num in a:
        result += v[:, idx]*num
    return result


def gethash(a, v, k, l):
    """Get l hash values of a sparse vector (a) according to the hash functions with parameter v
return a l-dimensional integer"""
    dotresult = np.sign(cdotSparseDense(a, v))
    result = [0]*l
    for rp in range(l):
        idxstart = k*rp
        for rq in range(k):
            result[rp] *= 2
            if dotresult[rp*k+rq] > 0:
                # positive
                result[rp] += 1
    return result


def constructHashtable(data, v, k, l):
    """Construct local sensitive hash table"""
    hstbl = [dict() for rp in range(l)]
    for idx in data:
        hsvalues = gethash(data[idx], v, k, l)
        for rp, val in enumerate(hsvalues):
            if val not in hstbl[rp]:
                hstbl[rp][val] = []
            hstbl[rp][val].append(idx)
    return hstbl


def findNearest(data, classlabel, k, l):
    """Find nearest neighbor by local sensitive hashing"""
    # find the dimension (61067)
    dim = 61067
    searchcount = 0
    errorcount = 0
    v = generateVectors(k*l, dim)
    hstbl = constructHashtable(data, v, k, l)
    sas = [0]*1000
    for i in range(1000):
        sas[i] = sum([x[1]*x[1] for x in data[i] ])
    for rp in range(len(data)):
        # find nearest neighbor of data[rp] in hashtable (apart self)
        x = data[rp]
        sa = sas[rp]
        hs = gethash(x, v, k, l)
        maxSimu = (float("-inf"), None)
        # use a set to record the point that has been searched
        visited = set([rp])
        for idx, h in enumerate(hs):
            for idy in hstbl[idx][h]:
                if idy in visited:
                    # skip self and visited points
                    continue
                simu = similarity(x, data[idy], sa, sas[idy])
                if simu > maxSimu[0]:
                    maxSimu = (simu, idy)
                visited.add(idy)
                searchcount += 1
        # debug: print the result
        #if maxSimu[1] is None:
        #    print("fail")
        #else:
        #    print(classlabel[maxSimu[1]], maxSimu[1])
        if maxSimu[1] is None or classlabel[maxSimu[1]] != classlabel[rp]:
            errorcount += 1
    searchcount /= 1000
    return (errorcount, searchcount)

if __name__ == '__main__':
    data, classlabel = readData('data.csv', 'label.csv')
    k = 16
    l = 16
    start = time()
    nn = findNearest(data, classlabel, k, l)
    print("k: %d\tl: %d" % (k, l))
    print("Hash:\nError\tAve comp")
    print(nn)
    print("Seconds consumed: %f" % (time() - start))