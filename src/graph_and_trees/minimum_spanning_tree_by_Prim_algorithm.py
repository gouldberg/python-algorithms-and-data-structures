# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# minimum spanning tree
#  - Prim algorithm
# ----------------------------------------------------------------------------

from heapq import heappop, heappush

def prim(G, s):
    P, Q = {}, [(0, None, s)]
    while Q:
        _, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        for v, w in G[u].items():
            heappush(Q, (w, u, v))

    return P


# ----------
a, b, c, d, e, f, g, h = range(8)

G = {
    a: {d: 5, f: 6, h: 3},
    b: {d: 8, e: 4, g: 3},
    c: {e: 9, f: 10, h: 5},
    d: {a: 5, b: 8, h: 6},
    e: {b: 4, c: 9, g: 2},
    f: {a: 6, c: 10},
    g: {b: 3, e: 2, h: 7},
    h: {a: 3, c: 5, d: 6, g: 7}
}

print(G)


# ----------
# minimum spanning tree
# start node: s
T = prim(G=G, s=b)

print(T)

T.pop(1)

# weight for each edge in T
print([G[u][v] for (u, v) in T.items()])

# sum of the weight
print(sum([G[u][v] for (u, v) in T.items()]))


