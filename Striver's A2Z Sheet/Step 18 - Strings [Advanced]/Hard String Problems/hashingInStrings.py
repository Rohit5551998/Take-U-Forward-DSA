# mypy: disable-error-code="empty-body"
# QUESTION: Hashing in Strings (String Hashing / Polynomial Rolling Hash)
# String hashing maps a string to a single integer so that string comparisons can
# be done in O(1) after O(n) preprocessing. A polynomial rolling hash treats a
# string s of length n as a number in a base p (a prime larger than the alphabet
# size), taken modulo a large prime m:
#   hash(s) = (s[0]*p^0 + s[1]*p^1 + ... + s[n-1]*p^(n-1)) mod m
# By precomputing prefix hashes and powers of p, the hash of any substring
# s[l..r] can be obtained in O(1). Given a string s and a list of (l, r) queries,
# return the hash value of each requested substring.
# Example 1:
# Input: s = "abcde", queries = [(0, 2), (1, 3)]
# Output: [hash("abc"), hash("bcd")]
# Explanation: Each query asks for the polynomial rolling hash of the substring
# s[l..r]; equal substrings must produce equal hash values.
# Constraints:
# 1 <= s.length <= 10^5
# 1 <= number of queries <= 10^5
# 0 <= l <= r < s.length
# s consists of lowercase English letters.

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

from typing import List, Tuple


class Solution:
    def substring_hashes_brute(self, s: str, queries: List[Tuple[int, int]]) -> List[int]:
        pass

    def substring_hashes_better(self, s: str, queries: List[Tuple[int, int]]) -> List[int]:
        pass

    def substring_hashes_optimal(self, s: str, queries: List[Tuple[int, int]]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.substring_hashes_optimal("abcde", [(0, 2), (1, 3)]))
