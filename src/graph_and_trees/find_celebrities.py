# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# find celebrities
#  - brute-force approach
#  - time complexity: O(n^2)
# ----------------------------------------------------------------------------

def naive_find_celebrities(G):

    n = len(G)

    for u in range(n):
        for v in range(n):
            if u == v:
                continue
            if G[u][v]:
                break

        else:
            return u

    return None


# ----------
n = 100
G = [[randrange(2) for _ in range(n)] for _ in range(n)]
c = randrange(n)
c = 57
for i in range(n):
    G[i][c] = True
    G[c][i] = False

print(G)

print(naive_find_celebrities(G))


# ----------------------------------------------------------------------------
# find celebrities
#  - time complexity: O(n)
# ----------------------------------------------------------------------------

def find_celebrities(G):

    n = len(G)

    u, v = 0, 1

    for c in range(2, n+1):
        if G[u][v]: u = c
        else: v = c

    if u == n: c = v
    else: c = u

    for v in range(n):
        if c == v: continue
        if G[c][v]: break
        if not G[v][c]: break
        else: return c

    return None


# ----------
print(G)

print(find_celebrities(G))

