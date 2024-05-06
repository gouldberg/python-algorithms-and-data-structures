# -*- coding: utf-8 -*-

sys.path.append("C:\\Users\\kouse\\kw\\venv\\Lib\\site-packages")


# ----------------------------------------------------------------------------
# Find bitonic point in given biotonic sequence
# ----------------------------------------------------------------------------

def binarySearch(arr, left, right):

    if left <= right:

        mid = (left + right) // 2

        # base condition to check if arr[mid] is bitonic point or not
        if (arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]):
            return mid

        # We assume that sequence is bitonic.
        # We go to right subarray if middle point is part of increasing subsequence.
        # Else we go to left subarray.

        if (arr[mid] < arr[mid + 1]):
            return binarySearch(arr, mid + 1, right)
        else:
            return binarySearch(arr, left, mid - 1)

    return -1


# ----------
seq = [6, 7, 8, 11, 9, 5, 2, 1];

n = len(seq)

index = binarySearch(seq, 1, n - 2)

if (index != -1): print(seq[index])

