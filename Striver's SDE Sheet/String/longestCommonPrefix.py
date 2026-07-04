# mypy: disable-error-code="empty-body"
# QUESTION: Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Examples:
# Example 1
# Input: str = ["flower", "flow", "flight"]
# Output: "fl"
# Explanation: All strings in the array begin with the common prefix "fl".
#
# Example 2
# Input: str = ["apple", "banana", "grape", "mango"]
# Output: ""
# Explanation: None of the strings share a common starting sequence, so the result is an
# empty string.


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
    def longest_common_prefix_brute(self, strs: List[str]) -> str:
        pass

    def longest_common_prefix_better(self, strs: List[str]) -> str:
        pass

    def longest_common_prefix_optimal(self, strs: List[str]) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    strs = ["flower", "flow", "flight"]
    print(sol.longest_common_prefix_optimal(strs))
