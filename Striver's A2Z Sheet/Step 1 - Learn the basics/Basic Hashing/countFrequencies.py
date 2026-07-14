# mypy: disable-error-code="empty-body"
# QUESTION: Count Frequencies of Elements in an Array
# Given an array of n integers, count the frequency (number of occurrences) of
# every distinct element in the array and report each element with its count.
#
# Example 1:
# Input: arr = [2, 3, 2, 3, 5]
# Output: 2 -> 2, 3 -> 2, 5 -> 1
# Explanation: 2 occurs twice, 3 occurs twice, 5 occurs once.
#
# Example 2:
# Input: arr = [10, 10, 10, 10]
# Output: 10 -> 4
# Explanation: 10 occurs four times.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= arr[i] <= 10^9


"""
#Brute Force:
1. For each distinct element, scan the whole array again and count how many
   times it appears (nested loops).
2. Print / collect element -> count, guarding against re-counting duplicates.
TC -> O(n^2), SC -> O(1) (ignoring output)

#Better Approach:
SKIPPED — there is no meaningful middle tier between the O(n^2) rescan and the
O(n) hashmap; the hashmap is the natural next (and optimal) step.

#Optimal Approach (count_frequencies_optimal):
1. Create an empty hashmap (dict) mapping value -> count.
2. Traverse the array once; for each value increment its bucket
   (initialise to 0 on first sight).
3. The dict now holds the frequency of every distinct element in one pass.
TC -> O(n), SC -> O(k) where k = number of distinct elements

#KEY INSIGHT:
- A hashmap gives O(1) average lookup/update per element, so a single linear
  pass replaces the quadratic rescan-per-element counting.
"""

from typing import Dict, List


class Solution:
    def count_frequencies_brute(self, arr: List[int]) -> Dict[int, int]:
        n = len(arr)
        freq: Dict[int, int] = {}
        for i in range(n):
            if arr[i] in freq:
                continue  # already counted this value
            count = 0
            for j in range(n):
                if arr[j] == arr[i]:
                    count += 1
            freq[arr[i]] = count
        return freq

    def count_frequencies_better(self, arr: List[int]) -> Dict[int, int]:
        # SKIP: no distinct middle tier; hashmap pass is the natural optimal.
        pass

    def count_frequencies_optimal(self, arr: List[int]) -> Dict[int, int]:
        freq: Dict[int, int] = {}
        for value in arr:
            freq[value] = freq.get(value, 0) + 1
        return freq


if __name__ == "__main__":
    sol = Solution()
    print(sol.count_frequencies_optimal([2, 3, 2, 3, 5]))
    print(sol.count_frequencies_optimal([10, 10, 10, 10]))
