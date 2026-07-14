# mypy: disable-error-code="empty-body"
# QUESTION: Alien Dictionary
# There is a new alien language that uses the lowercase English alphabet, but the
# order among the letters is unknown to you. You are given a list of words from
# the alien language's dictionary, where the words are sorted lexicographically by
# the rules of this new language (K distinct letters are used).
# Derive the order of letters in this language and return it as a string. If a
# valid order exists, return any one of them. If there is no valid ordering
# (the given words contradict a valid ordering, e.g. a prefix appears after the
# longer word), return an empty string.
#
# Example 1:
# Input: words = ["baa", "abcd", "abca", "cab", "cad"], K = 4
# Output: "bdac"
# Explanation: Comparing adjacent words yields b < a (from "baa" vs "abcd"),
# d < a (from "abcd" vs "abca"), b < c (from "abca" vs "cab") and b < d
# (from "cab" vs "cad"). A topological order of {a, b, c, d} consistent with
# these constraints is "bdac".
#
# Constraints:
# 1 <= len(words) <= 300
# 1 <= len(words[i]) <= 300
# words[i] consists of the first K lowercase English letters.
# 1 <= K <= 26

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
    def alien_dictionary_brute(self, words: List[str], K: int) -> str:
        pass

    def alien_dictionary_better(self, words: List[str], K: int) -> str:
        pass

    def alien_dictionary_optimal(self, words: List[str], K: int) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.alien_dictionary_optimal(["baa", "abcd", "abca", "cab", "cad"], 4)
