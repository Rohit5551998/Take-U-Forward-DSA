# QUESTION: Merge K Sorted Arrays
# You are given k sorted arrays, each of size k. Merge all the arrays
# into one sorted array and return it.
# You should use an efficient algorithm. The expected time complexity is
# O(k^2 log k) — equivalently O(N log k) where N is the total number of
# elements across all arrays.
#
# Examples:
# Example 1:
# Input: k = 3, arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Example 2:
# Input: k = 2, arrays = [[1, 4, 7], [2, 5, 8]]
# Output: [1, 2, 4, 5, 7, 8]
#
# Constraints:
# 1 <= k <= 100
# Each array has size k.
# -10^9 <= array[i][j] <= 10^9
#
# Optimal approach: use a min-heap of size k. Push the first element of
# each array into the heap (with array index + position). Pop the min,
# append to result, push the next element from the same array. Repeat
# until the heap is empty.


"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""


def merge_k_sorted_arrays_brute() -> None:
    pass


def merge_k_sorted_arrays_better() -> None:
    pass


def merge_k_sorted_arrays_optimal() -> None:
    pass
