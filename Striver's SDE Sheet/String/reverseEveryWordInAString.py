# mypy: disable-error-code="empty-body"
# QUESTION: Reverse every word in a string
# Given an input string, containing upper-case and lower-case letters, digits, and spaces (' ').
# A word is defined as a sequence of non-space characters. The words in s are separated by at
# least one space. Return a string with the words in reverse order, concatenated by a single
# space.
#
# Examples:
# Example 1:
# Input: s = "welcome to the jungle"
# Output: "jungle the to welcome"
# Explanation: The words in the input string are "welcome", "to", "the", and "jungle". Reversing
# the order of these words gives "jungle", "the", "to", and "welcome". The output string should
# have exactly one space between each word.
#
# Example 2:
# Input: s = " amazing coding skills "
# Output: "skills coding amazing"
# Explanation: The input string has leading and trailing spaces, as well as multiple spaces
# between the words "amazing", "coding", and "skills". After trimming the leading and trailing
# spaces and reducing the multiple spaces between words to a single space, the words are
# "amazing", "coding", and "skills". Reversing the order of these words gives "skills",
# "coding", and "amazing". The output string should not have any leading or trailing spaces and
# should have exactly one space between each word.
#
# Constraints:
# - 1 <= s.length <= 10^4
# - s contains English letters (upper-case and lower-case), digits, and spaces ' '.
# - There is at least one word in s.


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
    def reverse_every_word_in_a_string_brute(self, s: str) -> str:
        pass

    def reverse_every_word_in_a_string_better(self, s: str) -> str:
        pass

    def reverse_every_word_in_a_string_optimal(self, s: str) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "welcome to the jungle"
    print(sol.reverse_every_word_in_a_string_optimal(s))
