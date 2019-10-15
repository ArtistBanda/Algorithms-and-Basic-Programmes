def quick_sort(arr, left, right):

    if right - left <= 1:
        return

    left_pointer = left + 1

    for right_pointer in range(left + 1, right):

        if arr[right_pointer] < arr[left]:

            arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]

            left_pointer += 1

    arr[left], arr[left_pointer - 1] = arr[left_pointer - 1], arr[left]

    quick_sort(arr, left, left_pointer)
    quick_sort(arr, left + 1, right)


n = int(input("Enter the number of elements "))

ar = [None] * n

for x in range(n):
    ar[x] = int(input("Enter Element " + str(x + 1) + " "))

quick_sort(ar, 0, n)

print(ar)
