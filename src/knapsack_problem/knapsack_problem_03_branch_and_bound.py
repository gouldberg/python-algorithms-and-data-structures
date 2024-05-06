# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

from collections import deque

base_path = 'C:\\Users\\kouse\\Desktop\\python\\01_Python_algorithm_and_data_structure\\knapsack_problem'
import pandas as pd

import time
import os


# ----------------------------------------------------------------------------
# knapsack problem
#  - branch and bound method
# ----------------------------------------------------------------------------

class KnapsackProblem(object):
    """The definition of KnapSackProblem."""

    def __init__(self, name, capacity, items, costs, weights, zeros=set(), ones=set()):
        self.name = name
        self.capacity = capacity
        self.items = items
        self.costs = costs
        self.weights = weights
        # item NOT to be in knapsack
        self.zeros = zeros
        # item to be in knapsack
        self.ones = ones

        self.lb = -100
        self.ub = -100
        ratio = {j:costs[j] / weights[j] for j in items}
        self.sitemList = [k for k, v in sorted(ratio.items(), key=lambda x:x[1], reverse=True)]

        # solution which achieves lower bound and upper bound
        self.xlb = {j:0 for j in self.items}
        self.xub = {j:0 for j in self.items}

        # fractional solution achieving upper bound
        self.bi = None

    def getbounds(self):
        """Calculate the upper and lower bounds."""
        for j in self.zeros:
            self.xlb[j] = self.xub[j] = 0
        for j in self.ones:
            self.xlb[j] = self.xub[j] = 1
        if self.capacity < sum(self.weights[j] for j in self.ones):
            self.lb = self.ub = -100
            return 0
        ritems = self.items - self.zeros - self.ones
        sitems = [j for j in self.sitemList if j in ritems]
        cap = self.capacity - sum(self.weights[j] for j in self.ones)
        for j in sitems:
            if self.weights[j] <= cap:
                cap -= self.weights[j]
                self.xlb[j] = self.xub[j] = 1
            else:
                self.xub[j] = cap / self.weights[j]
                self.bi = j
                break
        self.lb = sum(self.costs[j] * self.xlb[j] for j in self.items)
        self.ub = sum(self.costs[j] * self.xub[j] for j in self.items)

    def __str__(self):
        return('Name = '+self.name+', capacity = '+str(self.capacity)+', \n'
               'items = '+str(self.items)+',\n'+
               'costs = '+str(self.costs)+',\n'+
               'weights = '+str(self.weights)+',\n'+
               'zeros = '+str(self.zeros)+', ones = '+str(self.ones)+',\n'+
               'lb = '+str(self.lb)+', ub = '+str(self.ub)+',\n'+
               'sitemList = '+str(self.sitemList)+',\n'+
               'xlb = '+str(self.xlb)+',\n'+'xub ='+str(self.xub)+',\n'+
               'bi = '+str(self.items)+',\n')


def KnapsackProblemSolve(capacity, items, costs, weights):
    from collections import deque
    queue = deque()

    root = KnapsackProblem('KP', capacity=capacity, items=items, costs=costs,
                           weights=weights, zeros=set(), ones=set())
    # print('--- root -------------------------------------')
    # print(f'upper: {root.ub: .2f} : {root.xub}')
    # print(f'lower: {root.lb: .2f} : {root.xlb}')
    # print(f'bi item: {root.bi}')

    root.getbounds()
    # print('--- root bound -------------------------------')
    # print(f'upper: {root.ub: .2f} : {root.xub}')
    # print(f'lower: {root.lb: .2f} : {root.xlb}')
    # print(f'bi item: {root.bi}')

    best = root
    queue.append(root)

    i = 0
    while queue != deque([]):
        i += 1
        p = queue.popleft()
        p.getbounds()
        # print(f'--- {i}: {p.name} -------------------------------------')
        # print(f'upper: {p.ub: .2f} : {p.xub}')
        # print(f'lower: {p.lb: .2f} : {p.xlb}')
        # print(f'upper {p.ub: .2f} : best lower {best.lb: .2f}')
        # print(f'bi item: {p.bi}')

        if p.ub > best.lb:
            if p.lb > best.lb:
                best = p
            if p.ub > p.lb:
                k = p.bi
                p1 = KnapsackProblem(p.name + '+' + str(k),
                                     capacity=p.capacity,
                                     items=p.items,
                                     costs=p.costs,
                                     weights=p.weights,
                                     zeros=p.zeros,
                                     ones=p.ones.union({k}))
                # print(p1)
                queue.append(p1)
                p2 = KnapsackProblem(p.name + '+' + str(k),
                                     capacity=p.capacity,
                                     items=p.items,
                                     costs=p.costs,
                                     weights=p.weights,
                                     zeros=p.zeros.union({k}),
                                     ones=p.ones)
                # print(p2)
                queue.append(p2)
    return 'Optimal', best.lb, best.xlb


