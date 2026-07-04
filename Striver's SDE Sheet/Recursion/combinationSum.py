# mypy: disable-error-code="empty-body"
# QUESTION: Combination Sum
# Given an array of distinct integers `candidates` and a target integer
# `target`, return a list of all unique combinations of `candidates`
# where the chosen numbers sum to `target`. You may return the
# combinations in any order.
# The SAME number may be chosen from `candidates` an UNLIMITED number of
# times. Two combinations are unique if the frequency of at least one of
# the chosen numbers is different.
# The test cases are generated such that the number of unique
# combinations that sum up to `target` is less than 150 combinations.
#
# Examples:
# Example 1:
# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]
# Explanation: 2 + 2 + 3 = 7. 7 is itself a candidate.
#
# Example 2:
# Input: candidates = [2, 3, 5], target = 8
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
#
# Example 3:
# Input: candidates = [2], target = 1
# Output: []
#
# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
#
# Examples:
# Example 1:
# Input: array = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#  7 is a candidate, and 7 = 7.
#  These are the only two combinations.
#
# Example 2:
# Input: array = [2], target = 1
# Output: []
# Explaination: No combination is possible.


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


if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(sol.combination_sum_optimal(candidates, target))
