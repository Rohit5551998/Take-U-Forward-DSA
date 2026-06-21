# QUESTION: Longest Word with All Prefixes
# Given a string array `nums` of length n, a string is called a COMPLETE
# string if every prefix of this string is also present in the array
# nums. Find the longest complete string in the array nums.
# If there are multiple strings with the same longest length, return the
# lexicographically smallest one. If no such complete string exists,
# return an empty string "".
#
# Examples:
# Example 1:
# Input: nums = ["n", "ni", "nin", "ninj", "ninja", "nile"]
# Output: "ninja"
# Explanation: Every prefix of "ninja" — "n", "ni", "nin", "ninj",
# "ninja" — is present in the array.
#
# Example 2:
# Input: nums = ["a", "bb", "ab", "abc"]
# Output: ""
# Explanation: "abc" needs "ab" (yes) and "a" (yes) but also needs
# itself — actually it has all its prefixes ("a","ab","abc")? "a" is in
# array, "ab" is in array, "abc" is itself; let me recheck — yes "abc"
# is complete. Note: this example varies by source; the canonical
# Striver example uses an array where no complete string exists, in
# which case "" is returned.
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= nums[i].length <= 50
# nums[i] consists of lowercase English letters.
#
# Approach: Build a Trie of all strings in nums. Then DFS the Trie: a
# string is a candidate complete string only if every node along its
# path is marked as "end of a word" (meaning that prefix exists in nums).
# Track the longest such complete word; ties broken lexicographically.


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


def longest_word_with_all_prefixes_brute() -> None:
    pass


def longest_word_with_all_prefixes_better() -> None:
    pass


def longest_word_with_all_prefixes_optimal() -> None:
    pass
