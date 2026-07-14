# mypy: disable-error-code="empty-body"
# QUESTION: Merge Intervals
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all
# overlapping intervals and return an array of the non-overlapping intervals that
# cover all the intervals in the input.
#
# Example 1:
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: [1, 3] and [2, 6] overlap, so they merge into [1, 6].
#
# Constraints:
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^4

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
    def merge_intervals_brute(self, intervals: List[List[int]]) -> List[List[int]]:
        pass

    def merge_intervals_better(self, intervals: List[List[int]]) -> List[List[int]]:
        pass

    def merge_intervals_optimal(self, intervals: List[List[int]]) -> List[List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.merge_intervals_optimal([[1, 3], [2, 6], [8, 10], [15, 18]]))
