# mypy: disable-error-code="empty-body"
# QUESTION: Subset Sum I
# Given an array arr of n integers, return the sum of every subset (subsequence)
# in non-decreasing (sorted) order. There are 2^n subset sums in total.
# Example 1:
# Input: arr = [2, 3]
# Output: [0, 2, 3, 5]
# Explanation: Subsets are [], [2], [3], [2,3] with sums 0, 2, 3, 5.
# Example 2:
# Input: arr = [5, 2, 1]
# Output: [0, 1, 2, 3, 5, 6, 7, 8]
# Constraints:
# 1 <= n <= 15
# 0 <= arr[i] <= 10^4

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
    def subset_sum_i_brute(self, arr: List[int]) -> List[int]:
        pass

    def subset_sum_i_better(self, arr: List[int]) -> List[int]:
        pass

    def subset_sum_i_optimal(self, arr: List[int]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.subset_sum_i_optimal([2, 3]))
