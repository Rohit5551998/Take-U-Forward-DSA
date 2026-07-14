# mypy: disable-error-code="empty-body"
# QUESTION: Convert Min Heap to Max Heap
# Given an array arr of n integers that already represents a valid min-heap (in
# level order), convert it in-place into a valid max-heap and return the resulting
# array. A max-heap requires every parent node to be greater than or equal to both
# of its children.
#
# Example 1:
# Input: arr = [3, 4, 8, 11, 13]
# Output: [13, 11, 8, 3, 4]
# Explanation: One valid max-heap arrangement where each parent >= its children.
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
    def convertMinToMaxHeap_brute(self, arr: List[int]) -> List[int]:
        pass

    def convertMinToMaxHeap_better(self, arr: List[int]) -> List[int]:
        pass

    def convertMinToMaxHeap_optimal(self, arr: List[int]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.convertMinToMaxHeap_optimal([3, 4, 8, 11, 13]))
