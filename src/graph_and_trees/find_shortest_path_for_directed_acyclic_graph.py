# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# find shortest path for directed acyclic graph
#  - recursion with memoization
# ----------------------------------------------------------------------------

# This solution does not require topological sort.
# Perform depth-first search (DFS) implicitly and update following topological sort order automatically

from functools import lru_cache

def rec_dag_sp(W, s, t):
    @lru_cache
    def d(u):
        if u == t:  return 0
        return min(W[u][v] + d(v) for v in W[u])
    return d(s)


# ----------
a, b, c, d, e, f = range(6)

G = {
    a: {b: 2, f: 9},
    b: {c: 1, d: 2, f: 6},
    c: {d: 7},
    d: {e: 2, f: 3},
    e: {f: 4},
    f: {}
}

print(G)

# a -> b -> d -> f: 7 = 2 + 2 + 3
print(rec_dag_sp(W=G, s=a, t=f))


# ----------------------------------------------------------------------------
# find shortest path for directed acyclic graph
#  - iteration
# ----------------------------------------------------------------------------

def topsort(G):

    count = dict((u, 0) for u in G)

    for u in G:
        for v in G[u]:
            count[v] += 1

    Q = [u for u in G if count[u] == 0]
    S = []
    while Q:
        u = Q.pop()
        S.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                Q.append(v)

    return S


def dag_sp(W, s, t):
    d = {u:float('inf') for u in W}
    d[s] = 0

    # order by topological sort
    for u in topsort(W):
        if u == t:  break
        for v in W[u]:
            d[v] = min(d[v], d[u] + W[u][v])

    return d[t]


# ----------
a, b, c, d, e, f = range(6)

G = {
    a: {b: 2, f: 9},
    b: {c: 1, d: 2, f: 6},
    c: {d: 7},
    d: {e: 2, f: 3},
    e: {f: 4},
    f: {}
}

print(G)


# ----------
print(topsort(G))


# a -> b -> d -> f: 7 = 2 + 2 + 3
print(dag_sp(W=G, s=a, t=f))