# ----------
items = {1, 2, 3, 4, 5}
c = {1:50, 2:40, 3:10, 4:70, 5:55}
w = {1:7, 2:5, 3:1, 4:9, 5:6}
capacity = 15
res = KnapsackProblemSolve(capacity=capacity,
                           items=items,
                           costs=c,
                           weights=w)

print(res)
print('Optimal value = ', res[1])
print('Optimal solution = ', res[2])


# ----------
items = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
c = {1:65, 2:35, 3:245, 4:195, 5:65, 6:150, 7:275, 8:155, 9:120, 10:320, 11:75, 12:40, 13:200, 14:100, 15:220, 16:99}
w = {1:20, 2:8, 3:60, 4:55, 5:40, 6:70, 7:85, 8:25, 9:30, 10:65, 11:75, 12:10, 13:95, 14:50, 15:40, 16:10}
capacity = 250

res = KnapsackProblemSolve(capacity=capacity,
                           items=items,
                           costs=c,
                           weights=w)

print(res)
print('Optimal value = ', res[1])
print('Optimal solution = ', res[2])


# ----------
dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
c = {i:dat.value[i] for i in range(len(dat))}
w = {i:dat.weight[i] for i in range(len(dat))}
capacity = 40000

st11 = time.time()
result11 = KnapsackProblemSolve(capacity=capacity,
                           items=items,
                           costs=c,
                           weights=w)
ed11 = time.time()
print('Optimal value = ', result11[1])
print('Optimal solution = ', result11[2])
print(f'takes: {ed11 - st11: .4f} sec')


# ----------------------------------------------------------------------------
# knapsack problem
#  - branch and bound method  --> VERY SLOW !!!
# ----------------------------------------------------------------------------

from heapq import heappush, heappop
from itertools import count

def bb_knapsack(w, v, c):
    sol = 0
    n = len(w)

    idxs = list(range(n))
    idxs.sort(key=lambda i: v[i]/w[i], reverse=True)

    def bound(sw, sv, m):
        if m == n: return sv
        objs = ((v[i], w[i]) for i in idxs[m:])
        for av, aw in objs:
            if sw + aw > c: break
            sw += aw
            sv += av
        return sv + (av / aw) * (c - sw)

    def node(sw, sv, m):
        nonlocal sol
        if sw > c: return
        sol = max(sol, sv)
        if m == n: return
        i = idxs[m]
        ch = [(sw, sv), (sw + w[i], sv + v[i])]
        for sw, sv in ch:
            b = bound(sw, sv, m+1)
            if b > sol:
                yield b, node(sw, sv, m+1)

    num = count()
    Q = [(0, next(num), node(0, 0, 0))]
    while Q:
        _, _, r = heappop(Q)
        for b, u in r:
            heappush(Q, (b, next(num), u))

    return sol


# ----------
v = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]
w = [20, 8, 60, 55, 40, 70, 85, 25, 30, 65, 75, 10, 95, 50, 40, 10]
capacity = 250
n = len(c)
print(bb_knapsack(w=w, v=v, c=capacity))


# ----------
dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
v = [dat.value[i] for i in range(len(dat))]
w = [dat.weight[i] for i in range(len(dat))]
n = len(v)
capacity = 40000

st12 = time.time()
result12 = bb_knapsack(w=w, v=v, c=capacity)
ed12 = time.time()
print('solution', result12[1])
print(f'takes: {ed12 - st12: .4f} sec')


# ----------------------------------------------------------------------------
# knapsack problem:  compare
# ----------------------------------------------------------------------------

print(f'result: {result1}')
print(f'takes: {ed1 - st1: .4f} sec')

print(f'result: {result2}')
print(f'takes: {ed2 - st2: .4f} sec')

print(f'result: {result3}')
print(f'takes: {ed3 - st3: .4f} sec')

print(f'result: {result11[1]}')
print(f'takes: {ed11 - st11: .4f} sec')

print(f'result: {result12}')
print(f'takes: {ed12 - st12: .4f} sec')


