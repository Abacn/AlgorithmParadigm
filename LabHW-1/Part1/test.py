# Running tests on quicksort and counting sort

from time import time
from Quicksort import Quicksort
from Countingsort import Countingsort
from readNumbers import readNumbers

def benchmark(algo, arr, times=5):
    timestart = time()
    for rp in range(times):
        result  = algo(arr)
    timeend = time()
    return (timeend-timestart)*1000/times, result

if __name__ == '__main__':
    arrA1 = readNumbers('../test/A1.txt')
    arrA2 = readNumbers('../test/A2.txt')

    sorttime = [0]*2
    print('Testing results:\n--------------------\nFile\tn\tQuicksort\tCoungintsort')
    sorttime[0],_ = benchmark(Quicksort, arrA1)
    sorttime[1],_ = benchmark(Countingsort, arrA1)
    print('A1.txt\t%d\t%.3f\t%.3f' % (len(arrA1), sorttime[0], sorttime[1]))
    sorttime[0],_ = benchmark(Quicksort, arrA2)
    sorttime[1],_ = benchmark(Countingsort, arrA2)
    print('A2.txt\t%d\t%.3f\t%.3f' % (len(arrA2), sorttime[0], sorttime[1]))
    # sorttime[0],_ = benchmark(lambda arr: Quicksort(arr, True), arrA1)
    # sorttime[1],_ = benchmark(lambda arr: Quicksort(arr, True), arrA2)
    # print('Rand Quicksort\t%.3f\t%.3f' % tuple(sorttime))