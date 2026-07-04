# mypy: disable-error-code="empty-body"
# QUESTION: Search element in a sorted and rotated array/ find pivot where it is rotated
# Given an integer array nums, sorted in ascending order with distinct
# values, and a target value k. The array is rotated at some pivot point
# that is unknown (e.g., [0,1,2,3,4,5] may become [3,4,5,0,1,2]). Find
# the index at which k is present in the array. If k is not present,
# return -1.
# You must solve the problem in O(log n) time.
#
# Examples:
# Input:nums = [4, 5, 6, 7, 0, 1, 2], k = 0
# Output :4
# Explanation: The target is 0. We can see that 0 is present in the given rotated sorted
# array, nums, at index 4. Thus, we get output 4, the index at which 0 is present.
#
# Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3
# Output :-1
# Explanation: The target is 3. Since 3 is not present in the given rotated sorted array,
# we get the output as -1.


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
    def search_element_in_a_sorted_and_rotated_array_find_pivot_where_it_is_rotated_brute(
        self, nums: List[int], k: int
    ) -> int:
        pass

    def search_element_in_a_sorted_and_rotated_array_find_pivot_where_it_is_rotated_better(
        self, nums: List[int], k: int
    ) -> int:
        pass

    def search_element_in_a_sorted_and_rotated_array_find_pivot_where_it_is_rotated_optimal(
        self, nums: List[int], k: int
    ) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    k = 0
    print(
        sol.search_element_in_a_sorted_and_rotated_array_find_pivot_where_it_is_rotated_optimal(
            nums, k
        )
    )
