# mypy: disable-error-code="empty-body"
# QUESTION: Word Break
# Given a string s and a dictionary of strings wordDict, return true if
# s can be segmented into a space-separated sequence of one or more
# dictionary words; otherwise return false.
# Note: The same word in the dictionary can be used multiple times in
# the segmentation.
#
# Examples:
# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: "leetcode" can be segmented as "leet code".
#
# Example 2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: "apple pen apple" — "apple" reused.
#
# Example 3:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
# Constraints:
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.


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
    def word_break_brute(self, s: str, word_dict: List[str]) -> bool:
        pass

    def word_break_better(self, s: str, word_dict: List[str]) -> bool:
        pass

    def word_break_optimal(self, s: str, word_dict: List[str]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    word_dict = ["leet", "code"]
    print(sol.word_break_optimal(s, word_dict))
