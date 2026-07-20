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
1. The k-th LARGEST element is just a positional query once the data is ordered, so the most
   direct idea is to fully sort. Sort nums in DESCENDING order so index 0 holds the largest,
   index 1 the second-largest, and so on.
2. The k-th largest therefore sits at index k-1. Walk i from 0 to k-1 keeping the last seen
   value in `ans`; after the loop `ans` is nums[k-1]. (Equivalently you could just index
   nums[k-1] directly — the loop lands on the same element.)
3. Return ans. Cost is dominated by the sort; we throw away most of the ordering work since we
   only needed one position, which is what the better/optimal tiers improve on.
TC -> O(n log n), SC -> O(1)  (in-place sort; O(n) if the sort allocates)

#Better Approach:
1. We don't need the whole array ordered — only the top-k region. A heap gives us cheap
   repeated "extract current largest". Python's heapq is a MIN-heap, so negate every value
   first: the smallest negative corresponds to the largest original number.
2. heapify the negated list in O(n) — this is cheaper than a full sort and turns the array
   into a max-heap-by-proxy.
3. Pop k times; each pop removes the current maximum (negated back with -). After k pops the
   last popped value is the k-th largest, held in `ans`.
4. Return ans. Each pop re-heapifies in O(log n), so k pops cost O(k log n) on top of the
   O(n) build.
TC -> O(n + k log n), SC -> O(n)  (the negated copy / heap)

#Optimal Approach:
1. Quickselect. We never need the array fully sorted — only the single element that WOULD sit
   at a known index. In ascending order the k-th largest lives at index target = n - k.
2. partition(left, right) picks a pivot (here nums[left]) and rearranges the window so all
   elements < pivot go before it and the rest after; it returns the pivot's FINAL sorted
   index p. That index is now correct forever, regardless of the rest.
3. Compare p with target. If p == target, the pivot is exactly the element we want -> return
   nums[p].
4. If p > target the answer sits to the LEFT of the pivot, so discard the right part:
   right = p - 1. If p < target it sits to the RIGHT, so left = p + 1.
5. Loop, re-partitioning only the surviving side. Unlike quicksort we recurse into ONE side,
   so the work shrinks: n + n/2 + n/4 + ... ≈ 2n on average -> O(n). A pathological pivot
   sequence degrades to O(n^2) worst case.
TC -> O(n) average / O(n^2) worst, SC -> O(1) (in-place, iterative loop)

#KEY INSIGHT:
- A single partition locks ONE element into its true sorted index for free. So instead of
  sorting everything, keep partitioning and steer toward the one index you care about
  (n - k), throwing away the half that can't contain the answer each time.
"""

import heapq
from typing import List


class Solution:
    def k_th_largest_element_in_an_array_brute(self, nums: List[int], k: int) -> int:
        ans = -1
        nums.sort(reverse=True)

        for i in range(0, k):
            ans = nums[i]

        return ans

    def k_th_largest_element_in_an_array_better(self, nums: List[int], k: int) -> int:
        ans = -1
        nums = [-x for x in nums]
        heapq.heapify(nums)

        for _ in range(0, k):
            ans = -heapq.heappop(nums)

        return ans

    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[left]  # pivot parked at left until the final swap
        p = left  # boundary: nums[left+1..p] all < pivot

        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                p += 1  # grow the "< pivot" region, swap the small element in
                nums[i], nums[p] = nums[p], nums[i]

        nums[p], nums[left] = nums[left], nums[p]  # drop pivot into its sorted slot

        return p  # pivot's final index (not its value)

    def k_th_largest_element_in_an_array_optimal(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = self.partition(nums, left, right)
            if pivot == target:
                return nums[pivot]
            if pivot > target:
                right = pivot - 1
            else:
                left = pivot + 1

        return -1  # unreachable: target is always in [0, n-1], so the loop always returns


if __name__ == "__main__":
    sol = Solution()
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sol.k_th_largest_element_in_an_array_brute(nums, k))
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(sol.k_th_largest_element_in_an_array_better(nums, k))
    nums = [3, 2, 5, 1, 6, 4]
    k = 2
    print(sol.k_th_largest_element_in_an_array_optimal(nums, k))
