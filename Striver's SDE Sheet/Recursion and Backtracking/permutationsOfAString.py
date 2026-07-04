# mypy: disable-error-code="empty-body"
# QUESTION: Permutations of a String
# Given an array arr of distinct integers, print all possible permutations of the given array.
# A permutation is an arrangement of all the elements of the array into some sequence or order.
# An array of n distinct elements has exactly n! permutations. Return the permutations in any
# order.
#
# Examples:
# Example 1:
# Input: arr = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Explanation: There are 3! = 6 permutations of the 3 distinct elements, and all of them are
# listed.
#
# Example 2:
# Input: arr = [0, 1]
# Output: [[0, 1], [1, 0]]
# Explanation: The 2 distinct elements can be arranged in 2! = 2 different ways.


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
    def permutations_of_a_string_brute(self, nums: List[int]) -> List[List[int]]:
        pass

    def permutations_of_a_string_better(self, nums: List[int]) -> List[List[int]]:
        pass

    def permutations_of_a_string_optimal(self, nums: List[int]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permutations_of_a_string_optimal(nums))
