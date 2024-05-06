# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# permutations
#  - recursion
#  - time complexity: O(n * n!)
# ----------------------------------------------------------------------------

def permutations(A):

    def directed_permutations(i):

        if i == len(A) - 1:
            result.append(A.copy())
            return

        # Try every possibility for A[i].
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            # Generate all permutations for A[i+1:].
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result = []
    directed_permutations(0)
    return result


# ----------
A = [5,3,7]
A = [5,3,7,1,2]


result = permutations(A)
print(result)
print(len(result))


# ----------------------------------------------------------------------------
# permutations
#  - recursion
#  - time complexity: O(n * n!)
# ----------------------------------------------------------------------------

def next_permutation(perm):

    # Find the first entry from the right that is smaller than the entry
    # immediately after it.
    inversion_point = len(perm) - 2
    while (inversion_point >= 0
           and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []  # perm is the last permutation.

    # Swap the smallest entry after index inversion_point that is greater than
    # perm[inversion_point]. Since entries in perm are decreasing after
    # inversion_point, if we search in reverse order, the first entry that is
    # greater than perm[inversion_point] is the entry to swap with.
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    # Entries in perm must appear in decreasing order after inversion_point,
    # so we simply reverse these entries to get the smallest dictionary order.
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm


def permutations2(A):

    result = []
    while True:
        result.append(A.copy())
        A = next_permutation(A)
        if not A:
            break

    return result


# ----------
A = [5,3,7]
A = [5,3,7,1,2]


result = permutations2(A)
print(result)
print(len(result))

