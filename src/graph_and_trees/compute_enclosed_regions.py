# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import numpy as np

import collections


# ----------------------------------------------------------------------------
# compute enclosed regions
#  - time complexity: O(m * n)
#  - space complexity: O(m * n)
# ----------------------------------------------------------------------------

def fill_surrounded_regions(board_orig):

    board = board_orig.copy()

    n, m = len(board), len(board[0])

    q = collections.deque(
        [(i, j) for k in range(n) for i, j in ((k, 0), (k, m -1))] +
        [(i, j) for k in range(m) for i, j in ((0, k), (n - 1, k))])

    while q:
        x, y = q.popleft()

        if 0 <= x < n and 0 <= y < m and board[x][y] == 'W':
            board[x][y] = 'T'
            q.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

    board[:] = [['B' if c != 'T' else 'W' for c in row] for row in board]

    return board


# ----------

A = np.array([
    ['B', 'B', 'B', 'B'],
    ['W', 'B', 'W', 'B'],
    ['B', 'W', 'W', 'B'],
    ['B', 'B', 'B', 'B']])


B = np.array([
    ['B', 'B', 'B', 'B'],
    ['W', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B'],
    ['B', 'B', 'B', 'B']])


A_filled = fill_surrounded_regions(board_orig=A)

# filled area is True
print((~(A == A_filled)))


B_filled = fill_surrounded_regions(board_orig=B)

# filled area is True
print((~(B == B_filled)))

