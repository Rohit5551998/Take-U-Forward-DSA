# mypy: disable-error-code="empty-body"
# QUESTION: Rabin Karp Algorithm
# Given a string text and a string pattern, implement the Rabin-Karp algorithm to find the
# starting index of all occurrences of pattern in text. If pattern is not found, return an
# empty list.
#
# Examples:
# Example 1:
# Input: text = "ababcabcababc", pattern = "abc"
# Output: [2, 5, 10]
# Explanation: The pattern "abc" is found at indices 2, 5, and 10 in the text.
#
# Example 2:
# Input: text = "hello", pattern = "ll"
# Output: [2]
# Explanation: The pattern "ll" is found at index 2 in the text.
#
# Constraints:
# - 1 <= text.length, pattern.length <= 5*10^4


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
    def rabin_karp_algorithm_brute(self, text: str, pattern: str) -> List[int]:
        pass

    def rabin_karp_algorithm_better(self, text: str, pattern: str) -> List[int]:
        pass

    def rabin_karp_algorithm_optimal(self, text: str, pattern: str) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    text = "ababcabcababc"
    pattern = "abc"
    print(sol.rabin_karp_algorithm_optimal(text, pattern))
