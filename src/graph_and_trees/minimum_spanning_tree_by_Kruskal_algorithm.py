# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# minimum spanning tree
#  - Kruskal algorithm, naive approach
# ----------------------------------------------------------------------------

def naive_find(C, u):
    while C[u] != u:
        u = C[u]
    return u


def naive_union(C, u, v):
    u = naive_find(C, u)
    v = naive_find(C, v)
    C[u] = v


def naive_kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C = {u: u for u in G}
    for _, u, v in sorted(E):
        if naive_find(C, u) != naive_find(C, v):
            T.add((u, v))
            naive_union(C, u, v)

    return T


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
E = sorted([(G[u][v], u, v) for u in G for v in G[u]])
C = {u: u for u in G}

_, u, v = E[0]
print((u, v))
print(naive_find(C, u))
print(naive_find(C, v))
naive_union(C, u, v)

# C[u] == v
print(C[u])


# ----------
# minimum spanning tree
T = naive_kruskal(G)

print(T)

# weight for each edge in T
print([G[u][v] for (u, v) in list(T)])

# sum of the weight
print(sum([G[u][v] for (u, v) in list(T)]))


# ----------------------------------------------------------------------------
# minimum spanning tree
#  - Kruskal algorithm
#  - time complexity:  O(m * log(n))
# ----------------------------------------------------------------------------

def find(C, u):
    if C[u] != u:
        # path compression
        C[u] = find(C, C[u])
    return C[u]


def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:
        R[v] += 1


def kruskal(G):
    E = [(G[u][v], u, v) for u in G for v in G[u]]
    T = set()
    C, R = {u: u for u in G}, {u: 0 for u in G}
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)

    return T


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
T = kruskal(G)

print(T)

# weight for each edge in T
print([G[u][v] for (u, v) in list(T)])

# sum of the weight
print(sum([G[u][v] for (u, v) in list(T)]))

