# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

from heapq import heappush, heappop

from copy import deepcopy


# ----------------------------------------------------------------------------
# find shortest path by Johnson algorithm
#  - time complexity: O(m * n * log(n))  (n: number of nodes, m: number of edges)
# ----------------------------------------------------------------------------

inf = float('inf')

def relax(W, u, v, D, P):
    d = D.get(u, inf) + W[u][v]
    if d < D.get(v, inf):
        D[v], P[v] = d, u
        return True


def find_shortest_path_bellman_ford(G, s):

    D, P = {s: 0}, {}

    for i, rnd in enumerate(G):
        changed = False
        for u in G:
            for v in G[u]:
                if relax(G, u, v, D, P):
                    changed = True
                    print(f'{i+1} : ({u},{v})  D[{v}]={D[v]}')
        if not changed: break

    else: raise ValueError('negative cycle')

    return D, P


def find_shortest_path_dijkstra(G, s):

    D, P, Q, S = {s: 0}, {}, [(0, s)], set()

    while Q:
        _, u = heappop(Q)
        if u in S: continue
        S.add(u)
        for v in G[u]:
            relax(G, u, v, D, P)
            heappush(Q, (D[v], v))

    return D, P


def find_shortest_path_Johnson(G):

    G = deepcopy(G)
    s = object()
    G[s] = {v: 0 for v in G}

    h, _ = find_shortest_path_bellman_ford(G, s)
    del G[s]
    for u in G:
        for v in G[u]:
            G[u][v] += h[u] - h[v]
    D, P = {}, {}
    for u in G:
        D[u], P[u] = find_shortest_path_dijkstra(G, u)
        for v in G:
            D[u][v] += h[v] - h[u]

    return D, P


# ----------
a, b, c, d, e, f, g, h = range(8)

G = {
    a: {b: 2, c: 1, d: 3, e: 9, f: 4},
    b: {c: 4, e: 3},
    c: {d: 8},
    d: {e: 7},
    e: {f: 5},
    f: {c: 2, g: 2, h: 2},
    g: {f: 1, h: 6},
    h: {f: 9, g: 8}
}

print(G)

func1 = lambda x: x + 3

D, P = find_shortest_path_a_start(G=G, s=a, t=h, func=func1)

print(D)
print(P)


# ----------
print(P)

P.pop(a)

# weight for each edge in P
print([G[u][v] for (u, v) in P.items()])

# sum of the weight
print(sum([G[u][v] for (u, v) in P.items()]))





