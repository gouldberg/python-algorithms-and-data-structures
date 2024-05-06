# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Merging Intervals:  Sorting
# ----------------------------------------------------------------------------

def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []

    # Processes intervals in disjoint_intervals which come before new_interval.
    while(i < len(disjoint_intervals)
        and new_interval.left > disjoint_intervals[i].right):
        result.append(disjoint_intervals[i])
        i += 1

    # Processes intervals in disjoint_intervals which overlap with new_interval.
    while(i < len(disjoint_intervals)
        and new_interval.right >= disjoint_intervals[i].left):
        # If [a, b] and [c, d] overlap, union is [min(a, c), max(b, d)].
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right))
        i += 1

    # Processes intervals in disjoint_intervals which come after new_interval.
    return result + [new_interval] + disjoint_intervals[i:]



# ----------
import collections

Interval = collections.namedtuple('Interval', ('left', 'right'))

disjoint_intervals = [Interval(l, r) for l, r in [(-4, -1), (0, 2), (3, 6), (7, 9), (11, 12), (14, 17)]]

new_interval = Interval(1, 8)

print(add_interval(disjoint_intervals, new_interval))

