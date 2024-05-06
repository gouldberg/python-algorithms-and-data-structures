# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

from pyomo.environ import *
from pulp import *


# ----------------------------------------------------------------------------
# knapsack problem
#  -
# ----------------------------------------------------------------------------

c = {1:50, 2:40, 3:10, 4:70, 5:55}

w = {1:7, 2:5, 3:1, 4:9, 5:6}

items = list(c.keys())

capacity = 15


# ----------
c = {1:65, 2:35, 3:245, 4:195, 5:65, 6:150, 7:275, 8:155, 9:120, 10:320, 11:75, 12:40, 13:200, 14:100, 15:220, 16:99}

w = {1:20, 2:8, 3:60, 4:55, 5:40, 6:70, 7:85, 8:25, 9:30, 10:65, 11:75, 12:10, 13:95, 14:50, 15:40, 16:10}

items = list(c.keys())

capacity = 250


# ----------
kp = ConcreteModel()

kp.x = Var(items, within=NonNegativeReals, bounds=(0, 1))

kp.obj = Objective(expr=sum(c[i] * kp.x[i] for i in items), sense=maximize)

kp.con = Constraint(expr=sum(w[i] * kp.x[i] for i in items) <= capacity)

solver = SolverFactory('cbc')
print(solver.options)

result = solver.solve(kp)

print(result['Solver'])

print('optimal value:', value(kp.obj))

print('optimal solution:')

for i in kp.x:
    print(kp.x[i], kp.x[i]())

