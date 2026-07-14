# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Sum Combination
# Given two integer arrays A and B, each of size N, and an integer K. A sum
# combination is made by adding one element from array A and one element from
# array B. Return the maximum K valid distinct-index sum combinations from all the
# possible sum combinations, in non-increasing order.
#
# Example 1:
# Input: A = [3, 2], B = [1, 4], K = 2
# Output: [7, 6]
# Explanation: All sums are 3+1=4, 3+4=7, 2+1=3, 2+4=6; the top 2 are 7 and 6.
#
# Example 2:
# Input: A = [1, 4, 2, 3], B = [2, 5, 1, 6], K = 3
# Output: [10, 9, 9]
#
# Constraints:
# 1 <= N <= 10^5
# 1 <= K <= N
# -10^9 <= A[i], B[i] <= 10^9


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
    def maxSumCombination_brute(self, a: List[int], b: List[int], k: int) -> List[int]:
        pass

    def maxSumCombination_better(self, a: List[int], b: List[int], k: int) -> List[int]:
        pass

    def maxSumCombination_optimal(self, a: List[int], b: List[int], k: int) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.maxSumCombination_optimal([3, 2], [1, 4], 2))
