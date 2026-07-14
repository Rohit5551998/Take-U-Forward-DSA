# mypy: disable-error-code="empty-body"
# QUESTION: Rabin-Karp String Matching Algorithm
# Given a text string and a pattern string, find all starting indices in the text
# where the pattern occurs. The Rabin-Karp algorithm uses a rolling polynomial
# hash: it computes the hash of the pattern and the hash of every window of the
# text with the pattern's length, sliding the window in O(1) per step. When the
# window hash matches the pattern hash, the characters are compared directly to
# confirm the match (guarding against hash collisions).
# Example 1:
# Input: text = "abxabcabcaby", pattern = "abcaby"
# Output: [6]
# Explanation: The pattern "abcaby" occurs in the text starting at index 6.
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
    def rabin_karp_brute(self, text: str, pattern: str) -> List[int]:
        pass

    def rabin_karp_better(self, text: str, pattern: str) -> List[int]:
        pass

    def rabin_karp_optimal(self, text: str, pattern: str) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.rabin_karp_optimal("abxabcabcaby", "abcaby"))
