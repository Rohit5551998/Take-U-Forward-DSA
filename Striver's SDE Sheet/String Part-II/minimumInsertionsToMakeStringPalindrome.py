# QUESTION: Minimum insertions to make string palindrome
# Given a string s, find the minimum number of insertions needed to make
# it a palindrome. A palindrome is a sequence that reads the same
# backward as forward. You can insert characters at ANY position in the
# string (not just at the ends).
#
# Examples:
# Example 1:
# Input: s = "zzazz"
# Output: 0
# Explanation: It's already a palindrome.
#
# Example 2:
# Input: s = "mbadm"
# Output: 2
# Explanation: "mbdadbm" or "mdbabdm" — both require 2 insertions.
#
# Example 3:
# Input: s = "leetcode"
# Output: 5
# Explanation: Insert 5 characters to form "leetcodocteel".
#
# Constraints:
# 1 <= s.length <= 500
# s consists of lowercase English letters.
#
# Approach: This problem reduces to (n - LPS), where LPS is the length
# of the Longest Palindromic Subsequence of s. LPS = LCS(s, reverse(s)).
#
# Examples:
# Input: s = "abcaa"
# Output: 2
# Explanation: Insert 2 characters "c", and "b" to make "abcacba", which is a palindrome.
#
# Input : s = "ba"
# Output: 1
# Explanation : Insert "a" at the beginning to make "aba", which is a palindrome.


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


def minimum_insertions_to_make_string_palindrome_brute() -> None:
    pass


def minimum_insertions_to_make_string_palindrome_better() -> None:
    pass


def minimum_insertions_to_make_string_palindrome_optimal() -> None:
    pass
