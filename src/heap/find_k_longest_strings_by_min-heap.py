# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import itertools

import heapq


# ----------------------------------------------------------------------------
# find k-longest strings
#  - min-heap (not max-heap !!)
#  - time complexity:  O(n * log(k))
# ----------------------------------------------------------------------------

def top_k(k, stream):

    # Entries are compared by their lengths.
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in stream:
        # Push next_string and pop the shortest string in min_heap.
        heapq.heappushpop(min_heap, (len(next_string), next_string))

    return [p[1] for p in heapq.nsmallest(k, min_heap)]


# ----------
stream =\
    'Use a heap when all you care about is the largest or smallest elements,\
    and you do not need to support fast lookup, delete, or search operations for arbitrary elements.\
    A heap is a good choice when you need to compute the k largest or k smallest elements in a collection.\
    For the former, use a min-heap, for the latter, use a max-heap.'

stream = str.split(stream)
print(stream)

k = 10
min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
print(min_heap)

heapq.heapify(min_heap)
print(min_heap)

next_string = stream[0]
heapq.heappushpop(min_heap, (len(next_string), next_string))
print(min_heap)


# ----------
top_k(k=k, stream=stream)

