# mypy: disable-error-code="empty-body"
# QUESTION: Longest common subsequence
# Given two strings str1 and str2, print the longest common subsequence
# of the two strings. A subsequence of a string is a list of characters of
# the string where zero or more characters in the original string are
# deleted without disturbing the relative ordering of the remaining
# characters. If multiple LCS exist, return any one. If no common
# subsequence exists, return "".
#
# Examples:
# Example 1:
# Input: str1 = "abcd", str2 = "bdef"
# Output: "bd"
#
# Example 2:
# Input: str1 = "apple", str2 = "waffle"
# Output: "ale"
#
# Examples:
# Input: str1 = "abcd", str2="bdef"
# Output: "bd"
# Explanation: LCS of two strings is "bd".
#
# Input: str1 = "apple" str2 = "waffle"
# Output: "ale"
# Explanation: LCS of two strings is "ale".


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


class Solution:
    def longest_common_subsequence_brute(self, str1: str, str2: str) -> str:
        pass

    def longest_common_subsequence_better(self, str1: str, str2: str) -> str:
        pass

    def longest_common_subsequence_optimal(self, str1: str, str2: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    str1 = "abcd"
    str2 = "bdef"
    print(sol.longest_common_subsequence_optimal(str1, str2))
