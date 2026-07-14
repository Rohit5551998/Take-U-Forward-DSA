# mypy: disable-error-code="empty-body"
# QUESTION: Minimum Multiplications to Reach End
# Given a start integer, an end integer, and an array arr of integers, at each step
# you may multiply the current number by any element of arr and take the result
# modulo 100000 (i.e. new = (current * arr[i]) % 100000). Starting from start,
# find the minimum number of multiplication steps needed to reach end. If it is not
# possible to reach end, return -1.
#
# Example 1:
# Input:
#   arr = [2, 5, 7], start = 3, end = 30
# Output: 2
# Explanation: 3 * 2 = 6, then 6 * 5 = 30. So 2 multiplications are enough.
#
# Constraints:
# 1 <= arr.length <= 10^4
# 1 <= arr[i] <= 10^4
# 0 <= start, end < 100000
# All arithmetic is performed modulo 100000.

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
    def minimum_multiplications_to_reach_end_brute(
        self, arr: List[int], start: int, end: int
    ) -> int:
        pass

    def minimum_multiplications_to_reach_end_better(
        self, arr: List[int], start: int, end: int
    ) -> int:
        pass

    def minimum_multiplications_to_reach_end_optimal(
        self, arr: List[int], start: int, end: int
    ) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.minimum_multiplications_to_reach_end_optimal([2, 5, 7], 3, 30)
