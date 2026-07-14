# mypy: disable-error-code="empty-body"
# QUESTION: KMP Algorithm / LPS (pi) Array
# The Knuth-Morris-Pratt (KMP) algorithm finds all occurrences of a pattern in a
# text in O(n + m) time. Its core is the LPS array (also called the prefix
# function or pi array): for each prefix of the pattern, lps[i] is the length of
# the longest proper prefix of pattern[0..i] that is also a suffix of it. During
# matching, on a mismatch the LPS array tells us how far to shift the pattern
# without re-examining already matched characters. Given a text and a pattern,
# return all starting indices where the pattern occurs in the text.
# Example 1:
# Input: text = "ababcababcabc", pattern = "ababc"
# Output: [0, 5]
# Explanation: The pattern "ababc" occurs starting at indices 0 and 5.
# Example 2:
# Input: text = "aaaaa", pattern = "aa"
# Output: [0, 1, 2, 3]
# Constraints:
# 1 <= pattern.length <= text.length <= 10^5
# text and pattern consist of lowercase English letters.

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
    def kmp_search_brute(self, text: str, pattern: str) -> List[int]:
        pass

    def kmp_search_better(self, text: str, pattern: str) -> List[int]:
        pass

    def kmp_search_optimal(self, text: str, pattern: str) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.kmp_search_optimal("ababcababcabc", "ababc"))
