# mypy: disable-error-code="empty-body"
# QUESTION: Merge Overlapping Intervals
# Given an array of intervals where intervals[i] = [start, end], merge all
# overlapping intervals and return the non-overlapping intervals covering the
# same ranges.
# Example 1:
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: [1,3] and [2,6] overlap and merge into [1,6].
# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2, 0 <= start <= end <= 10^4

"""
#Brute Force:
1. Sort intervals by start. For each interval not already covered by the last
   result, extend its end by scanning forward over every interval whose start is
   within the current end.
2. Append the merged [start, end]; skip intervals already absorbed.
TC -> O(n log n) + O(2n), SC -> O(n)

#Better Approach:
SKIPPED — the single-pass sweep below is the direct optimization; there is no
distinct intermediate tier.

#Optimal Approach (Sort + Single Pass):
1. Sort intervals by start.
2. Walk once: if the result is empty or the current start is beyond the last
   merged end, push the interval as a new block.
3. Otherwise the current interval overlaps the last block, so extend the last
   block's end to max(lastEnd, currentEnd).
TC -> O(n log n) + O(n), SC -> O(n)

#KEY INSIGHT:
- Once sorted by start, overlap is decided solely by comparing each interval's
  start with the running merged end, so one pass suffices.
"""

from typing import List


class Solution:
    def merge_intervals_brute(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans: List[List[int]] = []
        for i in range(len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if ans and end <= ans[-1][1]:
                continue
            for j in range(i + 1, len(intervals)):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])
                else:
                    break
            ans.append([start, end])
        return ans

    def merge_intervals_better(self, intervals: List[List[int]]) -> List[List[int]]:
        # SKIP: no distinct better tier; single-pass sweep is the optimal.
        pass

    def merge_intervals_optimal(self, intervals: List[List[int]]) -> List[List[int]]:
        ans: List[List[int]] = []
        intervals.sort()
        for i in range(len(intervals)):
            if not ans or intervals[i][0] > ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.merge_intervals_optimal([[1, 3], [2, 6], [8, 10], [15, 18]]))
