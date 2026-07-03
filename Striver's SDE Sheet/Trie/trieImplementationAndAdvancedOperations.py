# QUESTION: Trie Implementation and Advanced Operations
# Implement "TRIE" data structure from scratch with the following functions.
# - Trie(): Initialize the object of this "TRIE" data structure.
# - insert("WORD"): Insert the string "WORD" into this "TRIE" data structure.
# - countWordsEqualTo("WORD"): Return how many times this "WORD" is present in this "TRIE".
# - countWordsStartingWith("PREFIX"): Return how many words are there in this "TRIE" that have
#   the string "PREFIX" as a prefix.
# - erase("WORD"): Delete one occurrence of the string "WORD" from the "TRIE".
#
# Examples:
# Example 1:
# Input:
# ["Trie", "insert", "countWordsEqualTo", "insert", "countWordsStartingWith", "erase",
#  "countWordsStartingWith"]
# ["apple", "apple", "app", "app", "apple", "app"]
# Output: [null, null, 1, null, 2, null, 1]
# Explanation:
# Trie trie = new Trie()
# trie.insert("apple")
# trie.countWordsEqualTo("apple")      // return 1
# trie.insert("app")
# trie.countWordsStartingWith("app")   // return 2
# trie.erase("apple")
# trie.countWordsStartingWith("app")   // return 1
#
# Example 2:
# Input:
# ["Trie", "insert", "countWordsEqualTo", "insert", "erase", "countWordsStartingWith"]
# ["mango", "apple", "app", "app", "mango"]
# Output: [null, null, 0, null, null, 1]
# Explanation:
# Trie trie = new Trie()
# trie.insert("mango")
# trie.countWordsEqualTo("apple")      // return 0
# trie.insert("app")
# trie.erase("app")
# trie.countWordsStartingWith("mango") // return 1
#
# Constraints:
# - 1 <= word.length, prefix.length <= 2000
# - word and prefix consist only of lowercase English letters.
# - At most 3*10^4 calls in total will be made to insert, countWordsEqualTo,
#   countWordsStartingWith and erase.


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


class Solution:
    def trie_implementation_and_advanced_operations_brute(self) -> None:
        pass

    def trie_implementation_and_advanced_operations_better(self) -> None:
        pass

    def trie_implementation_and_advanced_operations_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
