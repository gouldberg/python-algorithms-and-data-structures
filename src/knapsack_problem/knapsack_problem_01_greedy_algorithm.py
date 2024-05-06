# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

base_path = 'C:\\Users\\kouse\\Desktop\\python\\01_Python_algorithm_and_data_structure\\knapsack_problem'
import pandas as pd
import os

dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
c = {i:dat.value[i] for i in range(len(dat))}
w = {i:dat.weight[i] for i in range(len(dat))}
capacity = 40000


# ----------------------------------------------------------------------------
# knapsack problem
#  - greedy algorithm
#  - approximate solution by greedy algorithm provides lower bound of optimal values
# ----------------------------------------------------------------------------

items = {1, 2, 3, 4, 5}
c = {1:50, 2:40, 3:10, 4:70, 5:55}
w = {1:7, 2:5, 3:1, 4:9, 5:6}
capacity = 15


items = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
c = {1:65, 2:35, 3:245, 4:195, 5:65, 6:150, 7:275, 8:155, 9:120, 10:320, 11:75, 12:40, 13:200, 14:100, 15:220, 16:99}
w = {1:20, 2:8, 3:60, 4:55, 5:40, 6:70, 7:85, 8:25, 9:30, 10:65, 11:75, 12:10, 13:95, 14:50, 15:40, 16:10}
capacity = 250


# ----------
ratio = {j:c[j]/w[j] for j in items}

sItems = [key for key, val in sorted(ratio.items(), key=lambda x:x[1], reverse=True)]

for j in sItems:
    print('c[%d]/w[%d] = %1f' % (j, j, c[j]/w[j]))


# ----------
x = {j:0 for j in sItems}

cap = capacity

for j in sItems:
    if w[j] <= cap:
        cap -= w[j]
        x[j] = 1

print(x)
print(sum(c[j] * x[j] for j in sItems))


# -->
# approximate solution (lower bound) is 105 (item 3, 5, 2)


# ----------------------------------------------------------------------------
# knapsack problem
#  - greedy algorithm with linear relaxation
#  - this provides upper bound of optimal value
# ----------------------------------------------------------------------------

x = {j:0 for j in sItems}

cap = capacity

for j in sItems:
    if w[j] <= cap:
        cap -= w[j]
        x[j] = 1
    else:
        x[j] = cap / w[j]
        break

print(x)
print(sum(c[j] * x[j] for j in sItems))


# -->
# upper bound is 128.3 (item 3, 5, 2, and 1/3 of 4)

