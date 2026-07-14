# mypy: disable-error-code="empty-body"
# QUESTION: Aggressive Cows
# Given stall positions in an array and k cows, place the cows in stalls so that
# the minimum distance between any two of them is as large as possible. Return that
# largest minimum distance.
# Example 1:
# Input: stalls = [0,3,4,7,10,9], k = 4
# Output: 3
# Explanation: Sorted = [0,3,4,7,9,10]; placing cows at 0,3,7,10 gives min gap 3,
# which is the maximum achievable.
# Constraints:
# 2 <= k <= len(stalls) <= 10^5

"""
#Brute Force:
1. Sort stalls. For each candidate distance from 1 to (max - min), greedily check
   if all k cows can be placed with at least that spacing.
2. The first distance that FAILS means the previous one is the answer.
TC -> O(N logN) + O(N * (max - min)), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the distance is the improvement.

#Optimal Approach:
1. Sort stalls. Feasibility "can place k cows with min gap >= d" is monotone
   decreasing in d, so binary search d in [1, max - min].
2. Greedy check: place first cow at stalls[0], then each next cow at the first
   stall at least d away; count placed cows.
3. If feasible, record d and try larger (low = mid + 1); else smaller (high = mid-1).
TC -> O(N logN) + O(N * log(max - min)), SC -> O(1)

#KEY INSIGHT:
- A wider required gap can only make placement harder, so feasibility is monotone
  in d; we binary search the LARGEST feasible gap (maximize the minimum).
"""

from typing import List


class Solution:
    def _can_place(self, stalls: List[int], dist: int, k: int) -> bool:
        last = stalls[0]
        placed = 1
        for i in range(1, len(stalls)):
            if stalls[i] - last >= dist:
                placed += 1
                last = stalls[i]
                if placed >= k:
                    return True
        return placed >= k

    def aggressive_cows_brute(self, stalls: List[int], k: int) -> int:
        stalls.sort()
        limit = stalls[-1] - stalls[0]
        for d in range(1, limit + 1):
            if not self._can_place(stalls, d, k):
                return d - 1
        return limit

    def aggressive_cows_better(self, stalls: List[int], k: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def aggressive_cows_optimal(self, stalls: List[int], k: int) -> int:
        stalls.sort()
        low, high = 1, stalls[-1] - stalls[0]
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if self._can_place(stalls, mid, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.aggressive_cows_optimal([0, 3, 4, 7, 10, 9], 4))
