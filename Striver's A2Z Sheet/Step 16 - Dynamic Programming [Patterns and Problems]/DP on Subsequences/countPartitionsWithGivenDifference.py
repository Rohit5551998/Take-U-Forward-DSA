# mypy: disable-error-code="empty-body"
# QUESTION: Count Partitions With Given Difference
# Partition the array into S1, S2 (sum(S1) >= sum(S2)) with
# sum(S1)-sum(S2) = d. Count such partitions, modulo 1e9+7.
#
# Example 1:
# Input: nums = [5,2,6,4], d = 3
# Output: 1
#
# Constraints:
# 1 <= n <= 100
# 0 <= nums[i] <= 1000

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
    def count_partitions_diff_brute(self, nums: List[int], d: int) -> int:
        pass

    def count_partitions_diff_better(self, nums: List[int], d: int) -> int:
        pass

    def count_partitions_diff_optimal(self, nums: List[int], d: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.count_partitions_diff_optimal([5, 2, 6, 4], 3)
