# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# maximum permutations
#  - brute-force approach
#  - time complexity: O(n^2)
# ----------------------------------------------------------------------------

def naive_max_perm(M, A=None):

    if A is None:
        A = set(range(len(M)))

    # base case
    if len(A) == 1:
        return A

    B = set(M[i] for i in A)
    C = A - B

    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)

    return A


# ----------
# 8 people get the ticket at movie theater.
# but each people prefer other people's position.
# first people prefers 2nd people's position

M = [2, 2, 0, 5, 3, 5, 7, 4]

# 0, 2, 5 people can change positions, but others cannot.
print(naive_max_perm(M=M))


# ----------------------------------------------------------------------------
# maximum permutations
#  - time complexity: O(n)
# ----------------------------------------------------------------------------

def max_perm(M):

    n = len(M)
    A = set(range(n))
    count = [0] * n
    for i in M:
        count[i] += 1

    Q = [i for i in A if count[i] == 0]

    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)

    return A


# ----------
M = [2, 2, 0, 5, 3, 5, 7, 4]

print(max_perm(M=M))

