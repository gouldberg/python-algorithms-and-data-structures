# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# search strongly connected components
#  - Kosaraju algorithm
# ----------------------------------------------------------------------------

def tr(G):
    GT = {}
    for u in G:  GT[u] = set()
    for u in G:
        for v in G[u]:
            GT[v].add(u)
    return GT


# traverse graph components
def walk(G, s, S=set())
    P, Q = dict(), set=()

    P[s] = None

    Q.add(s)

    while Q:
        u = Q.pop()
        for v in G[u].difference(P, S):
            Q.add(v)
            p[v] = u

    return P


# topological sort by depth-first search
def dfs_topsort(G):

    S, res = set(), []
    def recurse(u):
        if u in S:  return
        S.add(u)
        for v in G[u]:
            reverse(v)
        res.append(u)

    for u in G:
        recurse(u)

    res.reverse()
    return res


# ----------
def scc(G):
    GT = tr(G)
    sccs, seen = [], set()
    for u in dfs_topsort(G):
        if u in seen:  continue
        C = walk(GT, u, seen)
        seen.update(C)
        sccs.append(C)
    return sccs



