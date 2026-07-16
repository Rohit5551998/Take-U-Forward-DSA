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
1. The array is rotated, so it is NOT globally sorted — that means we cannot
   trust ordering to skip elements. The safest thing is to just look at every
   element one by one.
2. Walk the array left to right; the moment nums[i] == k, record i as the answer
   and stop early (no need to scan further since values are distinct).
3. If the loop finishes without a match, the element is absent, so the answer
   stays at its initial -1.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — there is no meaningful middle tier here. The problem jumps straight
from the O(N) linear scan to the O(log N) binary search; any intermediate
(e.g. sort-then-search) would destroy the original indices and be strictly
worse than the optimal, so no distinct "better" approach exists.

#Optimal Approach:
1. We must hit O(log N), which screams binary search — but the array is rotated,
   so a plain binary search on the whole thing won't work. KEY OBSERVATION: even
   after one rotation, at any mid the array splits into two parts and AT LEAST ONE
   of the two halves [low..mid] or [mid..high] is fully sorted.
2. Standard setup: low = 0, high = n-1, loop while low <= high, mid = low + (high-low)//2.
3. First check nums[mid] == k — if so we found it, record mid and break.
4. Decide which half is sorted. If nums[low] <= nums[mid], the LEFT half is sorted.
   Within a sorted half we CAN reason about ranges: if nums[low] <= k <= nums[mid],
   the target must lie in this sorted left half, so move high = mid - 1; otherwise
   it can only be in the messy right half, so move low = mid + 1.
5. Else the RIGHT half (nums[mid] <= nums[high]) is sorted. Symmetrically, if
   nums[mid] <= k <= nums[high], the target lies in the sorted right half, so move
   low = mid + 1; otherwise search the left half with high = mid - 1.
6. Each iteration discards half the search space, so we converge in O(log N).
   If low crosses high without a hit, k is absent and we return -1.
TC -> O(log N), SC -> O(1)

#KEY INSIGHT:
- A rotated sorted array, when split at any mid, always has at least one half
  that is perfectly sorted. Identify that sorted half, use its clean range to
  decide whether the target lies inside it (discard the other half) or outside
  it (discard this half) — turning rotation back into an ordinary binary search.
"""

from typing import List


class Solution:
    def search_element_in_a_sorted_and_rotated_array_find_pivot_where_it_is_rotated_brute(
        self, nums: List[int], k: int
    ) -> int:
        ans = -1
        for i in range(len(nums)):
            if nums[i] == k:
                ans = i
                break
        return ans

    def search_element_in_a_sorted_and_rotated_array_find_pivot_where_it_is_rotated_better(
        self, nums: List[int], k: int
    ) -> int:
        # SKIP: No meaningful middle tier — the problem goes straight from the
        # O(N) linear scan to the O(log N) rotated binary search; any in-between
        # (e.g. sort-then-search) loses the original indices and is strictly worse.
        pass

    def search_element_in_a_sorted_and_rotated_array_find_pivot_where_it_is_rotated_optimal(
        self, nums: List[int], k: int
    ) -> int:
        ans = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == k:
                ans = mid
                break

            # Left half [low..mid] is sorted (its start <= its end).
            if nums[low] <= nums[mid]:
                # k falls inside that sorted range -> keep left, else go right.
                if nums[low] <= k <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Otherwise the right half [mid..high] must be the sorted one.
            elif nums[mid] <= nums[high]:
                # k falls inside that sorted range -> keep right, else go left.
                if nums[mid] <= k <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    k = 0
    print(
        sol.search_element_in_a_sorted_and_rotated_array_find_pivot_where_it_is_rotated_brute(
            nums, k
        )
    )
    nums = [4, 5, 6, 7, 0, 1, 2]
    k = 0
    print(
        sol.search_element_in_a_sorted_and_rotated_array_find_pivot_where_it_is_rotated_optimal(
            nums, k
        )
    )
