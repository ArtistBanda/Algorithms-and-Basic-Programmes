n = int(raw_input())

wealth_array = map(long, raw_input().split())

parent_array = map(int, raw_input().split())

adjacency_list = [None] * (n + 1)

for x in range(1, n + 1):
    adjacency_list[x] = []

for x in range(1, n + 1):
    if parent_array[x - 1] != -1:
        adjacency_list[parent_array[x - 1]].append(x)

for x in range(n):
    if parent_array[x] == -1:
        top1 = x + 1

print adjacency_list

temp = [top1]

visited = [False] * (n + 1)

maxValue = -9999999999999999999

flag = True


def find_max(top, maxValue, flag=False):

    visited[top] = True

    for x in adjacency_list[top]:
        if not visited[x]:
            temp.append(x)
            maxValue = find_max(x, maxValue)

    if top != top1:

        tempLength = len(temp)

        cur = wealth_array[temp[tempLength - 1] - 1]

        for x in range(tempLength - 1):
            temp1 = wealth_array[temp[x] - 1]

            if (temp1 > 0 and cur > 0) or (temp1 < 0 and temp1 < 0):
                tempMax = abs(abs(temp1) - abs(cur))

            elif temp1 < 0 and cur > 0:
                tempMax = abs(temp1) + cur

            else:
                tempMax = temp1 + abs(cur)

            if maxValue < tempMax:
                maxValue = tempMax

        temp.pop()

    return maxValue


maxValue = find_max(top1, maxValue, True)

if n == 1:
    print 0

else:
    print maxValue
