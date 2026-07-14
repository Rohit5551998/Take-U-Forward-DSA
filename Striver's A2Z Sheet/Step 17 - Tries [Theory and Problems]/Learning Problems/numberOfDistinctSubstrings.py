# mypy: disable-error-code="empty-body"
# QUESTION: Number of Distinct Substrings in a String
# Given a string of length "n" of lowercase alphabet characters, count the total
# number of distinct substrings of the string (including the empty substring, or
# excluding it depending on the variant; here we count non-empty distinct
# substrings and may add 1 for the empty string).
#
# Example 1:
# Input: s = "ababa"
# Output: 10
# Explanation: The distinct non-empty substrings are:
#   "a","b","ab","ba","aba","bab","abab","baba","ababa","abab"... i.e. the set of
#   all unique substrings has size 10 (plus 1 for empty string if counted).
#
# Example 2:
# Input: s = "ccfdf"
# Output: 14
#
# Constraints:
# - 1 <= n <= 10^3
# - s consists only of lowercase English letters.

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
    def countDistinctSubstrings_brute(self, s: str) -> int:
        pass

    def countDistinctSubstrings_better(self, s: str) -> int:
        pass

    def countDistinctSubstrings_optimal(self, s: str) -> int:
        pass


if __name__ == "__main__":
    # sol = Solution()
    # print(sol.countDistinctSubstrings_optimal("ababa"))
    pass
