# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import collections
import operator

base_path = 'C:\\Users\\kouse\\Desktop\\python\\01_Python_algorithm_and_data_structure\\knapsack_problem'
import pandas as pd

import time
import os


# ----------------------------------------------------------------------------
# knapsack problem
#  - dynamic programming
# ----------------------------------------------------------------------------

def optimum_subject_to_capacity(items, capacity):

    # Returns the optimum value when we choose from items[:k+1] and have a capacity of available_capacity
    def optimum_subject_to_item_and_capacity(k, available_capacity):
        if k < 0:
            # No items can be chosen
            return 0

        if V[k][available_capacity] == -1:
            without_curr_item = optimum_subject_to_item_and_capacity(k - 1, available_capacity)
            with_curr_item = (0 if available_capacity < items[k].weight else(
                items[k].value + optimum_subject_to_item_and_capacity(k - 1, available_capacity - items[k].weight)))

            V[k][available_capacity] = max(without_curr_item, with_curr_item)

        return V[k][available_capacity]

    # V[i][j] holds the optimum value when we choose from items[:i+1] and have a capacity of j
    V = [[-1] * (capacity + 1) for _ in items]
    return optimum_subject_to_item_and_capacity(len(items) - 1, capacity)

# ----------
Item = collections.namedtuple('Item', ('weight', 'value'))

items1 = [Item(w, v) for w, v in
         [(20, 65), (8, 35), (60, 245), (55, 195), (40, 65), (70, 150), (85, 275),
         (25, 155), (30, 120), (65, 320), (75, 75), (10, 40), (95, 200), (50, 100),
         (40, 220), (10, 99)]]

capacity1 = 250


items2 = [Item(w, v) for w, v in
         [(5, 60), (3, 50), (4, 70), (2, 30)]]

capacity2 = 5

print(items2)


# ----------
print(optimum_subject_to_capacity(items=items1, capacity=capacity1))

print(optimum_subject_to_capacity(items=items2, capacity=capacity2))


# ----------------------------------------------------------------------------
# knapsack problem
#  - dynamic programming
#  - time complexity:  O(N * W) where ‘N’ is the number of weight element and ‘W’ is capacity
#  - space complexity: O(N * W), the use of 2D array N * W
# ----------------------------------------------------------------------------

def knapSack1(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


# ----------
c = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]
w = [20, 8, 60, 55, 40, 70, 85, 25, 30, 65, 75, 10, 95, 50, 40, 10]
capacity = 250
n = len(c)
print(knapSack1(W=capacity, wt=w, val=c, n=n))


# ----------
dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
c = [dat.value[i] for i in range(len(dat))]
w = [dat.weight[i] for i in range(len(dat))]
n = len(c)
capacity = 40000

st1 = time.time()
result1 = knapSack1(W=capacity, wt=w, val=c, n=n)
ed1 = time.time()
print(f'result: {result1}')
print(f'takes: {ed1 - st1: .4f} sec')


# ----------
# weight * 1/10
dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
c = [dat.value[i] for i in range(len(dat))]
w = [int(dat.weight[i]/10) for i in range(len(dat))]
n = len(c)
capacity = int(40000/10)

st1_2 = time.time()
result1_2 = knapSack1(W=capacity, wt=w, val=c, n=n)
ed1_2 = time.time()
print(f'result: {result1_2}')
print(f'takes: {ed1_2 - st1_2: .4f} sec')


# ----------------------------------------------------------------------------
# knapsack problem
#  - dynamic programming with memoization technique
#  - time complexity:  O(N * W) where ‘N’ is the number of weight element and ‘W’ is capacity
#  - space complexity: O(N * W), the use of 2D array N * W
# ----------------------------------------------------------------------------

def knapSack2(wt, val, W, n):
    # base conditions
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # choice diagram code
    if wt[n - 1] <= W:
        t[n][W] = max(
            val[n - 1] + knapSack2(
                wt, val, W - wt[n - 1], n - 1),
            knapSack2(wt, val, W, n - 1))
        return t[n][W]
    elif wt[n - 1] > W:
        t[n][W] = knapSack2(wt, val, W, n - 1)
        return t[n][W]


