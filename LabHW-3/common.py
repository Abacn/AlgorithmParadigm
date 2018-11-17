from __future__ import division
import math, csv

def similarity(a, b, sa=None, sb=None):
    """compute the similarity between two articles"""
    if sa is None:
        sa = sum([x[1]*x[1] for x in a])
    if sb is None:
        sa = sum([x[1]*x[1] for x in b])
    return cdot(a, b)/math.sqrt(sa*sb)

    
def readData(fname='data.csv', labelfname='label.csv'):
    """Read csv format data into a dict, with keys are the indices of articles,
and values is a list of tuples with (word indices, frequency)"""
    result = {}
    with open(fname, 'r') as fin:
        csvreader = csv.reader(fin, delimiter=',')
        for row in csvreader:
            intr = int(row[0])-1
            if intr not in result:
                result[intr] = []
            result[intr].append((int(row[1])-1, int(row[2])))
    for ks in result:
        result[ks].sort(key=lambda x: x[0])
    with open(labelfname, 'r') as fin:
        classlabel = [int(i) for i in fin.readlines()]
    return result, classlabel
    
    
def cdot(a, b):
    """Dot product. Input form is two index-sorted sparse vector"""
    i = j = 0
    lenA = len(a)
    lenB = len(b)
    result = 0.0
    while i < lenA and j < lenB:
        if b[j][0] < a[i][0]:
            j += 1
        else:
            if b[j][0] == a[i][0]:
                result += a[i][1]*b[j][1]
                j += 1
            i += 1
    return result