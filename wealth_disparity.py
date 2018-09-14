
"""Wealth Disparity

Indian National Olympiad in Informatics, 2016

Boing Inc, has N employees, numbered 1 … N. Every employee other than Mr. Hojo (the head of the company) has a manager (P[i] denotes the manager of employee i). Thus an employee may manage any number of other employees but he reports only to one manager, so that the organization forms a tree with Mr. Hojo at the root. We say that employee B is a subordinate of employee A if B appears in the subtree rooted at A.

Mr. Hojo, has hired Nikhil to analyze data about the employees to suggest how to identify faults in Boing Inc. Nikhil, who is just a clueless consultant, has decided to examine wealth disparity in the company. He has with him the net wealth of every employee (denoted A[i] for employee i). Note that this can be negative if the employee is in debt. He has already decided that he will present evidence that wealth falls rapidly as one goes down the organizational tree. He plans to identify a pair of employees i and j, j a subordinate of i, such that the wealth difference A[i] - A[j] is maximum. Your task is to help him do this.

Suppose, Boing Inc has 4 employees and the parent (P[i]) and wealth information (A[i]) for each employee are as follows:

i      1   2   3   4  
A[i]   5  10   6  12
P[i]   2  -1   4   2  

P[2] = -1 indicates that employee 2 has no manager, so employee 2 is Mr. Hojo.

In this case, the possible choices to consider are (2,1) with a difference in wealth of 5, (2,3) with 4, (2,4) with -2 and (4,3) with 6. So the answer is 6.
Solution hint

The company hierarchy is a tree. Explore using DFS and incrementally keep track of the maximum difference. Your algorithm should work in time O(n+m).
Input Format

There are three lines of input. The first line contains a single integer N, giving the number of employees in the company. The next line has N integers A[1], .., A[N] that give the wealth of the N employees. The third line has N integers P[1], P[2], .., P[N], where P[i] identifies the manager of employee i. If Mr. Hojo is employee i then, P[i] = -1, indicating that he has no manager.
Output Format

One integer, which is the needed answer. """

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
