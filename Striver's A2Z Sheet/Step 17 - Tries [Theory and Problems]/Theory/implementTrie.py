# mypy: disable-error-code="empty-body"
# QUESTION: Implement Trie (Prefix Tree) - INSERT | SEARCH | STARTSWITH
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. Implement the Trie
# class:
# - Trie() Initializes the trie object.
# - void insert(String word) Inserts the string word into the trie.
# - boolean search(String word) Returns true if word is in the trie (i.e. was
#   inserted before), and false otherwise.
# - boolean startsWith(String prefix) Returns true if there is a previously
#   inserted string word that has the prefix prefix, and false otherwise.
#
# Example 1:
# Input:
#   ["Trie","insert","search","search","startsWith","insert","search"]
#   [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
# Output: [null, null, true, false, true, null, true]
# Explanation:
#   insert("apple"); search("apple") -> True; search("app") -> False;
#   startsWith("app") -> True; insert("app"); search("app") -> True
#
# Constraints:
# - 1 <= word.length, prefix.length <= 2000
# - word and prefix consist only of lowercase English letters.
# - At most 3 * 10^4 calls in total will be made to insert, search, startsWith.

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


class Node:
    def __init__(self) -> None:
        pass


class Trie:
    def __init__(self) -> None:
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


if __name__ == "__main__":
    # trie = Trie()
    # trie.insert("apple")
    # print(trie.search("apple"))
    # print(trie.search("app"))
    # print(trie.startsWith("app"))
    pass
