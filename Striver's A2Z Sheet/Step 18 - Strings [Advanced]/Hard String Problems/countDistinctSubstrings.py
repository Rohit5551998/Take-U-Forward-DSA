# mypy: disable-error-code="empty-body"
# QUESTION: Count Distinct Substrings (using Trie/Hashing)
# Given a string s, count the number of distinct (unique) non-empty substrings of
# s. Two substrings are considered the same if they consist of the same sequence
# of characters. This can be solved by inserting every suffix of s into a Trie and
# counting the total number of nodes created (each node represents one distinct
# substring), or by using string hashing to deduplicate substrings.
# Example 1:
# Input: s = "ababa"
# Output: 10
# Explanation: The distinct substrings are: "a", "b", "ab", "ba", "aba", "bab",
# "abab", "baba", "ababa" and "abab"/"aba" counted once each -> 10 unique
# substrings in total.
# Example 2:
# Input: s = "aaa"
# Output: 3
# Explanation: The distinct substrings are "a", "aa" and "aaa".
# Constraints:
# 1 <= s.length <= 10^3
# s consists of lowercase English letters.

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
    def count_distinct_substrings_brute(self, s: str) -> int:
        pass

    def count_distinct_substrings_better(self, s: str) -> int:
        pass

    def count_distinct_substrings_optimal(self, s: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.count_distinct_substrings_optimal("ababa"))
