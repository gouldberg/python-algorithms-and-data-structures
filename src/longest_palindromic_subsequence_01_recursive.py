# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/


# ----------------------------------------------------------------------------
# Longest Palindromic Subsequence (LPS):  Recursive Solution
# ----------------------------------------------------------------------------

# A utility function to get max of two egers
def max(x, y):
    if (x > y): return x
    return y


# Returns the length of the longest palindromic subsequence in seq
def lps(seq, i, j):
    # Base Case 1: If there is only 1 character
    if (i == j): return 1

    # Base Case 2: If there are only 2 characters and both are same
    if (seq[i] == seq[j] and i + 1 == j): return 2

    # If the first and last characters match
    if (seq[i] == seq[j]): return lps(seq, i + 1, j - 1) + 2

    # If the first and last characters do not match
    return max(lps(seq, i, j - 1), lps(seq, i + 1, j))


# ----------
seq = "GEEKSFORGEEKS"
seq = "amazon"

n = len(seq)
print("The length of the LPS is", lps(seq, 0, n - 1))

