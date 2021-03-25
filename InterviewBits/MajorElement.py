"""
Given an array of size n, find the majority element. The majority element is the element that appears more than floor(n/2) times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example :

Input : [2, 1, 2]
Return  : 2 which occurs 2 times which is greater than 3/2. 
"""


def majorityElement(A):
    n = len(A)
    count_dict = {}
    for x in range(n):
        if A[x] not in count_dict:
            count_dict[A[x]] = 1
        else:
            count_dict[A[x]] += 1
            
    max_val_count= count_dict[A[0]]
    max_val = A[0]
    for key, value in count_dict.items():
        if value > max_val_count:
            max_val_count = value
            max_val = key
            
    return max_val

print(majorityElement([2, 1, 2]))