# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# adjacency list representation of the graph
# ----------------------------------------------------------------------------

# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no. of the vertices "V"
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


# ----------
V = 5
graph = Graph(V)

graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()


# ----------------------------------------------------------------------------
# adjacency list representation of the graph
# ----------------------------------------------------------------------------

a, b, c, d, e, f, g, h = range(8)

N = [
    {b, c, d, e, f},    # a
    {c, e},             # b
    {d},                # c
    {e},                # d
    {f},                # e
    {c, g, h},          # f
    {f, h},             # g
    {f, g},             # h
]

print(N)

print(b in N[a])

len(N[f])


# ----------------------------------------------------------------------------
# adjacency list representation of the graph
#  - use hashable for node label
# ----------------------------------------------------------------------------

N = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}

print(N)

print(b in N[a])

len(N[f])


# ----------------------------------------------------------------------------
# adjacency list representation of the graph
#  - generate randomly
# ----------------------------------------------------------------------------

from random import seed
from random import sample, randrange, shuffle

n = 6

seed(2365)

G = dict()
seq = list(range(n))
shuffle(seq)

rest = set(seq)
for x in seq[:-1]:
    rest.remove(x)
    m = randrange(1, len(rest)+1)
    G[x] = set(sample(rest, m))


print(G)

