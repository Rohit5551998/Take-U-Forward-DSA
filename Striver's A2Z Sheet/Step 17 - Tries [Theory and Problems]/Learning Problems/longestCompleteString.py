# mypy: disable-error-code="empty-body"
# QUESTION: Longest String with All Prefixes (Complete String)
# A string is called "complete" if every prefix of that string is also present in
# the given array of strings. Given an array of "n" strings, find the longest
# complete string in the array. If multiple strings have the same longest length,
# return the lexicographically smallest one. If no such string exists, return "None".
#
# Example 1:
# Input: ["ab","abc","a","bp"]
# Output: "None"
# Explanation: For "abc", its prefix "ab" is present but for "bp", prefix "b" is
#   not present, so no complete string with all prefixes exists -> "None".
#
# Example 2:
# Input: ["ab","abc","a","bp","abcd"]
# Output: "abcd"
# Explanation: All prefixes of "abcd" ("a","ab","abc","abcd") are present in array.
#
# Constraints:
# - 1 <= n <= 10^5
# - 1 <= words[i].length <= 10^5
# - Strings consist only of lowercase English letters.

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
    def longestCompleteString_brute(self, words: List[str]) -> str:
        pass

    def longestCompleteString_better(self, words: List[str]) -> str:
        pass

    def longestCompleteString_optimal(self, words: List[str]) -> str:
        pass


if __name__ == "__main__":
    # sol = Solution()
    # print(sol.longestCompleteString_optimal(["ab", "abc", "a", "bp", "abcd"]))
    pass
