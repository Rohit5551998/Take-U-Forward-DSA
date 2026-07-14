# mypy: disable-error-code="empty-body"
# QUESTION: Combination Sum II
# Given a collection of candidate numbers (may contain duplicates) and a target,
# find all unique combinations where the candidate numbers sum to target. Each
# number in candidates may be used at most once in a combination.
# The solution set must not contain duplicate combinations.
# Example 1:
# Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
# Example 2:
# Input: candidates = [2, 5, 2, 1, 2], target = 5
# Output: [[1, 2, 2], [5]]
# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30

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
    def combination_sum_ii_brute(self, candidates: List[int], target: int) -> List[List[int]]:
        pass

    def combination_sum_ii_better(self, candidates: List[int], target: int) -> List[List[int]]:
        pass

    def combination_sum_ii_optimal(self, candidates: List[int], target: int) -> List[List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.combination_sum_ii_optimal([10, 1, 2, 7, 6, 1, 5], 8))
