# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Dynamic Programming:  Levenshtein Distance
# ----------------------------------------------------------------------------

def levenshtein_distance(A, B):

    def compute_distance_between_prefixes(A_idx, B_idx):

        print(f'{A_idx}: {A[0:(A_idx+1)]}{" " * (len(A) - A_idx - 1)} - {B_idx}: {B[0:(B_idx+1)]}{" " * (len(B) - B_idx - 1)}')

        if A_idx < 0:
            # A is empty so add all of B's characters.
            return B_idx + 1
        elif B_idx < 0:
            # B is empty so delete all of A's characters.
            return A_idx + 1

        if distance_between_prefixes[A_idx][B_idx] == -1:

            # if the last character of A is equal to the last character of B
            if A[A_idx] == B[B_idx]:
                distance_between_prefixes[A_idx][B_idx] =\
                    (compute_distance_between_prefixes(A_idx - 1, B_idx - 1))

            else:
                # if the last character of A is NOT equal to the last character of B
                substitute_last = compute_distance_between_prefixes(A_idx - 1, B_idx - 1)
                add_last = compute_distance_between_prefixes(A_idx - 1, B_idx)
                delete_last = compute_distance_between_prefixes(A_idx, B_idx - 1)

                distance_between_prefixes[A_idx][B_idx] = (1 + min(substitute_last, add_last, delete_last))

        return distance_between_prefixes[A_idx][B_idx]

    distance_between_prefixes = [[-1] * len(B) for _ in A]

    return compute_distance_between_prefixes(len(A) - 1, len(B) - 1)


# ----------
A = 'Carthorse'
B = 'Orchestra'

print(levenshtein_distance(A, B))


# ----------------------------------------------------------------------------
# Dynamic Programming:  Levenshtein Distance
# One-Liner
# ----------------------------------------------------------------------------

ls = lambda a, b: len(b) if not a else len(a) if not b else min(
    ls(a[1:], b[1:]) + (a[0] != b[0]),
    ls(a[1:], b) + 1,
    ls(a, b[1:]) + 1
)

ls(A, B)
