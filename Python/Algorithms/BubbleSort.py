def bubbleSort(ar, n):
    for x in range(n - 1):
        for y in range(n - x - 1):
            if ar[y] > ar[y + 1]:
                ar[y], ar[y+1] = ar[y+1], ar[y]


# Test Code

n = int(input())

ar = list(map(int, input().split()))

bubbleSort(ar, n)

print(ar)
