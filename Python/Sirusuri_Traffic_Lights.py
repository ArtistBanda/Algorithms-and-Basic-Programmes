"""
Siruseri Traffic Lights
Adapted from Traffic Lights, International Olympiad in Informatics, 1999

In Siruseri, there are junctions connected by roads. There is at most one road between any pair of junctions. There is no road connecting a junction to itself. The travel time for a road is the same in both directions.

At every junction there is a single traffic light. These traffic lights are a bit peculiar. Starting from time 0, each light flashes green once every T time units, where the value of T is different for each junction.

A vehicle that is at a junction can start moving along a road only when the light at the current junction flashes green. If a vehicle arrives at a junction between green flashes, it must wait for the next green flash before continuing in any direction. If it arrives at a junction at exactly the same time that the light flashes green, it can immediatly proceed along any road originating from that junction.

You are given a city map that shows travel times for all roads. For each junction i, you are given Ti, the time period between green flashes of the light at that junction. Your task is to find the minimum time taken from a given source junction to a given destination junction for a vehicle when the traffic starts.

Solution hint
Use Dijkstra's algorithm. At each phase, from the current shortest time for a given junction, compute when the next green flash will occur to let you travel to its neighbours and use this to update shortest path information.

Input Format
There are N junctions and M roads. The junctions are identified by integers 1 through N.

The first line of input contains two integers: the source junction and the destination junction.
The second line contains two integers: N and M.
The third line contains N integers, T1, T2,…TN, describing the time periods at which the traffic lights flash green. The light at junction i flashes green at times 0, Ti, 2Ti, 3Ti, …
The next M lines contain information about the M roads. Each line has three integers i, j, lij , where:
i and j are the junctions connected by this road
lij is the time required to move from junction i to junction j using this road
Output Format
A single line consisting of a single integer, the time taken by a minimum-time path from source to destination.

Constraints:
2 ≤ N ≤ 300
1 ≤ M ≤ 14,000
1 ≤ T_i ≤ 100
1 ≤ lij ≤ 100
"""


from __future__ import division

n, m = 0, 0

X, Y = map(int, raw_input().split())

n, m = map(int, raw_input().split())

adjacency_list = {}

for x in range(1, n + 1):
    adjacency_list[x] = []

time_matrix = [n]

time_matrix = map(int, raw_input().split())

x, y, z = 0, 0, 0

maxDis = 0

for i in range(m):
    x, y, z = map(int, raw_input().split())
    maxDis += z
    adjacency_list[x].append([y, z])
    adjacency_list[y].append([x, z])


def minIndex(distance, visited, minDis, n):

    min_index = -1

    for count in range(1, n + 1):
        if distance[count] < minDis and not visited[count]:
            min_index = count
            minDis = distance[count]

    return min_index


def dijkstra_short(s, n, maxDis, Y):

    visited = [False] * (n + 1)
    distance = [maxDis] * (n + 1)

    distance[s] = 0

    for count in range(1, n + 1):

        u = minIndex(distance, visited, maxDis, n)

        visited[u] = True

        total = 0

        if distance[u] % time_matrix[u - 1] == 0:
            total = distance[u]
        elif (distance[u] / time_matrix[u - 1]) > 1:
            total = time_matrix[u - 1]
            while (distance[u] / total) > 1:
                total += time_matrix[u - 1]
        elif distance[u] / time_matrix[u - 1] < 1:
            total = time_matrix[u - 1]

        for x in adjacency_list[u]:
            if not visited[x[0]]:
                if distance[x[0]] > (total + x[1]):
                    distance[x[0]] = total + x[1]

    return distance[Y]


print dijkstra_short(X, n, maxDis, Y)
