def insertion_sort(ar, len_array):

    for x in range(1, len_array):

        curPos = x

        while curPos > 0 and ar[curPos] < ar[curPos - 1]:
            ar[curPos], ar[curPos - 1] = ar[curPos - 1], ar[curPos]
            curPos -= 1
            print "@"


def merge_sort(ar, left, right):

    if right - left > 1:

        mid = (left + right) / 2

        print '#'

        merge_sort(ar, left, mid)
        merge_sort(ar, mid, right)

        merge(ar, left, mid, right)


def merge(ar, left, mid, right):

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


ar = [6, 3, 8, 10, 5, 6]
print ar
ar1 = ar
insertion_sort(ar1, len(ar))
print ar1
merge_sort(ar, 0, len(ar))

print ar
