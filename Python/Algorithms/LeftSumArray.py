# Given, an array of size n. Find an element that divides the array into two sub-arrays with equal sum.

def naive_method(arr):
    # slower method
    # O(n^2)
    n = len(arr)

    counter = 0
    for x in range(n):
        # calculating sum of left and right part and comparing values
        if sum(arr[:x]) == sum(arr[x + 1:]):
            counter += 1

    return counter


def fast_method(arr):
    # faster method
    # O(n)

    left_sum_array = []
    right_sum_array = []

    temp_sum = 0
    for x in arr:
        temp_sum += x
        left_sum_array.append(temp_sum)

    temp_sum = 0
    for x in reversed(arr):
        temp_sum += x
        right_sum_array.append(temp_sum)

    counter = 0
    # comparing left_sum_array and right_sum_array
    # incrementing counter whenever the values collide
    for x, y in zip(left_sum_array, right_sum_array):
        if x == y:
            counter += 1

    return counter


# Test Code

arr = [2, 3, 4, 1, 5, 4]
# Output : 1
# Subarrays are : {2, 3, 4} and {4, 5}

print(fast_method(arr))
