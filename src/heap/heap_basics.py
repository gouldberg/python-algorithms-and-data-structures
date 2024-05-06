# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import heapq


# ----------------------------------------------------------------------------
# Priority queue
#  - get min or max value by time complexity O(log(n))
#  - insert element by time complexity O(log(n))
# ----------------------------------------------------------------------------

a = [1, 6, 8, 0, -1]


# ----------
heapq.heapify(a)

print(a)


# ----------
# get min out
heapq.heappop(a)

print(a)


# ----------
# insert element
heapq.heappush(a, -2)

print(a)


# ----------
# get max out

# all elements multiplied by -1
a = list(map(lambda x: x*(-1), a))

print(a)

heapq.heapify(a)

print(heapq.heappop(a)*(-1))

print(a)
