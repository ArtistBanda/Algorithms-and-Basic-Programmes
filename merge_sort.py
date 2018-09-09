def merge_sort(ar, left, right):

        # recursive merge sort function

    if right - left > 1:

        mid = (left + right) / 2

        merge_sort(ar, left, mid)
        merge_sort(ar, mid, right)

        merge(ar, left, mid, right)


def merge(ar, left, mid, right):

        # funtion to merge two sorted arrays in ascending order

    first_half = ar[left:mid]
    second_half = ar[mid:right]

    i = j = 0
    k = left

    while i < mid - left and j < right - mid:

        if first_half[i] <= second_half[j]:
            ar[k] = first_half[i]
            i += 1

        else:
            ar[k] = second_half[j]
            j += 1

        k += 1

    if i != mid - left - 1:
        while i < mid - left:
            ar[k] = first_half[i]
            i += 1
            k += 1

    if j != right - mid - 1:
        while j < right - mid:
            ar[k] = second_half[j]
            j += 1
            k += 1


n = int(raw_input("Enter the number of elements for the list "))

ar = []

for x in range(n):
    ar.append(int(raw_input("Enter the element " + str(x + 1) + " ")))

print "Merge Sorting... "

merge_sort(ar, 0, len(ar))

print ar
