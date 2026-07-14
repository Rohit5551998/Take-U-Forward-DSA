# mypy: disable-error-code="empty-body"
# QUESTION: Implement Trie - II (Prefix Tree)
# Implement a data structure "Trie" to store and count strings. It should support
# the following operations:
# - insert(word): Inserts the string word into the Trie.
# - countWordsEqualTo(word): Returns the number of instances of the string word
#   present in the Trie.
# - countWordsStartingWith(prefix): Returns the number of strings in the Trie whose
#   prefix matches the given prefix.
# - erase(word): Deletes one occurrence of the string word from the Trie.
#
# Example 1:
# Input:
#   insert("apple"); insert("apple"); insert("apps");
#   countWordsEqualTo("apple"); countWordsStartingWith("app");
#   erase("apple"); countWordsEqualTo("apple")
# Output: 2, 3, 1
# Explanation: "apple" inserted twice -> countWordsEqualTo=2. Prefix "app" matches
#   3 inserted words. After erasing one "apple", countWordsEqualTo("apple")=1.
#
# Constraints:
# - 1 <= word.length, prefix.length <= 1000
# - word and prefix consist only of lowercase English letters.
# - erase(word) is only called on words already present in the Trie.

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

    def countWordsEqualTo(self, word: str) -> int:
        pass

    def countWordsStartingWith(self, prefix: str) -> int:
        pass

    def erase(self, word: str) -> None:
        pass


if __name__ == "__main__":
    # trie = Trie()
    # trie.insert("apple")
    # trie.insert("apple")
    # trie.insert("apps")
    # print(trie.countWordsEqualTo("apple"))
    # print(trie.countWordsStartingWith("app"))
    # trie.erase("apple")
    # print(trie.countWordsEqualTo("apple"))
    pass
