# mypy: disable-error-code="empty-body"
# QUESTION: Find the Highest and Lowest Frequency Element
# Given an array of n integers, find the element with the highest frequency
# (occurs the most) and the element with the lowest frequency (occurs the
# least). Return them as [highestFreqElement, lowestFreqElement].
#
# Example 1:
# Input: arr = [2, 3, 2, 3, 5, 3, 2, 2, 1]
# Output: [2, 5]
# Explanation: 2 occurs 4 times (highest); 5 and 1 each occur once (lowest) —
# the first one encountered with the minimum count is reported.
#
# Example 2:
# Input: arr = [1, 1, 1, 2]
# Output: [1, 2]
# Explanation: 1 occurs 3 times (highest); 2 occurs once (lowest).
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= arr[i] <= 10^9


"""
#Brute Force:
1. For each distinct value, rescan the array to count its occurrences.
2. Track the value achieving the maximum count and the value achieving the
   minimum count.
TC -> O(n^2), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; once we decide to use a hashmap we are
already at the optimal linear solution.

#Optimal Approach (highest_lowest_frequency_optimal):
1. Build a frequency hashmap in one pass over the array.
2. Iterate over the map's items, tracking maxFrequency/maxElement and
   minFrequency/minElement (seed min with +infinity so the first entry wins).
3. Return [maxElement, minElement].
TC -> O(n), SC -> O(k) where k = number of distinct elements

#KEY INSIGHT:
- Counting frequencies with a hashmap (O(n)) then a single linear scan of the
  distinct keys reduces the O(n^2) rescan-per-element approach to O(n).
"""

import math
from typing import Dict, List


class Solution:
    def highest_lowest_frequency_brute(self, arr: List[int]) -> List[int]:
        n = len(arr)
        seen: Dict[int, bool] = {}
        maxElement, maxFrequency = arr[0], 0
        minElement, minFrequency = arr[0], math.inf
        for i in range(n):
            if arr[i] in seen:
                continue
            seen[arr[i]] = True
            count = 0
            for j in range(n):
                if arr[j] == arr[i]:
                    count += 1
            if count > maxFrequency:
                maxFrequency, maxElement = count, arr[i]
            if count < minFrequency:
                minFrequency, minElement = count, arr[i]
        return [maxElement, minElement]

    def highest_lowest_frequency_better(self, arr: List[int]) -> List[int]:
        # SKIP: no distinct middle tier; hashmap pass is the natural optimal.
        pass

    def highest_lowest_frequency_optimal(self, arr: List[int]) -> List[int]:
        freq: Dict[int, int] = {}
        for value in arr:
            freq[value] = freq.get(value, 0) + 1

        maxElement, maxFrequency = arr[0], 0
        minElement, minFrequency = arr[0], math.inf
        for key, value in freq.items():
            if value > maxFrequency:
                maxFrequency, maxElement = value, key
            if value < minFrequency:
                minFrequency, minElement = value, key
        return [maxElement, minElement]


if __name__ == "__main__":
    sol = Solution()
    print(sol.highest_lowest_frequency_optimal([2, 3, 2, 3, 5, 3, 2, 2, 1]))
    print(sol.highest_lowest_frequency_optimal([1, 1, 1, 2]))
