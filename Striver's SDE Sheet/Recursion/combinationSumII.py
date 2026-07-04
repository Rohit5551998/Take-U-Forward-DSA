# mypy: disable-error-code="empty-body"
# QUESTION: Combination Sum II
# Given a collection of candidate numbers (candidates) and an integer target, find all unique
# combinations in candidates where the sum is equal to the target. There can only be one usage
# of each number in a candidates combination, and return the answer in sorted order.
# e.g.: The combinations [1, 1, 2] and [1, 2, 1] are not unique.
#
# Examples:
# Example 1:
# Input: candidates = [2, 1, 2, 7, 6, 1, 5], target = 8
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
# Explanation: The combinations that sum up to target are
# 1 + 1 + 6 => 8; 1 + 2 + 5 => 8; 1 + 7 => 8; 2 + 6 => 8.
#
# Example 2:
# Input: candidates = [2, 5, 2, 1, 2], target = 5
# Output: [[1, 2, 2], [5]]
# Explanation: The combinations that sum up to target are 1 + 2 + 2 => 5; 5 => 5.
#
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


if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 1, 2, 7, 6, 1, 5]
    target = 8
    print(sol.combination_sum_ii_optimal(candidates, target))
