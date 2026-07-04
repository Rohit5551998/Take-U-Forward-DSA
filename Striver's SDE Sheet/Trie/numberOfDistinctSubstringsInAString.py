# mypy: disable-error-code="empty-body"
# QUESTION: Number of distinct substrings in a string
# Implement a program that takes a string 'S' as input and returns the number of distinct
# substrings of the given string, including the empty substring. Use a trie data structure.
#
# Examples:
# Input: s = "aba"
# Output: 6
# Explanation: The distinct substrings are "a", "ab", "ba", "b", "aba", "".
#
# Input: s = "abc"
# Output: 7
# Explanation: The distinct substrings are "a", "ab", "abc", "b", "bc", "c", "".


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
    def number_of_distinct_substrings_in_a_string_brute(self, s: str) -> int:
        pass

    def number_of_distinct_substrings_in_a_string_better(self, s: str) -> int:
        pass

    def number_of_distinct_substrings_in_a_string_optimal(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "aba"
    print(sol.number_of_distinct_substrings_in_a_string_optimal(s))
