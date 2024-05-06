# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import collections


# ----------------------------------------------------------------------------
# deadlock detection
#  - We can check for the existence of a cycle in G by running DFS on G.
#    DFS maintains a color for each vertex. Initially, all vertices are white.
#    When a vertex is first discovered, it is colored gray.
#    When DFS finished processing a vertex, that vertex is colored black.
#    A cycle exists if and only if DFS discovers an edge from a gray vertex to a gray vertex
#  - time complexity:  O(|V| + |E|): we iterate over all vertices, and spend a constant amount of time per edge.
#  - space complexity: O(|V|), which is maximum stack depth
# ----------------------------------------------------------------------------

class GraphVertex:

    WHITE, GRAY, BLACK = range(3)

    def __init__(self):
        self.color = GraphVertex.WHITE
        self.edges = []

def is_deadlocked(graph):
    def has_cycle(cur):
        # Visiting a gray vertex means a cycle.
        if cur.color == GraphVertex.GRAY:
            return True

        # Marks current vertex as a gray one
        cur.color = GraphVertex.GRAY

        # Traverse the neighbor vertices.
        if any(next.color != GraphVertex.BLACK and has_cycle(next) for next in cur.edges):
            return True
        # Marks current vertex as black.
        cur.color = GraphVertex.BLACK
        return False

    return any(vertex.color == GraphVertex.WHITE and has_cycle(vertex) for vertex in graph)


# ----------
# cde is cycle and ijl is cycle

# ----------
# model nodes and edges by class GraphVertex

num_nodes = 12
a, b, c, d, e, f, g, h, i, j, k, l = range(num_nodes)
graph = [GraphVertex() for _ in range(num_nodes)]

# cde and ijl are cycle
edges = [
    (a, c),
    (a, b),
    (b, k),
    (c, e),
    (d, c),
    (e, d),
    (f, g),
    (g, h),
    (i, j),
    (j, l),
    (k, i),
    (l, i)
]

for (fr, to) in edges:
    graph[fr].edges.append(graph[to])

print(graph)


# ----------
is_deadlocked(graph=graph)
