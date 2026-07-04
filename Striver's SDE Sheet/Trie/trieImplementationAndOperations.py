# mypy: disable-error-code="empty-body"
# QUESTION: Trie Implementation and Operations
# Implement the Trie class:
# - Trie(): Initializes the trie object.
# - void insert(String word): Inserts the string word into the trie.
# - boolean search(String word): Returns true if the string word is in the trie (i.e., was
#   inserted before), and false otherwise.
# - boolean startsWith(String prefix): Returns true if there is a previously inserted string
#   word that has the prefix prefix, and false otherwise.
#
# Examples:
# Example 1:
# Input:
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [ [], "apple", "apple", "app", "app", "app", "app" ]
# Output: [null, null, true, false, true, null, true]
# Explanation:
# Trie trie = new Trie()
# trie.insert("apple")
# trie.search("apple")   // return True
# trie.search("app")     // return False
# trie.startsWith("app") // return True
# trie.insert("app")
# trie.search("app")     // return True
#
# Example 2:
# Input:
# ["Trie", "insert", "insert", "startsWith", "search"]
# [ [], "takeu", "banana", "bana", "takeu" ]
# Output: [null, null, null, true, true]
# Explanation:
# Trie trie = new Trie()
# trie.insert("takeu")
# trie.insert("banana")
# trie.startsWith("bana") // return True
# trie.search("takeu")    // return True
#
# Constraints:
# - 1 <= word.length, prefix.length <= 2000
# - word and prefix consist only of lowercase English letters.
# - At most 3*10^4 calls in total will be made to insert, search and startsWith.


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


class Trie:
    def __init__(self) -> None:
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def starts_with(self, prefix: str) -> bool:
        pass


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.starts_with("app"))
    trie.insert("app")
    print(trie.search("app"))