# ----------
c = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]
w = [20, 8, 60, 55, 40, 70, 85, 25, 30, 65, 75, 10, 95, 50, 40, 10]
capacity = 250
n = len(c)
# We initialize the matrix with -1 at first
t = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]
print(t)
print(knapSack2(wt=w, val=c, W=capacity, n=n))


# ----------
dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
c = [dat.value[i] for i in range(len(dat))]
w = [dat.weight[i] for i in range(len(dat))]
n = len(c)
capacity = 40000
t = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]

st2 = time.time()
result2 = knapSack2(W=capacity, wt=w, val=c, n=n)
ed2 = time.time()
print(f'result: {result2}')
print(f'takes: {ed2 - st2: .4f} sec')


# ----------
# weight * 1/10
dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
c = [dat.value[i] for i in range(len(dat))]
w = [int(dat.weight[i]/10) for i in range(len(dat))]
n = len(c)
capacity = int(40000/10)
t = [[-1 for i in range(capacity + 1)] for j in range(n + 1)]

st2_2 = time.time()
result2_2 = knapSack2(W=capacity, wt=w, val=c, n=n)
ed2_2 = time.time()
print(f'result: {result2_2}')
print(f'takes: {ed2_2 - st2_2: .4f} sec')


# ----------------------------------------------------------------------------
# knapsack problem
#  - dynamic programming
#  - time complexity:  O(N * W) where ‘N’ is the number of weight element and ‘W’ is capacity
#  - space complexity: O(W) !!!
# ----------------------------------------------------------------------------

def knapSack3(W, wt, val, n):
    dp = [0 for i in range(W + 1)]  # Making the dp array

    for i in range(1, n + 1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
            # previous computation when taking i-1 items
            if wt[i - 1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])

    return dp[W]  # returning the maximum value of knapsack


# ----------
c = [65, 35, 245, 195, 65, 150, 275, 155, 120, 320, 75, 40, 200, 100, 220, 99]
w = [20, 8, 60, 55, 40, 70, 85, 25, 30, 65, 75, 10, 95, 50, 40, 10]
capacity = 250
n = len(c)
print(knapSack3(W=capacity, wt=w, val=c, n=n))


# ----------
dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
c = [dat.value[i] for i in range(len(dat))]
w = [dat.weight[i] for i in range(len(dat))]
n = len(c)
capacity = 40000

st3 = time.time()
result3 = knapSack3(W=capacity, wt=w, val=c, n=n)
ed3 = time.time()
print(f'result: {result3}')
print(f'takes: {ed3 - st3: .4f} sec')


# ----------
# weight * 1/10
dat = pd.read_csv(os.path.join(base_path, 'knapsack_problem_data.txt'), sep='\t')
items = set(range(len(dat)))
c = [dat.value[i] for i in range(len(dat))]
w = [int(dat.weight[i]/10) for i in range(len(dat))]
n = len(c)
capacity = int(40000/10)

st3_2 = time.time()
result3_2 = knapSack3(W=capacity, wt=w, val=c, n=n)
ed3_2 = time.time()
print(f'result: {result3_2}')
print(f'takes: {ed3_2 - st3_2: .4f} sec')


# ----------------------------------------------------------------------------
# knapsack problem:  compare
# ----------------------------------------------------------------------------

print(f'result: {result1}')
print(f'takes: {ed1 - st1: .4f} sec')

print(f'result: {result1_2}')
print(f'takes: {ed1_2 - st1_2: .4f} sec')

print(f'result: {result2}')
print(f'takes: {ed2 - st2: .4f} sec')

print(f'result: {result2_2}')
print(f'takes: {ed2_2 - st2_2: .4f} sec')

print(f'result: {result3}')
print(f'takes: {ed3 - st3: .4f} sec')

print(f'result: {result3_2}')
print(f'takes: {ed3_2 - st3_2: .4f} sec')

