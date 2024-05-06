# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# compute binomial coefficient (Pascal triangle)
#  - dynamic programming
# ----------------------------------------------------------------------------

def compute_binomial_coefficient(n, k):
    def compute_x_choose_y(x, y):
        if y in (0, x):
            return 1

        if x_choose_y[x][y] == 0:
            without_y = compute_x_choose_y(x - 1, y)
            with_y = compute_x_choose_y(x - 1, y - 1)
            x_choose_y[x][y] = without_y + with_y
        return x_choose_y[x][y]

    x_choose_y = [[0] * (k + 1) for _ in range(n + 1)]

    return compute_x_choose_y(n, k)


# ----------
print(compute_binomial_coefficient(10, 7))


# ----------------------------------------------------------------------------
# compute binomial coefficient
#  - Pascal triangle, iteration
# ----------------------------------------------------------------------------

from collections import defaultdict

def compute_binomial_coefficient2(n, k):

    C = defaultdict(int)

    for row in range(n + 1):
        C[row, 0] = 1
        for col in range(1, k + 1):
            C[row, col] = C[row - 1, col - 1] + C[row - 1, col]

    return C


# ----------
C = compute_binomial_coefficient2(10, 7)

print(C)

print(C[10, 7])


# ----------------------------------------------------------------------------
# compute binomial coefficient
#  - Pascal triangle, recursion
# ----------------------------------------------------------------------------

# memoize decorator
from functools import wraps
from functools import lru_cache

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap

@lru_cache()
# @memo
def C3(n, k):
    if k == 0:  return 1
    if n == 0:  return 0
    return C3(n -1 , k - 1) + C3(n - 1, k)

# ----------
print(C3(10, 7))







