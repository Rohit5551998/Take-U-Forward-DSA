# mypy: disable-error-code="empty-body"
# QUESTION: Minimum Number of Days to Make M Bouquets
# Given bloomDay[i] (the day flower i blooms), and integers m and k: to make one
# bouquet you need k ADJACENT bloomed flowers. Return the minimum number of days
# to make m bouquets, or -1 if impossible.
# Example 1:
# Input: bloomDay = [7,7,7,7,13,11,12,7], m = 2, k = 3
# Output: 12
# Explanation: By day 12, flowers form two runs of >=3 adjacent bloomed flowers.
# Constraints:
# 1 <= len(bloomDay) <= 10^5
# 1 <= bloomDay[i] <= 10^9

"""
#Brute Force:
1. If m*k > n it's impossible -> -1.
2. For each candidate day from min(bloomDay) to max(bloomDay), count how many
   bouquets can be made (scan runs of adjacent flowers with bloomDay <= day).
3. Return the first day where bouquets >= m.
TC -> O((max-min+1) * N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the day is the improvement.

#Optimal Approach:
1. Impossible check: if m*k > n return -1.
2. Bouquets-makeable is monotone non-decreasing in the day, so binary search the
   day in [min(bloomDay), max(bloomDay)].
3. If bouquets(mid) >= m, mid works; record it and search earlier (high = mid - 1).
4. Else need more days -> low = mid + 1.
TC -> O(N * log(max-min+1)), SC -> O(1)

#KEY INSIGHT:
- Waiting longer can only make MORE flowers available, so feasibility is monotone
  in the number of days — the classic setup for binary search on the answer.
"""

from typing import List


class Solution:
    def _bouquets(self, bloom: List[int], day: int, k: int) -> int:
        bouquets = 0
        run = 0
        for b in bloom:
            if b <= day:
                run += 1
            else:
                bouquets += run // k
                run = 0
        bouquets += run // k
        return bouquets

    def bouquets_brute(self, bloom: List[int], m: int, k: int) -> int:
        if len(bloom) < m * k:
            return -1
        for day in range(min(bloom), max(bloom) + 1):
            if self._bouquets(bloom, day, k) >= m:
                return day
        return -1

    def bouquets_better(self, bloom: List[int], m: int, k: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def bouquets_optimal(self, bloom: List[int], m: int, k: int) -> int:
        if len(bloom) < m * k:
            return -1
        low, high = min(bloom), max(bloom)
        ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if self._bouquets(bloom, mid, k) >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.bouquets_optimal([7, 7, 7, 7, 13, 11, 12, 7], 2, 3))
