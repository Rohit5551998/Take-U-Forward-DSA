# mypy: disable-error-code="empty-body"
# QUESTION: Longest Palindrome in a string
# Given a string s, return the longest palindromic substring in s. A palindromic substring is a
# contiguous sequence of characters within the string that reads the same forward and backward.
# If multiple palindromic substrings share the maximum length, any one of them may be returned.
#
# Examples:
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "bab" is a palindrome of length 3, the maximum possible; "aba" is an equally
# valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# Explanation: The longest palindromic substring is "bb", of length 2.
#
# Constraints:
# - 1 <= s.length <= 1000
# - s consists of digits and English letters


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
    def longest_palindrome_in_a_string_brute(self, s: str) -> str:
        pass

    def longest_palindrome_in_a_string_better(self, s: str) -> str:
        pass

    def longest_palindrome_in_a_string_optimal(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "babad"
    print(sol.longest_palindrome_in_a_string_optimal(s))
