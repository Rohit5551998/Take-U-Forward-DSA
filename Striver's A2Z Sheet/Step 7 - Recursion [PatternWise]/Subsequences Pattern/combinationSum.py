# mypy: disable-error-code="empty-body"
# QUESTION: Combination Sum
# Given an array of distinct integers candidates and a target integer, return a
# list of all unique combinations of candidates where the chosen numbers sum to
# target. The same number may be chosen an unlimited number of times.
# Two combinations are unique if the frequency of at least one number differs.
# Example 1:
# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]
# Example 2:
# Input: candidates = [2, 3, 5], target = 8
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements are distinct.
# 1 <= target <= 40

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
    def combination_sum_brute(self, candidates: List[int], target: int) -> List[List[int]]:
        pass

    def combination_sum_better(self, candidates: List[int], target: int) -> List[List[int]]:
        pass

    def combination_sum_optimal(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.combination_sum_optimal([2, 3, 6, 7], 7))
