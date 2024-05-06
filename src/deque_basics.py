# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

from collections import deque


# ----------------------------------------------------------------------------
# deque
#  - add element at top or tail by time complexity O(1)
# ----------------------------------------------------------------------------

a = [1, 2, 4, 5, 0]

a = deque(a)


# add element to tail
a.append(10)

# add element to top
a.appendleft(-1)

print(a)


# ----------
# count element 5
print(a.count(5))


# ----------
# index
print(a.index(10))


# ----------
# insert 2 at index 7
a.insert(7, 2)

print(a)


# ----------
a.pop()
a.popleft()

print(a)


# ----------
a.remove(4)

print(a)


a.reverse()

print(a)


# ----------
li = [6, 7, 8, 9]

a.extend(li)
a.extendleft(li)

print(a)


# ----------
a.rotate(1)

print(a)


a.rotate(-2)

print(a)


# ----------
a.clear()

print(a)


# ----------
# set maxlen

li = [1, 2, 3, 4, 5]

d = deque(li, 3)

print(d)
