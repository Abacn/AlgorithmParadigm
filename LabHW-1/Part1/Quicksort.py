# An implementation of quicksort algorithm described of the textbook:
#  Cormen et al (3rd), pp 171
import random

# master function
def Quicksort(arr, randomized=False):
    result = list(arr)
    if randomized:
        _quick_sort_randomized(result, 0, len(arr)-1)
    else:
        _quick_sort(result, 0, len(arr)-1)
    return result


# recurrance function
def _quick_sort(arr, lb ,rb):
    if lb < rb:
        # partition
        x = arr[rb]
        i = lb - 1
        for j in range(lb, rb):
            if arr[j] < x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[rb] = x, arr[i+1]
        # divide
        _quick_sort(arr, lb ,i)
        _quick_sort(arr, i+2 ,rb)


# with random pivot element
def _quick_sort_randomized(arr, lb ,rb):
    if lb < rb:
        # partition
        xidx = random.randint(lb, rb)
        x = arr[xidx]
        arr[xidx] = arr[rb]
        arr[rb] = x
        i = lb - 1
        for j in range(lb, rb):
            if arr[j] < x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[rb] = x, arr[i+1]
        # divide
        _quick_sort_randomized(arr, lb ,i)
        _quick_sort_randomized(arr, i+2 ,rb)


# test
def _test_qsort():
    arr = [random.randint(0,100) for i in range(20)]
    print('Original array: ')
    print(arr)
    sortedarr = Quicksort(arr)
    print('Quicksort conducted: ')
    print(sortedarr)
    sortedarr = Quicksort(arr, True)
    print('Randomized quicksort conducted: ')
    print(sortedarr)

if __name__ == '__main__':
    _test_qsort()