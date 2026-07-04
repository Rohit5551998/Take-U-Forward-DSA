# mypy: disable-error-code="empty-body"
# QUESTION: Maximum of Minimums for Every Window Size
# Given an array arr[] of size n, for every window size i from 1 to n,
# find the maximum of the minimum of all contiguous subarrays of size i.
# Return an array `ans` of size n where ans[i-1] contains the maximum
# of minimums for window size i.
#
# Examples:
# Example 1:
# Input: arr = [10, 20, 30, 50, 10, 70, 30]
# Output: [70, 30, 20, 10, 10, 10, 10]
# Explanation:
#   Window size 1: max of (10,20,30,50,10,70,30) = 70
#   Window size 2: mins are (10,20,30,10,10,30) => max = 30
#   Window size 3: mins are (10,20,10,10,10) => max = 20
#   ... and so on.
#
# Example 2:
# Input: arr = [10, 20, 30]
# Output: [30, 20, 10]
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= arr[i] <= 10^9
#
# Optimal approach: O(n) using a monotonic stack — for each element find
# the nearest smaller to the left and right; that element is the min in
# a window of size (right - left - 1), and contributes to all smaller
# window sizes too. Then propagate to fill all window sizes.


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
    def maximum_of_minimums_for_every_window_size_brute(self, arr: List[int]) -> List[int]:
        pass

    def maximum_of_minimums_for_every_window_size_better(self, arr: List[int]) -> List[int]:
        pass

    def maximum_of_minimums_for_every_window_size_optimal(self, arr: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    arr = [10, 20, 30, 50, 10, 70, 30]
    print(sol.maximum_of_minimums_for_every_window_size_optimal(arr))
