# mypy: disable-error-code="empty-body"
# QUESTION: Check if an array represents a min-heap or not
# Given an array arr of n integers representing a complete binary tree in level
# order, determine whether it satisfies the min-heap property, i.e. every parent
# node is less than or equal to both of its children.
# For a node at index i (0-based): left child = 2*i+1, right child = 2*i+2.
#
# Example 1:
# Input: arr = [10, 20, 30, 21, 23]
# Output: True
# Explanation: 10<=20, 10<=30, 20<=21, 20<=23; every parent <= its children.
#
# Example 2:
# Input: arr = [10, 20, 30, 25, 15]
# Output: False
# Explanation: 20 > 15 (parent at index 1 greater than its child at index 4).
#
# Constraints:
# 1 <= n <= 10^5
# -10^9 <= arr[i] <= 10^9


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
    def isMinHeap_brute(self, arr: List[int]) -> bool:
        pass

    def isMinHeap_better(self, arr: List[int]) -> bool:
        pass

    def isMinHeap_optimal(self, arr: List[int]) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.isMinHeap_optimal([10, 20, 30, 21, 23]))
