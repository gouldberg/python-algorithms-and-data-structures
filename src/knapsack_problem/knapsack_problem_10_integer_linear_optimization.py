# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

from pulp import *

base_path = 'C:\\Users\\kouse\\Desktop\\python\\01_Python_algorithm_and_data_structure\\knapsack_problem'
import pandas as pd

import time
import os


# ----------------------------------------------------------------------------
# knapsack problem
#  - integer linear optimization by PuLP
# ----------------------------------------------------------------------------

items = {1, 2, 3, 4, 5}
c = {1:50, 2:40, 3:10, 4:70, 5:55}
w = {1:7, 2:5, 3:1, 4:9, 5:6}
capacity = 15


# ----------
items = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
c = {1:65, 2:35, 3:245, 4:195, 5:65, 6:150, 7:275, 8:155, 9:120, 10:320, 11:75, 12:40, 13:200, 14:100, 15:220, 16:99}
w = {1:20, 2:8, 3:60, 4:55, 5:40, 6:70, 7:85, 8:25, 9:30, 10:65, 11:75, 12:10, 13:95, 14:50, 15:40, 16:10}
capacity = 250


# ----------
dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
c = {i:dat.value[i] for i in range(len(dat))}
w = {i:dat.weight[i] for i in range(len(dat))}
capacity = 40000


# ----------
kp = LpProblem('0-1_Knapsack_problem', LpMaximize)

x = LpVariable.dicts('x', list(items), None, None, LpBinary)

kp += lpSum([c[i] * x[i] for i in items])

kp += lpSum([w[i] * x[i] for i in items]) <= capacity

st20 = time.time()
status = kp.solve()
print('status: ', LpStatus[status])
ed20 = time.time()

print('optimal solution:')
for i in items:
    print(x[i].name, x[i].value())

print(f'result: {sum(x[i].value() * c[i] for i in items)}')
print(f'takes: {ed20 - st20: .4f} sec')

