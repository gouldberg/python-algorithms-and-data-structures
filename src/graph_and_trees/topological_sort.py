# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# topological sort
#  - naive approach
#  - time complexity: O(n^2)
# ----------------------------------------------------------------------------

def naive_topsort(G, S=None):

    # default: all nodes
    if S is None:
        S = set(G)

    # base case
    if len(S) == 1:
        return list(S)

    v = S.pop()
    seq = naive_topsort(G, S)
    min_i = 0

    for i, u in enumerate(seq):
        if v in G[u]:
            min_i = i + 1

    seq.insert(min_i, v)

    return seq


# ----------
# DAG (directed acyclic graph)
G = {'a': set('bf'), 'b': set('cdf'),
     'c': set('d'), 'd': set('ef'), 'e': set('f'), 'f': set()}

print(G)


# ----------
naive_topsort(G=G, S=None)


# ----------------------------------------------------------------------------
# topological sort
#  - time complexity: O(n)
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


# ----------
# DAG (directed acyclic graph)
G = {'a': set('bf'), 'b': set('cdf'),
     'c': set('d'), 'd': set('ef'), 'e': set('f'), 'f': set()}

print(G)


# ----------
topsort(G=G)


# ----------------------------------------------------------------------------
# topological sort
#  - depth-first search
# ----------------------------------------------------------------------------

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
# DAG (directed acyclic graph)
G = {'a': set('bf'), 'b': set('cdf'),
     'c': set('d'), 'd': set('ef'), 'e': set('f'), 'f': set()}

print(G)


# ----------
topsort(G=G)

