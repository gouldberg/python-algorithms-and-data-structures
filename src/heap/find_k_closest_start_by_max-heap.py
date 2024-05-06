# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

import itertools

import heapq


# ----------------------------------------------------------------------------
# find k-closest starts
#  - max-heap
#  - time complexity:  O(n * log(k))
# ----------------------------------------------------------------------------

class Star:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs):
        return self.distance < rhs.distance


def find_closest_k_starts(stars, k):
    # max_heap to store the closest k starts seen so far.
    max_heap = []

    for star in stars:
        # Add each star to the max-heap.
        # If the max-heap size exceeds k, remove the maximum element from the max-heap.
        # As python has only min-heap, insert tuple (negative of distance, start) to
        # sort in reversed distance order.
        heapq.heappush(max_heap, (-star.distance, star))
        if len(max_heap) == k + 1:
            heapq.heappop(max_heap)

    # Iteratively extract from the max-heap, which yields the stars sorted.
    # according from furthest to closest.
    return [s[1] for s in heapq.nlargest(k, max_heap)]


# ----------
# Model starts as points, and assume distances are in years.
# The Milky Way consists of approximately 10^12 starts.
# Earth coordinate is at (0,0,0)

stars_coord = [
    (10,10,10),
    (2,2,20),
    (3,3,18),
    (4,20,10),
    (5,3,10),
    (3,2,4),
    (4,8,19),
    (20,12,3),
    (15,13,10),
    (9,9,4),
    (8,2,15),
    (20,23,24),
    (15,13,12),
    (21,23,25)
]

stars = [Star(stars_coord[i][0], stars_coord[i][1], stars_coord[i][2]) for i in range(len(stars_coord))]


# ----------
k = 2

stars_found = find_closest_k_starts(stars=stars, k=k)

print([(stars_found[i].x, stars_found[i].y, stars_found[i].z) for i in range(k)])
