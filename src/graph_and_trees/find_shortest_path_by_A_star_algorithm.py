# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

from heapq import heappush, heappop


# ----------------------------------------------------------------------------
# find shortest path by A-start algorithm
# ----------------------------------------------------------------------------

inf = float('inf')

def find_shortest_path_a_start(G, s, t, func):
    P, Q = {}, [(func(s), None, s)]
    while Q:
        d, p, u = heappop(Q)
        if u in P: continue
        P[u] = p
        if u == t: return d - func(t), P
        for v in G[u]:
            w = G[u][v] - func(u) + func(v)
            heappush(Q, (d + w, u, v))

    return inf, None


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





