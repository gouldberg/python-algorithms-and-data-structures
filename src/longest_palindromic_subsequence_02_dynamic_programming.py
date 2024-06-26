# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")

# https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/


# ----------------------------------------------------------------------------
# Longest Palindromic Subsequence (LPS):  Dynamic Programming
# ----------------------------------------------------------------------------

def lps(str):
    n = len(str)

    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n): L[i][i] = 1

    # Build the table. Note that the lower diagonal values of table are useless and
    # not filled in the process.
    # The values are filled in a manner similar to Matrix Chain Multiplication DP solution
    # (See https://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
    # cl is length of substring
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if str[i] == str[j] and cl == 2:
                L[i][j] = 2
            elif str[i] == str[j]:
                L[i][j] = L[i + 1][j - 1] + 2
            else:
                L[i][j] = max(L[i][j - 1], L[i + 1][j])

    return L[0][n - 1]

# ----------
seq = "GEEKS FOR GEEKS"
seq = "amazon"

n = len(seq)
print("The length of the LPS is " + str(lps(seq)))

