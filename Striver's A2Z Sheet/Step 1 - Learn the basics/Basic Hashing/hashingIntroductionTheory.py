# mypy: disable-error-code="empty-body"
# QUESTION: Introduction to Hashing (Theory)
# Foundational/theory topic: hashing maps keys to array indices via a hash
# function, enabling average O(1) insert, lookup, and delete. Pre-computing counts
# or presence into a hash table (dict/set) trades space for speed and underlies
# many optimal solutions. Collisions are resolved by chaining or open addressing.
# Example 1:
# Input: arr = [1, 2, 1, 3, 2], query = 2
# Output: 2
# Explanation: Build a frequency map in one pass, then answer each query in O(1).
# Constraints:
# - Average operations are O(1); worst case degrades to O(n) with many collisions.
# - Keys must be hashable (immutable) to be stored in a dict/set.

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
    def hashing_introduction_theory_brute(self, arr: List[int], query: int) -> None:
        pass

    def hashing_introduction_theory_better(self, arr: List[int], query: int) -> None:
        pass

    def hashing_introduction_theory_optimal(self, arr: List[int], query: int) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.hashing_introduction_theory_optimal(...)
