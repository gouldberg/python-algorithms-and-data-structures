# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import collections


# ----------------------------------------------------------------------------
# clone graph
#  - create a copy of the graph on the vertices reachable from specified vertex
#  - breadth first search
#  - space complexity: O(|V| + |E|), if excluding the space for the result O(|V|)
# ----------------------------------------------------------------------------

class GraphVertex:

    def __init__(self, label):
        self.label = label
        self.edges = []


def clone_graph(graph):
    if not graph:
        return None

    q = collections.deque([graph])
    vertex_map = {graph: GraphVertex(graph.label)}
    while q:
        v = q.popleft()
        for e in v.edges:
            # Try to copy vertex e.
            if e not in vertex_map:
                vertex_map[e] = GraphVertex(e.label)
                q.append(e)
            # Copy edge v -> e.
            vertex_map[v].edges.append(vertex_map[e])

    return vertex_map[graph]


def copy_labels(edges):
    return [e.label for e in edges]


def check_graph(node, graph):
    if node is None:
        raise TestFailure('Graph was not copied')

    vertex_set = set()
    q = collections.deque()
    q.append(node)
    vertex_set.add(node)
    while q:
        vertex = q.popleft()
        if vertex.label >= len(graph):
            raise TestFailure('Invalid vertex label')
        label1 = copy_labels(vertex.edges)
        label2 = copy_labels(graph[vertex.label].edges)
        if sorted(label1) != sorted(label2):
            raise TestFailure('Edges mismatch')
        for e in vertex.edges:
            if e not in vertex_set:
                vertex_set.add(e)
                q.append(e)


# ----------
# model nodes and edges by class GraphVertex
num_nodes = 9
a, b, c, d, e, f, g, h, i = range(num_nodes)
graph = [GraphVertex(i) for i in range(num_nodes)]

edges = [
    (a, b),
    (a, c),
    (c, d),
    (h, d),
    (h, i),
    (i, h),
    (b, e),
    (e, f),
    (f, g),
    (g, e),
    (g, h)
]


for (fr, to) in edges:
    graph[fr].edges.append(graph[to])

print(graph)


# ----------
result = clone_graph(graph[b])

print(result.label)
print(list(result.edges[i].label for i in range(len(result.edges))))

check_graph(result, graph)
