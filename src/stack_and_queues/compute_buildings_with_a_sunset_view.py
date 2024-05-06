# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Compute building with a sunset view by stack
# buildings in east-to-west order
# ----------------------------------------------------------------------------

import collections

def examine_buildings_with_sunset(sequence):

    BuildingWithHeight = collections.namedtuple('BuildingWithHeight', ('id', 'height'))

    candidates = []

    for building_idx, building_height in enumerate(sequence):

        while candidates and building_height >= candidates[-1].height:

            candidates.pop()

        candidates.append(BuildingWithHeight(building_idx, building_height))

    return [c.id for c in reversed(candidates)]



# ----------
# the buildings height provided from east-to-west
sequence = [10, 11, 12, 7, 6, 5, 6, 7, 9]

# the buildings id with sunset view
examine_buildings_with_sunset(sequence)


