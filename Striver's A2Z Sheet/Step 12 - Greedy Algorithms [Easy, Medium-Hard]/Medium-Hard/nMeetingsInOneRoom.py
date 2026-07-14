# mypy: disable-error-code="empty-body"
# QUESTION: N Meetings in One Room
# There is one meeting room. Given N meetings with start times start[i] and end times
# end[i], find the maximum number of meetings that can be held in the room such that
# only one meeting can happen at a time (a meeting must fully end before the next begins).
# Return the maximum number of non-overlapping meetings.
#
# Example 1:
# Input: start = [1, 3, 0, 5, 8, 5], end = [2, 4, 6, 7, 9, 9]
# Output: 4
# Explanation: Choose meetings (1-2), (3-4), (5-7), (8-9) for a total of 4 meetings.
#
# Constraints:
# 1 <= N <= 10^5
# 0 <= start[i] < end[i] <= 10^9

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
    def n_meetings_brute(self, start: List[int], end: List[int]) -> int:
        pass

    def n_meetings_better(self, start: List[int], end: List[int]) -> int:
        pass

    def n_meetings_optimal(self, start: List[int], end: List[int]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.n_meetings_optimal([1, 3, 0, 5, 8, 5], [2, 4, 6, 7, 9, 9]))
