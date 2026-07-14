# mypy: disable-error-code="empty-body"
# QUESTION: Minimum Window Subsequence
# Given strings s1 and s2, return the minimum (contiguous) substring W of s1 such
# that s2 is a SUBSEQUENCE of W. (Order of s2's characters must be preserved, but
# they need not be contiguous inside W.)
# If there is no such window, return the empty string "". If there are multiple
# minimum-length windows, return the one with the left-most starting index.
#
# Example 1:
# Input: s1 = "abcdebdde", s2 = "bde"
# Output: "bcde"
# Explanation: "bcde" is the shortest substring of s1 containing "bde" as a
# subsequence. "deb" is not shorter and "bde" appears out of order, so "bcde" wins.
#
# Example 2:
# Input: s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl", s2 = "u"
# Output: ""
#
# Constraints:
# 1 <= s1.length <= 2 * 10^4
# 1 <= s2.length <= 100
# s1 and s2 consist of lowercase English letters.

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
    def minWindowSubsequence_brute(self, s1: str, s2: str) -> str:
        pass

    def minWindowSubsequence_better(self, s1: str, s2: str) -> str:
        pass

    def minWindowSubsequence_optimal(self, s1: str, s2: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.minWindowSubsequence_optimal("abcdebdde", "bde"))  # "bcde"
