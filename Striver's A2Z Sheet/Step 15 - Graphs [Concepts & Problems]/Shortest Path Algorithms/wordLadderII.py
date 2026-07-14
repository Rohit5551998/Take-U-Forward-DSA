# mypy: disable-error-code="empty-body"
# QUESTION: Word Ladder II
# Given two words beginWord and endWord, and a dictionary wordList, return all the
# shortest transformation sequences from beginWord to endWord, such that:
#   - Only one letter can be changed at a time.
#   - Each transformed word must exist in wordList. (beginWord need not be in it.)
# Each returned sequence is a list of words [beginWord, ..., endWord]. If there is
# no valid transformation sequence, return an empty list.
# All words have the same length and consist of lowercase English letters.
#
# Example 1:
# Input:
#   beginWord = "hit", endWord = "cog"
#   wordList = ["hot","dot","dog","lot","log","cog"]
# Output:
#   [["hit","hot","dot","dog","cog"],
#    ["hit","hot","lot","log","cog"]]
# Explanation: There are two shortest transformation sequences of length 5.
#
# Constraints:
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# All words consist of lowercase English letters.
# beginWord != endWord; all words in wordList are unique.

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
    def word_ladder_ii_brute(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        pass

    def word_ladder_ii_better(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        pass

    def word_ladder_ii_optimal(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.word_ladder_ii_optimal(
    #     "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    # )
