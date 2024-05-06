# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

from heapq import heappush, heappop

from string import ascii_lowercase as chars


# ----------------------------------------------------------------------------
# word ladder
#  - A-star algorithm
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


class WordSpace:

    def variants(self, wd, words):
        wasl = list(wd)
        for i, c in enumerate(wasl):
            for oc in chars:
                if c == oc:
                    continue
                wasl[i] = oc
                ow = ''.join(wasl)
                if ow in words:
                    yield ow
            wasl[i] = c

    def __init__(self, words):
        self.words = words
        self.M = dict()

    def __getitem__(self, wd):
        if wd not in self.M:
            self.M[wd] = dict.fromkeys(self.variants(wd, self.words), 1)
        return self.M[wd]

    def heuristic(self, u, v):
        return sum(a != b for a, b in zip(u, v))

    def ladder(self, s, t, func=None):
        if func is None:
            def h(v):
                return self.heuristic(v, t)

        _, P = find_shortest_path_a_star(self, s, h, func)
        if P is None:
            return [s, None, t]
        u, p = t, []
        while u is not None:
            p.append(u)
            u = P[u]
        p.reverse()
        return p


