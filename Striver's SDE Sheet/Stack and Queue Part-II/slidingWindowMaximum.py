# mypy: disable-error-code="empty-body"
# QUESTION: Sliding Window Maximum
# Given an array of integers arr, there is a sliding window of size k which is moving from the
# very left of the array to the very right. You can only see the k numbers in the window. Each
# time the sliding window moves right by one position. Return the max sliding window.
#
# Examples:
# Example 1:
# Input: arr = [4, 0, -1, 3, 5, 3, 6, 8], k = 3
# Output: [4, 3, 5, 5, 6, 8]
# Explanation:
# Window position           Max
# [4  0 -1] 3  5  3  6  8    4
#  4 [0 -1  3] 5  3  6  8    3
#  4  0 [-1 3  5] 3  6  8    5
#  4  0 -1 [3  5  3] 6  8    5
#  4  0 -1  3 [5  3  6] 8    6
#  4  0 -1  3  5 [3  6  8]   8
# For each window of size k=3, we find the maximum element in the window and add it to our
# output array.
#
# Example 2:
# Input: arr = [20, 25], k = 2
# Output: [25]
# Explanation: There's just one window of size 2 that is possible and the maximum of the two
# elements is our answer.
#
# Constraints:
# - 1 <= arr.length <= 10^5
# - -10^4 <= arr[i] <= 10^4
# - 1 <= k <= arr.length


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
    def sliding_window_maximum_brute(self, arr: List[int], k: int) -> List[int]:
        pass

    def sliding_window_maximum_better(self, arr: List[int], k: int) -> List[int]:
        pass

    def sliding_window_maximum_optimal(self, arr: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    arr = [4, 0, -1, 3, 5, 3, 6, 8]
    k = 3
    print(sol.sliding_window_maximum_optimal(arr, k))
