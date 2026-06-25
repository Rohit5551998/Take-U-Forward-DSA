# QUESTION: Sort an array of 0's 1's and 2's
# Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
#
# Examples:
# Input: nums = [1, 0, 2, 1, 0]
# Output: [0, 0, 1, 1, 2]
# Explanation: The nums array in sorted order has 2 zeroes, 2 ones and 1 two
#
# Input: nums = [0, 0, 1, 1, 1]
# Output: [0, 0, 1, 1, 1]
# Explanation: The nums array in sorted order has 2 zeroes, 3 ones and zero twos.


"""
#Brute Force:
1. Hand the array to the language's built-in `.sort()`.
2. It works, but it treats the input as a general comparison sort and ignores
   the fact that there are only three distinct values — so we pay the full
   comparison-sort cost for no reason.
TC -> O(n log n), SC -> O(1)

#Better Approach:
1. First pass: count how many 0s, 1s and 2s exist by tallying into a hashmap.
2. Second pass: overwrite the array in place from the left — write all the 0s,
   then all the 1s, then all the 2s, using the counts to know how many of each.
3. Two linear passes, no comparisons, but we read the array twice.
TC -> O(n), SC -> O(1)  # hashmap holds at most 3 keys

#Optimal Approach (Dutch National Flag — one pass, three pointers):
1. Carve the array into four regions via three pointers: [0, low) = settled 0s,
   [low, mid) = settled 1s, [mid, high] = the unknown region still to scan, and
   (high, end] = settled 2s.
2. Initialise low = 0, mid = 0, high = len-1 — at the start everything is in the
   "unknown" region.
3. Scan with `mid`, looping while mid <= high (i.e. while the unknown region is
   non-empty), and branch on arr[mid]:
4.   - arr[mid] == 0: it belongs at the front, so swap arr[low] <-> arr[mid], then
     advance BOTH low and mid — the value that just moved into mid came from the
     1s region, so it's already correct and safe to step past.
5.   - arr[mid] == 1: it's already in its final region, so just advance mid.
6.   - arr[mid] == 2: swap arr[mid] <-> arr[high] and shrink high by 1, but do NOT
     advance mid — the value pulled in from `high` is unexamined, so it must be
     re-checked on the next iteration.
7. When mid passes high the unknown region is empty and the array is partitioned
   0s | 1s | 2s — sorted in a single pass with no counting and no extra space.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- One pass with low/mid/high pointers partitions the array into 0s / 1s / 2s.
  The subtlety: after swapping a 2 to the high end you must NOT advance mid,
  because the value just brought in from `high` hasn't been classified yet.
"""

from typing import List


class Solution:
    def sort_an_array_of_zeros_ones_and_twos_brute(self, arr: List[int]) -> List[int]:
        arr.sort()
        return arr

    def sort_an_array_of_zeros_ones_and_twos_better(self, arr: List[int]) -> List[int]:
        hashMap = dict()
        hashMap[0] = 0
        hashMap[1] = 0
        hashMap[2] = 0

        for i in range(0, len(arr)):
            hashMap[arr[i]] += 1

        i = -1
        while hashMap[0] != 0:
            i += 1
            arr[i] = 0
            hashMap[0] -= 1

        while hashMap[1] != 0:
            i += 1
            arr[i] = 1
            hashMap[1] -= 1

        while hashMap[2] != 0:
            i += 1
            arr[i] = 2
            hashMap[2] -= 1

        return arr

    def sort_an_array_of_zeros_ones_and_twos_optimal(self, arr: List[int]) -> List[int]:
        low, mid, high = 0, 0, len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1

            elif arr[mid] == 1:
                mid += 1

            elif arr[mid] == 2:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr


if __name__ == "__main__":
    sol = Solution()
    arr = [0, 1, 2, 0, 0, 1, 2, 0, 0, 1, 2, 0]
    print(sol.sort_an_array_of_zeros_ones_and_twos_brute(arr))
    arr = [0, 1, 2, 0, 0, 1, 2, 0, 0, 1, 2, 0]
    print(sol.sort_an_array_of_zeros_ones_and_twos_better(arr))
    arr = [0, 1, 2, 0, 0, 1, 2, 0, 0, 1, 2, 0]
    print(sol.sort_an_array_of_zeros_ones_and_twos_optimal(arr))
