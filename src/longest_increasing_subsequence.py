# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


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


# ----------
seq1 = [0,1,2,3,-2,5,-3,4,-20,6,-5,12,-20,-23,-3,2,3,4,5,9,6,-20,-5]

seq2 = [904, 40, 523, 12, -335, -385, -124, 481, -31]

seq3 = [1,3,7,2,5,10,2,3,4,2]

seq4 = [1,3,7,2,5,8]

seq5 = [0, 8, 4, 12 ,2, 10, 6, 14, 1, 9]


# ----------------------------------------------------------------------------
# Longest Increasing (non-Decreasing) Subsequence (LIS):  brute-force approach
# ----------------------------------------------------------------------------

from itertools import combinations

def naive_lis(seq):
    for length in range(len(seq), 0, -1):
        for sub in combinations(seq, length):

            print(f'sub: {sub}  len: {length}')
            if list(sub) == sorted(sub):
                return sub


# ----------
# combinations
a = [1,2,3,4]
print(list(combinations(a,2)))


# ----------
print(naive_lis(seq3))


# ----------------------------------------------------------------------------
# Longest Increasing (non-Decreasing) Subsequence (LIS):  recursive solution
# ----------------------------------------------------------------------------

def rec_lis(seq):

    val_trav = []

    @memo
    def L(cur):
        res = 1
        val = [seq[cur]]
        for pre in range(cur):
            if seq[pre] <= seq[cur]:
                val.extend([seq[pre]])
                res = max(res, 1 + L(pre))

        val_trav.append(val)
        return res

    return list(L(i) for i in range(len(seq))), val_trav


# ----------
seq = seq4

print(seq)

lis_length_list, val_trav = rec_lis(seq)
print(lis_length_list)
print(val_trav)

# this is the length of LIS
lis_length = sorted(lis_length_list)[-1]
print(lis_length)

idx = np.argmax(np.array(lis_length_list))


# ----------------------------------------------------------------------------
# Longest Increasing (non-Decreasing) Subsequence (LIS):  iterative approach
# this takes O(n^2) time and O(n) space complexity
# ----------------------------------------------------------------------------

def basic_lis(seq):

    L = [1] * len(seq)

    for cur, val in enumerate(seq):
        for pre in range(cur):
            if seq[pre] <= val:
                L[cur] = max(L[cur], 1 + L[pre])

    return L


# ----------
seq = seq5

print(seq)

lis_length_list = basic_lis(seq)
print(lis_length_list)

# this is the length of LIS
lis_length = sorted(lis_length_list)[-1]
print(lis_length)

idx = np.argmax(np.array(lis_length_list))


# ----------------------------------------------------------------------------
# Longest Increasing (non-Decreasing) Subsequence (LIS):  bisect
# This return LIS itself !!
# ----------------------------------------------------------------------------

from bisect import bisect

def lis(seq):

    end = []

    for val in seq:
        idx = bisect(end, val)
        if idx == len(end): end.append(val)
        else: end[idx] = val

        print(f'{val} - {end}')

    return end


# ----------
# bisect returns the index the value (=3) is inserted
bisect(seq4, 3)


# ----------
seq = seq4

print(seq)

lis_seq = lis(seq)

# LIS itself !!!
print(lis_seq)

# this is the length of LIS
print(len(lis_seq))

