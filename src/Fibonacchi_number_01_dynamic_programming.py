# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Fibonacchi number
#  - dynamic programming
#  - time complexity: O(n)
#  - space complexity: O(1)
# ----------------------------------------------------------------------------

def fibonacchi(n):

    if n <= 1: return n

    f_minus_2, f_minus_1 = 0, 1

    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f

    return f_minus_1


# ----------
print(fibonacchi(n=10))


# ----------------------------------------------------------------------------
# Fibonacchi number
#  - dynamic programming with memoization
# ----------------------------------------------------------------------------

# memoize decorator
from functools import wraps

def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap

@memo
def fib(n):
    if n < 2: return 1
    return fib(n-1) + fib(n-2)



# ----------
# fib = memo(fib)

print(fib(100))


# ----------------------------------------------------------------------------
# Fibonacchi number
#  - dynamic programming with memoization by functools.lru_cache
# ----------------------------------------------------------------------------

import functools

@functools.lru_cache()
def fib(n):
    if n < 2: return 1
    return fib(n-1) + fib(n-2)


# ----------
print(fib(100))


# ----------------------------------------------------------------------------
# Fibonacchi number
#  - one liner
# ----------------------------------------------------------------------------

from functools import reduce

fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n - 2), [0, 1])

n = 100


# ----------
# series
print(fibs)

# total
print(np.array(fibs).sum())


