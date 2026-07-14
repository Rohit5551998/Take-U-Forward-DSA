# mypy: disable-error-code="empty-body"
# QUESTION: Word Ladder I
# Given two words beginWord and endWord, and a dictionary wordList, return the
# length of the shortest transformation sequence from beginWord to endWord, such
# that:
#   - Only one letter can be changed at a time.
#   - Each transformed word must exist in wordList. (beginWord itself need not be
#     in wordList.)
# Return the number of words in the shortest transformation sequence (including
# both beginWord and endWord). If no such sequence exists, return 0.
# All words have the same length and consist of lowercase English letters.
#
# Example 1:
# Input:
#   beginWord = "hit", endWord = "cog"
#   wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: One shortest transformation is
#   "hit" -> "hot" -> "dot" -> "dog" -> "cog", which is 5 words long.
#
# Constraints:
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
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
    def word_ladder_i_brute(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass

    def word_ladder_i_better(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass

    def word_ladder_i_optimal(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.word_ladder_i_optimal(
    #     "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    # )
