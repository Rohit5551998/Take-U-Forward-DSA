# mypy: disable-error-code="empty-body"
# QUESTION: Number of NGEs to the Right
# Given an array arr of size n and an array of q indices, for each queried index
# i return the count of elements to the right of i (in arr[i+1..n-1]) that are
# strictly greater than arr[i].
# Example 1:
# Input: arr = [3, 4, 2, 7, 5, 8, 10, 6], indices = [0, 5]
# Output: [6, 1]
# Explanation: To the right of index 0 (value 3), the elements 4,7,5,8,10,6 are
# all greater -> 6. To the right of index 5 (value 8), only 10 is greater -> 1.
# Constraints:
# 1 <= n <= 10^4
# 1 <= q <= 10^4
# 0 <= indices[j] < n

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
    def count_nge_brute(self, arr: List[int], indices: List[int]) -> List[int]:
        pass

    def count_nge_better(self, arr: List[int], indices: List[int]) -> List[int]:
        pass

    def count_nge_optimal(self, arr: List[int], indices: List[int]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.count_nge_optimal([3, 4, 2, 7, 5, 8, 10, 6], [0, 5]))
