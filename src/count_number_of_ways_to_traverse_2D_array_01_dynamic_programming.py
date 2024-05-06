# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# count the number of ways to traverse a 2D array
#  - dynamic programming
# ----------------------------------------------------------------------------

def number_of_ways(n, m):
    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1

        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x - 1, y)
            ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y - 1)
            number_of_ways[x][y] = ways_top + ways_left
        return number_of_ways[x][y]

    number_of_ways = [[0] * m for _ in range(n)]

    return compute_number_of_ways_to_xy(n - 1, m - 1)

