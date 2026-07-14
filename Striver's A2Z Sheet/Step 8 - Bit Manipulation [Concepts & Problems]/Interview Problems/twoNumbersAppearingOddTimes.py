# mypy: disable-error-code="empty-body"
# QUESTION: Find the two numbers appearing an odd number of times
# Given an array of integers where every element appears an even number of times
# except for exactly two elements that each appear an odd number of times, find
# those two elements. Return them (order does not matter).
# Example 1:
# Input: nums = [1, 2, 3, 2, 1, 4]
# Output: [3, 4]
# Explanation: 1 and 2 appear twice each; 3 and 4 appear once each (odd).
# Example 2:
# Input: nums = [4, 2, 4, 10, 2, 3]
# Output: [10, 3]
# Explanation: 4 and 2 appear twice each; 10 and 3 appear once each (odd).
# Constraints:
# 2 <= len(nums) <= 10^5
# Exactly two elements appear an odd number of times.

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
    def twoOddOccurrences_brute(self, nums: List[int]) -> List[int]:
        pass

    def twoOddOccurrences_better(self, nums: List[int]) -> List[int]:
        pass

    def twoOddOccurrences_optimal(self, nums: List[int]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.twoOddOccurrences_optimal([1, 2, 3, 2, 1, 4]))
