key_mapping = {2: ['a', 'b', 'c'],
               3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'],
               9: ['w', 'x', 'y', 'z'], }


def merge_sort(ar, left, right):

    if right - left > 1:

        mid = (left + right) / 2

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


def number_array_maker(word_array, n):

    number_array = []

    i = 0

    for x in word_array:
        number_array.append(0)
        for y in x:
            number_array[i] = number_array[i] * 10 + helper_funcion(y)
        i += 1

    return number_array


def helper_funcion(value_check):

    for x in range(2, 10):
        for y in key_mapping[x]:
            if y == value_check:
                return x

    raise ValueError("Wrong Input")


def check_highest_count(number_array, n):

    merge_sort(number_array, 0, n)

    max_count = 1
    current = number_array[0]
    current_count = 1

    for x in range(1, n):

        if number_array[x - 1] == number_array[x]:
            current_count += 1

        else:
            if current_count > max_count:
                max_count = current_count
                current = number_array[x - 1]

            current_count = 1

    if current_count > max_count:

        max_count = current_count
        current = number_array[n - 1]

    return current


n = int(raw_input())

word_array = []

for x in range(n):
    word_array.append(list(raw_input()))

number_array = number_array_maker(word_array, len(word_array))

print check_highest_count(number_array, len(number_array))
