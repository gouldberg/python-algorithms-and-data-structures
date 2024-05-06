# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Huffman algorithm
# ----------------------------------------------------------------------------

from heapq import heapify, heappush, heappop

from itertools import count


def huffman(seq, frq):

    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)

    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa + fb, n, [a, b]))

    return trees[0][-1]


def codes(tree, prefix=""):

    if len(tree) == 1:
        yield (tree, prefix)
        return

    # 0 for left and 1 for right
    for bit, child in zip("01", tree):
        for pair in codes(child, prefix + bit):
            yield pair



# ----------
seq = "abcdefghi"

freq = [4,5,6,9,11,12,15,16,20]

tree = huffman(seq, freq)

print(tree)


# ----------
# huffman code
huffman_code = codes(tree)

# 0 for left and 1 for right in tree
print(dict(huffman_code))



