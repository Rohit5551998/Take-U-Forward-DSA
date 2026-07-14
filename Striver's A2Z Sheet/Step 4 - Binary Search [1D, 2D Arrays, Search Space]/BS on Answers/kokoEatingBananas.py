# mypy: disable-error-code="empty-body"
# QUESTION: Koko Eating Bananas
# Koko has piles of bananas and h hours. Each hour she picks one pile and eats up
# to k bananas from it (if the pile has fewer, she finishes it and waits). Find the
# minimum integer eating speed k so she finishes all piles within h hours.
# Example 1:
# Input: piles = [7,15,6,3], h = 8
# Output: 5
# Explanation: At speed 5 the hours are 2+3+2+1 = 8 <= 8, and no smaller speed works.
# Constraints:
# 1 <= len(piles) <= 10^4
# 1 <= piles[i] <= 10^9, len(piles) <= h

"""
#Brute Force:
1. Try every speed k from 1 to max(piles). For each, total hours = sum(ceil(pile/k)).
2. Return the first k whose total hours <= h.
TC -> O(max(piles) * N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the speed is the improvement.

#Optimal Approach:
1. The predicate "hours(k) <= h" is monotone: larger k never needs more hours.
2. Binary search k in [1, max(piles)].
3. If hours(mid) <= h, mid is feasible; record it and try smaller (high = mid - 1).
4. Else mid too slow -> low = mid + 1.
5. Return the smallest feasible k.
TC -> O(N * log(max(piles))), SC -> O(1)

#KEY INSIGHT:
- Eating speed vs total hours is a monotone relationship, so we binary search the
  smallest speed satisfying the hour budget instead of scanning all speeds.
"""

import math
from typing import List


class Solution:
    def _hours(self, piles: List[int], k: int) -> int:
        return sum(math.ceil(p / k) for p in piles)

    def koko_brute(self, piles: List[int], h: int) -> int:
        for k in range(1, max(piles) + 1):
            if self._hours(piles, k) <= h:
                return k
        return -1

    def koko_better(self, piles: List[int], h: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def koko_optimal(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = high
        while low <= high:
            mid = low + (high - low) // 2
            if self._hours(piles, mid) <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.koko_optimal([7, 15, 6, 3], 8))
