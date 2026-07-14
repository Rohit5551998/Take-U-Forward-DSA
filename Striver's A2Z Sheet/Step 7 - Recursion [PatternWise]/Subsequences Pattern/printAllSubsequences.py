# mypy: disable-error-code="empty-body"
# QUESTION: Learn All Patterns of Subsequences (Print all / Print one / Count)
# Given an array arr of size n, master the three core recursion patterns over the
# subsequence "pick / not-pick" decision tree:
#   (a) Print ALL subsequences.
#   (b) Print exactly ONE subsequence that satisfies a condition (e.g. sum == k),
#       stopping the recursion early once found (return-boolean pattern).
#   (c) COUNT the number of subsequences that satisfy a condition (e.g. sum == k).
# These three patterns generalize to Combination Sum, Subset Sum, Power Set, etc.
# Example 1:
# Input: arr = [3, 1, 2]
# Output (print all): [], [2], [1], [1,2], [3], [3,2], [3,1], [3,1,2]
# Example 2:
# Input: arr = [1, 2, 1], k = 2
# Output (count sum==k): 2   (subsequences [2] and [1,1])
# Explanation: At each index we either PICK the element into the running
# subsequence or SKIP it; the leaves of this binary tree are all 2^n subsequences.
# Constraints:
# 1 <= n <= 20
# 0 <= arr[i] <= 100
# 0 <= k <= 1000

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
    def subsequence_patterns_brute(self, arr: List[int]) -> List[List[int]]:
        pass

    def subsequence_patterns_better(self, arr: List[int], k: int) -> bool:
        pass

    def subsequence_patterns_optimal(self, arr: List[int], k: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.subsequence_patterns_optimal([1, 2, 1], 2))
