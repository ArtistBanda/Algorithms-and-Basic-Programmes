import sys

sys.setrecursionlimit(1000000000)


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_1(n, ar):

    if ar[n]:
        value = ar[n]

    elif n == 1 or n == 0:
        value = n
    else:
        value = fibonacci_1(n - 1, ar) + fibonacci_1(n - 2, ar)
        ar[n] = value

    return value


def fibonacci_2(n):

    fibtable = [0] * (n + 1)
    fibtable[0] = 0
    fibtable[1] = 1
    for x in range(2, n + 1):
        fibtable[x] = fibtable[x - 1] + fibtable[x - 2]

    return fibtable[n]


n = int(raw_input())

# print fibonacci(n)

ar = [None] * (n + 1)

print fibonacci_2(n), "DP"

print fibonacci_1(n, ar), "Memoization"
