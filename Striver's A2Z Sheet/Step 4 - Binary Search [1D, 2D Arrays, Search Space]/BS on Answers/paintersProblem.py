# mypy: disable-error-code="empty-body"
# QUESTION: Painter's Partition Problem
# Given boards[i] (length of board i) and m painters, each painter paints a
# contiguous block of boards and takes 1 unit time per unit length. Minimize the
# total time to paint all boards (i.e. minimize the maximum block length).
# Example 1:
# Input: boards = [25,46,28,49,24], m = 4
# Output: 71
# Explanation: The optimal partition gives a maximum painter workload of 71.
# Constraints:
# 1 <= m <= len(boards) <= 10^5
# 1 <= boards[i] <= 10^6

"""
#Brute Force:
1. If m > n return -1. The answer lies in [max(boards), sum(boards)].
2. For each candidate max-time, greedily count painters needed (start a new painter
   when the running length would exceed the candidate).
3. Return the first candidate needing <= m painters.
TC -> O((sum - max + 1) * N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the max-time is the improvement.

#Optimal Approach:
1. Painters-needed is monotone non-increasing in the allowed max-time, so
   "painters(x) <= m" is monotone. Binary search x in [max(boards), sum(boards)].
2. If painters(mid) <= m, mid is feasible; record it and try smaller (high=mid-1).
3. Else mid too small -> low = mid + 1.
TC -> O(N * log(sum - max)), SC -> O(1)

#KEY INSIGHT:
- Same monotone "minimize the maximum contiguous block" pattern as Book Allocation
  and Split Array Largest Sum; only the story changes.
"""

from typing import List


class Solution:
    def _painters(self, boards: List[int], max_time: int) -> int:
        painters = 1
        painted = 0
        for length in boards:
            if painted + length <= max_time:
                painted += length
            else:
                painters += 1
                painted = length
        return painters

    def painters_brute(self, boards: List[int], m: int) -> int:
        if m > len(boards):
            return -1
        for x in range(max(boards), sum(boards) + 1):
            if self._painters(boards, x) <= m:
                return x
        return -1

    def painters_better(self, boards: List[int], m: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def painters_optimal(self, boards: List[int], m: int) -> int:
        if m > len(boards):
            return -1
        low, high = max(boards), sum(boards)
        ans = high
        while low <= high:
            mid = low + (high - low) // 2
            if self._painters(boards, mid) <= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.painters_optimal([25, 46, 28, 49, 24], 4))
