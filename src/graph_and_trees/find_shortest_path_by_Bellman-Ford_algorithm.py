# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# find shortest path by Bellman-Ford algorithm
#  - applicable for the DAG with only single source
#  - time complexity: O(n)  (n: number of nodes)
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

D, P = find_shortest_path_bellman_ford(G=G, s=a)

print(D)
print(P)


# ----------
G[a][b] = 3
G[a][c] = 7
G[c][d] = -4

print(G)

D, P = find_shortest_path_bellman_ford(G=G, s=a)
print(D)
print(P)


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

G[g][h] = -9

print(G)

D, P = find_shortest_path_bellman_ford(G=G, s=a)
print(D)
print(P)


