# An implementation of counting sort algorithm described of the textbook:
#  Cormen et al (3rd), pp 195
import random

# master function
def Countingsort(arr):
    k = max(arr)
    arrB = [0] * len(arr)
    _counting_sort(arr, arrB, k)
    return arrB


# recurrance function
def _counting_sort(arr, arrB, k):
    arrC = [0] * (k+1)
    larr = len(arr)
    for j in range(larr):
        arrC[arr[j]] += 1
    # arrC[i] now contains the number of elements equal to i
    for i in range(1, k+1):
        arrC[i] += arrC[i-1]
    # arrC[i] now contains the number of elements less or equal to i
    for j in range(larr-1, -1, -1):
        # index starts from 0 in python
        arrC[arr[j]] -= 1
        arrB[arrC[arr[j]]] = arr[j]


# test
def _test_csort():
    arr = [random.randint(0,100) for i in range(20)]
    print('Original array: ')
    print(arr)
    sortedarr = Countingsort(arr)
    print('Count sort conducted: ')
    print(sortedarr)

if __name__ == '__main__':
    _test_csort()