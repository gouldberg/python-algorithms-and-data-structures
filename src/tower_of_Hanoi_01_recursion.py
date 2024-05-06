# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# compute tower of Hanoi
#  - recursion
#  - time complexity:  O(2^n)
# ----------------------------------------------------------------------------

def compute_tower_hanoi(num_rings):

    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move - 1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            print(f'pegs : {pegs}')
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move - 1, use_peg, to_peg, from_peg)

    # Initialize pegs.
    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    print(f'pegs : {pegs}')
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result


# ----------
NUM_PEGS = 3
num_rings = 6

pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]

# this is initialize pegs
print(pegs)


# ----------
# pop top peg (now 1) from peg 0 and append to peg 2
from_peg = 0
to_peg = 2
pegs[to_peg].append(pegs[from_peg].pop())

print(pegs)


# ----------
NUM_PEGS = 3
num_rings = 6

result = compute_tower_hanoi(num_rings=num_rings)

print(result)

