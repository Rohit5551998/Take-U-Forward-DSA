# mypy: disable-error-code="empty-body"
# QUESTION: Count all subsequences with sum K
# Given an array arr of size n and an integer k, count the number of
# subsequences whose elements sum up to exactly k.
# Example 1:
# Input: arr = [1, 2, 1], k = 2
# Output: 2
# Explanation: Subsequences [1,1] (index 0,2) and [2] both sum to 2.
# Example 2:
# Input: arr = [4, 9, 2, 5, 1], k = 10
# Output: 2
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
    def count_subseq_sum_k_brute(self, arr: List[int], k: int) -> int:
        pass

    def count_subseq_sum_k_better(self, arr: List[int], k: int) -> int:
        pass

    def count_subseq_sum_k_optimal(self, arr: List[int], k: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.count_subseq_sum_k_optimal([1, 2, 1], 2))
