def insertion_sort(ar, start, end):
    if start >= end:
        return

    else:

        curPos = temp = 0

        for x in range(start + 1, end):
            curPos = x

            while curPos > 0 and (ar[curPos] < ar[curPos - 1]):

                temp = ar[curPos]
                ar[curPos] = ar[curPos - 1]
                ar[curPos - 1] = temp

                curPos -= 1


n = int(raw_input("Enter the no. of elements "))

ar = []

for x in range(n):
    ar.append(int(raw_input("Enter element " + str(x + 1) + " ")))

insertion_sort(ar, 0, len(ar))

print ar
