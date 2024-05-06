# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import itertools


# ----------------------------------------------------------------------------
# find maximum slice
#  - brute-force approach
#  - time complexity:  O(n^3)
# ----------------------------------------------------------------------------

A = [0,1,2,3,-2,5,-3,4,-20,6,-5,12,-20,-23,-3,2,3,4,5,9,6,-20,-5]

A = [904, 40, 523, 12, -335, -385, -124, 481, -31]

n = len(A)


# ----------
result = max((A[i:j] for i in range(n) for j in range(i+1, n+1)), key=sum)

print(result)
print(sum(result))


# ----------------------------------------------------------------------------
# find maximum slice
#  - time complexity:  O(n^2)
# ----------------------------------------------------------------------------

best = A[0]

for size in range(1, n+1):

    cur = sum(A[:size])
    best = max(best, cur)
    print(f'cur_{size}: {cur}')
    print(f'bset_{size}: {best}')

    for i in range(n - size):
        cur += A[i + size] - A[i]
        best = max(best, cur)
        print(f'   cur_{size}_{i}: {cur}')
        print(f'   best_{size}_{i}: {best}')

print(best)


# ----------------------------------------------------------------------------
# find maximum slice
#  - time complexity:  O(n)
# ----------------------------------------------------------------------------

max_ending = max_slice = 0

for a in A:
    max_ending = max(0, max_ending + a)
    max_slice = max(max_slice, max_ending)


# ----------
print(max_slice)



# ----------------------------------------------------------------------------
# find maximum slice
#  - dynamic programming approach
# ----------------------------------------------------------------------------

def find_maximum_subarray(A):
    min_sum = max_sum = 0
    print(f'{min_sum} - {max_sum}')
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
        print(f'{min_sum} - {max_sum}')

    return max_sum

print(list(itertools.accumulate(A)))

print(find_maximum_subarray(A))
