# mypy: disable-error-code="empty-body"
# QUESTION: Check if there exists a subsequence with sum K
# Given an array arr of size n and an integer k, determine whether there exists
# at least one subsequence whose elements sum up to exactly k. Return True/False.
# Example 1:
# Input: arr = [1, 2, 3, 4, 5], k = 8
# Output: True
# Explanation: The subsequence [3, 5] (or [1, 3, 4]) sums to 8.
# Example 2:
# Input: arr = [2, 4, 6], k = 5
# Output: False
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
    def check_subseq_sum_k_brute(self, arr: List[int], k: int) -> bool:
        pass

    def check_subseq_sum_k_better(self, arr: List[int], k: int) -> bool:
        pass

    def check_subseq_sum_k_optimal(self, arr: List[int], k: int) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.check_subseq_sum_k_optimal([1, 2, 3, 4, 5], 8))
