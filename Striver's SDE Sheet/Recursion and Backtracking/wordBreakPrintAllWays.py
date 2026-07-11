# mypy: disable-error-code="empty-body"
# QUESTION: Word Break (print all ways)
# Given a string s and a dictionary of strings wordDict, return ALL
# possible sentences that can be formed by adding spaces in s such that
# each word in the resulting sentence is a valid dictionary word. Return
# all such possible sentences in any order.
# Note: The same word in the dictionary may be reused multiple times in
# the segmentation.
#
# Examples:
# Example 1:
# Input: s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output: ["cats and dog", "cat sand dog"]
#
# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output: ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
#
# Example 3:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: []
#
# Constraints:
# 1 <= s.length <= 20
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 10
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# Number of valid sentences does not exceed 10^5.
# Inputs are generated such that the answer is guaranteed to be at most
# 10^5 sentences.


"""
#Brute Force (break_possible_brute + break_words_brute + word_break_print_all_ways_brute):
1. Same shape as palindrome partitioning: decide "where does the FIRST word end?"
   then recurse on the remaining suffix. Each recursion level owns a start `index`.
2. Loop i from index to end. The candidate first word is s[index..i]; only take
   that cut if the substring is a dictionary word (break_possible_brute checks it).
3. If it's a valid word, append it to the running `substring` list and recurse
   from i+1 to segment the rest of the string the same way.
4. Backtrack: pop the word so the next i explores a different first-word length.
5. Base case: when index == len(s) the whole string has been consumed by valid
   words, so `substring` is one complete segmentation — append a COPY to ans.
6. ans holds each segmentation as a LIST of words; the driver joins each list with
   spaces at the end to produce the final sentence strings.
7. Why this is the BRUTE tier: break_possible_brute does `s[index:i+1] in word_dict`
   on a LIST, so every prefix test is O(d * L) — it scans the whole dict comparing
   each word. The optimal tier removes the d factor with a set.
TC -> O(2^n * n * d * L), SC -> O(2^n * n) output + O(n) recursion + O(n) substring
   (up to ~2^(n-1) segmentations, each O(n) to build; every prefix test is an
    O(d*L) list scan; n = len(s), d = dict size, L = max word length)

#Better Approach:
SKIPPED — no distinct middle tier. The list-scan brute goes straight to the
set-lookup optimal; nothing sensible sits between them.

#Optimal Approach (break_possible_optimal + break_words_optimal + word_break_print_all_ways_optimal):
1. Identical partition backtracking to the brute — the ONLY change is how the
   dictionary membership test is done.
2. Convert word_dict to a set once, up front (hashSet). This is a one-time O(d*L)
   build, paid a single time instead of on every prefix check.
3. Now break_possible_optimal does `s[index:i+1] in hashSet`, which hashes the
   substring and probes the set in O(L) — no scan of the dictionary. That drops
   the per-check cost from O(d*L) to O(L), removing the d factor entirely.
4. Everything else is unchanged: loop each prefix, recurse on the suffix when the
   prefix is a valid word, backtrack, and join word-lists with spaces at the end.
TC -> O(2^n * n * L) + O(d*L) one-time set build, SC -> O(2^n * n) output +
      O(d*L) set + O(n) recursion + O(n) substring
   (vs brute's O(2^n * n * d * L): the d factor on every prefix test is gone)

#KEY INSIGHT:
- The enumeration is inherently exponential and can't be beaten, but the constant
  work PER prefix test can: hashing the dictionary once turns each "is this a word?"
  check from an O(d*L) list scan into an O(L) set lookup, shaving the whole dict-size
  factor d off the running time for the price of O(d*L) extra space.
"""

from typing import List


class Solution:
    def break_possible_brute(self, s: str, word_dict: List[str], index: int, i: int) -> bool:
        ans = False
        if s[index : i + 1] in word_dict:
            ans = True
        return ans

    def break_words_brute(
        self, s: str, word_dict: List[str], ans: List[List[str]], substring: List[str], index: int
    ) -> None:
        if index == len(s):
            ans.append(list(substring))

        else:
            for i in range(index, len(s)):
                if self.break_possible_brute(s, word_dict, index, i):
                    substring.append(s[index : i + 1])
                    self.break_words_brute(s, word_dict, ans, substring, i + 1)
                    substring.pop()

        return

    def word_break_print_all_ways_brute(self, s: str, word_dict: List[str]) -> List[str]:
        ans: List[List[str]] = []
        substring: List[str] = []
        self.break_words_brute(s, word_dict, ans, substring, 0)
        return [" ".join(row) for row in ans]

    def word_break_print_all_ways_better(self, s: str, word_dict: List[str]) -> List[str]:
        # SKIP: no distinct middle tier — the list-scan brute goes straight to the
        # set-lookup optimal; nothing sensible sits between them.
        pass

    def break_possible_optimal(self, s: str, word_dict: set, index: int, i: int) -> bool:
        ans = False
        if s[index : i + 1] in word_dict:
            ans = True
        return ans

    def break_words_optimal(
        self, s: str, word_dict: set, ans: List[List[str]], substring: List[str], index: int
    ) -> None:
        if index == len(s):
            ans.append(list(substring))

        else:
            for i in range(index, len(s)):
                if self.break_possible_optimal(s, word_dict, index, i):
                    substring.append(s[index : i + 1])
                    self.break_words_optimal(s, word_dict, ans, substring, i + 1)
                    substring.pop()

        return

    def word_break_print_all_ways_optimal(self, s: str, word_dict: List[str]) -> List[str]:
        ans: List[List[str]] = []
        substring: List[str] = []
        hashSet = set(word_dict)
        self.break_words_optimal(s, hashSet, ans, substring, 0)
        return [" ".join(row) for row in ans]


if __name__ == "__main__":
    sol = Solution()
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    print(sol.word_break_print_all_ways_brute(s, word_dict))
    s = "catsanddog"
    word_dict = ["cat", "cats", "and", "sand", "dog"]
    print(sol.word_break_print_all_ways_optimal(s, word_dict))
