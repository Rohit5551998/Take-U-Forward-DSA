# mypy: disable-error-code="empty-body"
# QUESTION: Capacity to Ship Packages Within D Days
# Packages with weights[i] must be shipped in order over d days. Each day the ship
# loads packages (in given order) not exceeding its capacity. Find the minimum
# capacity that ships everything within d days.
# Example 1:
# Input: weights = [5,4,5,2,3,4,5,6], d = 5
# Output: 9
# Explanation: With capacity 9 the loads split into 5 days: [5,4],[5,2],[3,4],[5],[6].
# Constraints:
# 1 <= d <= len(weights) <= 5*10^4
# 1 <= weights[i] <= 500

"""
#Brute Force:
1. Capacity must be at least max(weights) and at most sum(weights).
2. For each candidate capacity from max to sum, greedily count days needed.
3. Return the first capacity needing <= d days.
TC -> O((sum - max + 1) * N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the capacity is the improvement.

#Optimal Approach:
1. Days-needed is monotone non-increasing as capacity grows, so "days(cap) <= d"
   is a monotone predicate.
2. Binary search capacity in [max(weights), sum(weights)].
3. If days(mid) <= d, mid works; record it and try smaller (high = mid - 1).
4. Else mid too small -> low = mid + 1.
TC -> O(N * log(sum - max)), SC -> O(1)

#KEY INSIGHT:
- More capacity can never need more days, so we binary search the smallest
  capacity that fits within the day budget.
"""

from typing import List


class Solution:
    def _days(self, weights: List[int], cap: int) -> int:
        days = 1
        load = 0
        for w in weights:
            if load + w <= cap:
                load += w
            else:
                days += 1
                load = w
        return days

    def ship_capacity_brute(self, weights: List[int], d: int) -> int:
        for cap in range(max(weights), sum(weights) + 1):
            if self._days(weights, cap) <= d:
                return cap
        return -1

    def ship_capacity_better(self, weights: List[int], d: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def ship_capacity_optimal(self, weights: List[int], d: int) -> int:
        low, high = max(weights), sum(weights)
        ans = high
        while low <= high:
            mid = low + (high - low) // 2
            if self._days(weights, mid) <= d:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.ship_capacity_optimal([5, 4, 5, 2, 3, 4, 5, 6], 5))
