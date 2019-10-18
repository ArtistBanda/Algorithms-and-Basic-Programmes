class graph(object):
    def __init__(self, size):
        self.adjacency_list = {}
        self.maxSize = 0
        for x in range(1, size + 1):
            self.adjacency_list[x] = []
        self.size = size

    def add_node(self, start, end, weight):

        self.maxSize += weight

        self.adjacency_list[start].append([end, weight])
        self.adjacency_list[end].append([start, weight])

    def print_graph(self):
        for x in range(1, self.size + 1):
            print(x, " : ", self.adjacency_list[x])


def minIndex(g, visited, distance, minDis):

    minIndex = -1

    for count in range(1, g.size + 1):
        if distance[count] <= minDis and (not visited[count]):
            minIndex = count
            minDis = distance[count]

    return minIndex


def dijksrta_short(g, start, end):
    visited = [False] * (g.size + 1)
    distance = [g.maxSize] * (g.size + 1)

    distance[start] = 0

    for _ in range(g.size):

        minIndex1 = minIndex(g, visited, distance, g.maxSize)

        visited[minIndex1] = True

        for x in g.adjacency_list[minIndex1]:

            if not visited[x[0]]:
                if distance[x[0]] > distance[minIndex1] + x[1]:
                    distance[x[0]] = distance[minIndex1] + x[1]

    return distance[end]


g = graph(5)
g.add_node(1, 2, 10)
g.add_node(2, 3, 15)
g.add_node(1, 3, 70)
g.add_node(2, 4, 15)
g.add_node(4, 5, 20)
g.add_node(1, 5, 100)

g.print_graph()

print(dijksrta_short(g, 1, 5))
