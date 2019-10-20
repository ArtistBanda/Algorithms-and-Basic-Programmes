def selectionSort(ar, n):

    for i in range(n - 1):

        min_index = i

        for j in range(i + 1, n):
            if ar[min_index] > ar[j]:
                min_index = j

        ar[min_index], ar[i] = ar[i], ar[min_index]


# Test Code

n = int(input())

ar = list(map(int, input().split()))

selectionSort(ar, n)

print(ar)
