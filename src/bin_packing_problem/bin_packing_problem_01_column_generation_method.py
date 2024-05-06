# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

from pulp import *
import numpy as np

import time


# ----------------------------------------------------------------------------
# bin packing problem
#  - columns generation method
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


# KnapSack Problem solving by PuLP (0-1 integer linear programmin)
def KPS(capacity, items, costs, weights):
    knapsack = LpProblem(name='knapsack', sense=LpMaximize)
    x = {j: LpVariable('x'+str(j), lowBound=0, cat='Binary') for j in items}

    knapsack += lpSum(costs[j] * x[j] for j in items)
    knapsack += lpSum(weights[j] * x[j] for j in items) <= capacity, 'weights'

    knapsack.solve()
    xx = {j: int(x[j].varValue) for j in items}
    return LpStatus[knapsack.status], value(knapsack.objective), xx


def binpacking(capacity, w):

    m = len(w)
    items = set(range(m))
    A = np.identity(m)

    solved = False
    columns = 0
    dual = LpProblem(name='D(K)', sense=LpMaximize)
    y = [LpVariable('y'+str(i), lowBound=0) for i in items]

    # objective function
    dual += lpSum(y[i] for i in items)
    for j in range(len(A.T)):
        dual += lpDot(A.T[j], y) <= 1, 'ineq'+str(j)

    while not(solved):
        # dual
        dual.solve()

        costs = {i: y[i].varValue for i in items}
        weights = {i: w[i] for i in items}

        # Branch-and-Bound
        # (state, val, sol) = KnapsackProblemSolve(capacity, items, costs, weights)

        # PuLP is faster
        (state, val, sol) = KPS(capacity, items, costs, weights)

        if val >= 1.0 + MEPS:
            a = np.array([int(sol[i]) for i in items])
            dual += lpDot(a, y) <= 1, 'ineq'+str(m + columns)
            A = np.hstack((A, a.reshape((-1, 1))))
            columns += 1
        else:
            solved = True

    print('Generated columns: ', columns)

    m, n = A.shape
    primal = LpProblem(name='P(K)', sense=LpMinimize)
    x = [LpVariable('x'+str(j), lowBound=0, cat='Binary') for j in range(n)]

    # objective function
    primal += lpSum(x[j] for j in range(n))
    for i in range(m):
        primal += lpDot(A[i], x) >= 1, 'ineq'+str(i)

    primal.solve()
    if value(primal.objective) - value(dual.objective) < 1.0 - MEPS:
        print('Optimal solution found: ')
    else:
        print('Approximated solution found: ')

    K = [j for j in range(n) if x[j].varValue > MEPS]
    result = []
    itms = set(range(m))
    for j in K:
        J = {i for i in range(m) if A[i, j] > MEPS and i in itms}
        r = [w[i] for i in J]
        itms -= J
        result.append(r)

    print(result)


# ----------
MEPS = 1.0e-8

capacity = 125

items = set(range(100))

np.random.seed(1234)
w = {i:np.random.randint(3,42) for i in items}
w2 = [w[i] for i in items]

print(w2)

st1 = time.time()
binpacking(capacity, w)
ed1 = time.time()

print(f'takes {ed1 - st1: .2f} sec')


# ----------------------------------------------------------------------------
# bin packing problem
#  - columns generation method
#  - other formulation:  --> THIS IS FASTER
# ----------------------------------------------------------------------------

def binpacking2(capacity, w):
    n = len(w)
    items = range(n)
    bpprob = LpProblem(name='BinPacking2', sense=LpMinimize)
    z = [LpVariable('z_'+str(j), lowBound=0, cat='Binary') for j in items]
    x = [[LpVariable('x_'+str(i)+'_'+str(j), lowBound=0, cat='Binary') for j in items] for i in items]

    bpprob += lpSum(z[i] for i in items)
    for i in items:
        bpprob += lpSum(x[i][j] for j in items) == 1
    for j in items:
        bpprob += lpSum(x[i][j] * w[i] for i in items) <= capacity * z[j]

    bpprob.solve()
    result = []
    for j in items:
        if z[j].varValue > MEPS:
            r = [w[i] for i in items if x[i][j].varValue > MEPS]
            result.append(r)
    print(result)


# ----------
MEPS = 1.0e-8

capacity = 125

items = set(range(200))

np.random.seed(1234)
w = {i:np.random.randint(3,42) for i in items}
w2 = [w[i] for i in items]

print(w2)

st2 = time.time()
binpacking2(capacity, w)
ed2 = time.time()

print(f'takes {ed2 - st2: .2f} sec')


