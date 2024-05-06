# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# traverse components
# ----------------------------------------------------------------------------

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


# ----------
# search components
def components(G):

    comp = []
    seen = set()

    for u in G:
        if u in seen: continue
        C = walk(G, u)
        seen.update(C)
        comp.append(C)

    return comp


# ----------
# depth-first search by recursion
def rec_dfs(G, s, S=None):

    if S is None:  S = set()
    S.add(s)
    for u in G[s]:
        if u in S:  continue
        rec_dfs(G, u, S)

    return S


# ----------
# depth-first search by iteration
def iter_dfs(G, s):

    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S:  continue
        S.add(u)
        Q.extend(G[u])
        yield u


# ----------
# traverse
def traverse(G, s, qtype=set):

    S, Q = set(), qtype()
    Q.add(s)
    while Q:
        u = Q.pop()
        if u in S:  continue
        S.add(u)
        for v in G[u]:
            Q.add(v)
        yield u


# ----------
# depth-first search
def dfs(G, s, d, f, S=None, t=0):

    if S is None:  S = set()
    d[s] = t;  t += 1
    S.add(s)
    for u in G[s]:
        if u in S:  continue
        t = dfs(G, u, d, f, S, t)
    f[s] = t;  t += 1
    return t


# ----------
# iterative deepening depth-first search
def iddfs(G, s):

    yielded = set()
    def recurse(G, s, d, S=None):
        if s not in yielded:
            yielded s
            yielded.add(s)
        if d == 0:  return
        if S is None:  S = set()
        S.add(s)
        for u in G[s]:
            if u in S:  continue
            for v in recurse(G, u, d-1, S):
                yield v
    n = len(G)
    for d in range(n):
        if len(yielded) == n:  break
        for u in recurse(G, s, d):
            yield u


# ----------
# breadth-first search
def bfs(G, s):

    P, Q = {s: None}, deque([s])
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P:  continue
            P[v] = Q.append(v)

    return P


