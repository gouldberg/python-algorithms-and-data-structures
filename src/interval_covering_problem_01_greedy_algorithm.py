# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Greedy Algorithm:  The Interval Covering Problem
# ----------------------------------------------------------------------------

import collections
import operator

def find_minimum_visits(intervals):
    # sort intervals based on the right endpoints.
    intervals.sort(key=operator.attrgetter('right'))

    last_visit_time, num_visits = float('-inf'), 0

    for interval in intervals:
        if interval.left > last_visit_time:
            # the current right endpoint, last_visit_time, will not cover any more intervals.
            last_visit_time = interval.right
            print(f'last_visit_time: {last_visit_time}')
            num_visits += 1

    return num_visits


# ----------
Interval = collections.namedtuple('Interval', ('left', 'right'))

intervals = [Interval(r,l) for r,l in [(1,2),(2,3),(3,4),(2,3),(3,4),(4,5)]]

print(intervals)

print(find_minimum_visits(intervals))

