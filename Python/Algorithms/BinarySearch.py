def binarySearch(ar, n, key):
    lb = 0
    ub = n
    while lb < ub:
        mid = int((lb + ub) / 2)
        if ar[mid] == key:
            return mid
        if ar[mid] > key:
            ub = mid - 1
        else:
            lb = mid + 1
    print('!!Value Not Found!!')
    return -1

# Test Code


ar = [1, 4, 6, 8, 10, 12]
n = 6

print('Position of element 10 : ' + str(binarySearch(ar, n, 10) + 1))
