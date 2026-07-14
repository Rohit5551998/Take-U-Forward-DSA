# mypy: disable-error-code="empty-body"
# QUESTION: Longest Happy Prefix
# A string is called a happy prefix if it is a non-empty prefix that is also a
# suffix (excluding the whole string itself). Given a string s, return the longest
# happy prefix of s. If no such prefix exists, return an empty string.
# Example 1:
# Input: s = "level"
# Output: "l"
# Explanation: "l" is the longest string that is both a proper prefix and a
# proper suffix of "level".
# Example 2:
# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the longest proper prefix that is also a suffix.
# Constraints:
# 1 <= s.length <= 10^5
# s contains only lowercase English letters.

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
    def longest_happy_prefix_brute(self, s: str) -> str:
        pass

    def longest_happy_prefix_better(self, s: str) -> str:
        pass

    def longest_happy_prefix_optimal(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.longest_happy_prefix_optimal("ababab"))
