from __future__ import print_function
import six
from time import time
from common import *


def findNearest(data, classlabel, query, sas=None):
    """Find nearest neighbor by brute force"""
    if isinstance(query, six.string_types):
        query = int(query)
    if isinstance(query, int):
        # query point is an index in data
        querydata = data[query]
        queryidx = query
        if sas is None:
            sb = sum([x[1] * x[1] for x in querydata])
        else:
            sb = sas[query]
    else:
        # query point is a vector
        querydata = query
        queryidx = None
        sb = sum([x[1]*x[1] for x in querydata])
    maxSimu = (float("-inf"), None)
    for ind in data.keys():
        if queryidx == ind:
            # skip self
            continue
        sa = None
        if sas is not None:
            sa = sas[ind]
        simu = similarity(data[ind], querydata, sa, sb)
        if simu > maxSimu[0]:
            maxSimu = (simu, ind)
    # return the type, similarity, and index of nearest neighbor
    return classlabel[maxSimu[1]], maxSimu[0], maxSimu[1]
    
if __name__ == '__main__':
    data, classlabel = readData('data.csv', 'label.csv')
    countfalse = 0
    sas = [0]*1000
    start = time()
    for i in range(1000):
        sas[i] = sum([x[1]*x[1] for x in data[i] ])
    for i in range(1000):
        nn = findNearest(data, classlabel, i, sas)
        # debug: print every result
        #print(nn[0], nn[2])
        if nn[0] != classlabel[i]:
            countfalse += 1
    print("Brute force:\nError\tAve comp")
    print(countfalse,999)
    print("Seconds consumed: %f" % (time() - start))
