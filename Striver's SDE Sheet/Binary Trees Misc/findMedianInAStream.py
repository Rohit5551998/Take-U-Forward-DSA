# mypy: disable-error-code="empty-body"
# QUESTION: Find Median in a Stream
# You are given a stream of integers arr[], arriving one by one. After
# each new integer is added to the stream, output the median of all
# elements seen so far. Return a list of medians — one after each
# insertion — where:
#   - If the number of elements seen so far is odd, the median is the
#     middle element when those elements are sorted.
#   - If the number of elements seen so far is even, the median is the
#     average of the two middle elements (use float division).
#
# Examples:
# Example 1:
# Input: arr = [5, 15, 1, 3]
# Output: [5, 10.0, 5, 4.0]
# Explanation:
#   After 5      -> median 5
#   After 5, 15  -> median (5+15)/2 = 10.0
#   After 5,15,1 -> sorted [1,5,15], median 5
#   After 5,15,1,3 -> sorted [1,3,5,15], median (3+5)/2 = 4.0
#
# Example 2:
# Input: arr = [1, 2]
# Output: [1, 1.5]
#
# Constraints:
# 1 <= arr.length <= 10^5
# -10^5 <= arr[i] <= 10^5
#
# Follow up: Can you achieve O(log n) per insertion using two heaps
# (a max-heap for the lower half + min-heap for the upper half)?


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
    def find_median_in_a_stream_brute(self, arr: List[int]) -> List[float]:
        pass

    def find_median_in_a_stream_better(self, arr: List[int]) -> List[float]:
        pass

    def find_median_in_a_stream_optimal(self, arr: List[int]) -> List[float]:
        pass


if __name__ == "__main__":
    sol = Solution()
    arr = [5, 15, 1, 3]
    print(sol.find_median_in_a_stream_optimal(arr))
