# mypy: disable-error-code="empty-body"
# QUESTION: Insert Interval
# You are given an array of non-overlapping intervals intervals sorted in ascending
# order by start, and a new interval newInterval. Insert newInterval so that the
# intervals remain sorted and non-overlapping (merging where necessary). Return the
# resulting list of intervals.
#
# Example 1:
# Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
# Output: [[1, 5], [6, 9]]
# Explanation: [2, 5] overlaps [1, 3], so they merge into [1, 5]; [6, 9] is unaffected.
#
# Constraints:
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2 and newInterval.length == 2
# 0 <= start <= end <= 10^5
# intervals is sorted by start in ascending order and is non-overlapping.

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
    def insert_interval_brute(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        pass

    def insert_interval_better(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        pass

    def insert_interval_optimal(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.insert_interval_optimal([[1, 3], [6, 9]], [2, 5]))
