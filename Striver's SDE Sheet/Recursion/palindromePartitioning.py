# mypy: disable-error-code="empty-body"
# QUESTION: Palindrome partitioning
# Given a string s, partition string s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitions of string s.
#
# Examples:
# Example 1:
# Input: s = "aabaa"
# Output: [["a", "a", "b", "a", "a"], ["a", "a", "b", "aa"], ["a", "aba", "a"],
#          ["aa", "b", "a", "a"], ["aa", "b", "aa"], ["aabaa"]]
# Explanation: Above are all the possible ways in which the string can be partitioned so that
# each substring is a palindrome.
#
# Example 2:
# Input: s = "baa"
# Output: [["b", "a", "a"], ["b", "aa"]]
# Explanation: Above are all the possible ways in which the string can be partitioned so that
# each substring is a palindrome.
#
# Constraints:
# 1 <= s.length <= 16
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

from typing import List


class Solution:
    def palindrome_partitioning_brute(self, s: str) -> List[List[str]]:
        pass

    def palindrome_partitioning_better(self, s: str) -> List[List[str]]:
        pass

    def palindrome_partitioning_optimal(self, s: str) -> List[List[str]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "aabaa"
    print(sol.palindrome_partitioning_optimal(s))
