# mypy: disable-error-code="empty-body"
# QUESTION: Non-overlapping Intervals
# Given an array of intervals where intervals[i] = [start_i, end_i], return the minimum
# number of intervals you need to remove to make the rest of the intervals
# non-overlapping. Intervals that only touch at a point (e.g. [1, 2] and [2, 3]) are
# considered non-overlapping.
#
# Example 1:
# Input: intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# Output: 1
# Explanation: Remove [1, 3] and the remaining intervals are non-overlapping.
#
# Constraints:
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= start_i < end_i <= 5 * 10^4

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

from typing import List


class Solution:
    def non_overlapping_intervals_brute(self, intervals: List[List[int]]) -> int:
        pass

    def non_overlapping_intervals_better(self, intervals: List[List[int]]) -> int:
        pass

    def non_overlapping_intervals_optimal(self, intervals: List[List[int]]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.non_overlapping_intervals_optimal([[1, 2], [2, 3], [3, 4], [1, 3]]))
