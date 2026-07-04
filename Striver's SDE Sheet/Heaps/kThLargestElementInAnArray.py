# mypy: disable-error-code="empty-body"
# QUESTION: K-th Largest element in an array
# Given an integer array `nums` and an integer k, return the k-th
# LARGEST element in the array. Note that it is the k-th largest element
# in sorted order, not the k-th distinct element.
# Can you solve it without sorting?
#
# Examples:
# Example 1:
# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5
#
# Example 2:
# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
# Output: 4
#
# Constraints:
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
# Approaches:
#   - O(n log n): sort and return nums[n-k].
#   - O(n log k): maintain a min-heap of size k; the heap root is the
#     answer when done.
#   - O(n) average: Quickselect (partition-based selection).


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
    def k_th_largest_element_in_an_array_brute(self, nums: List[int], k: int) -> int:
        pass

    def k_th_largest_element_in_an_array_better(self, nums: List[int], k: int) -> int:
        pass

    def k_th_largest_element_in_an_array_optimal(self, nums: List[int], k: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sol.k_th_largest_element_in_an_array_optimal(nums, k))
