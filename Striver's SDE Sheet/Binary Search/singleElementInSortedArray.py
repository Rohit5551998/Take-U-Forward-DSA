# mypy: disable-error-code="empty-body"
# QUESTION: Single element in sorted array
# Given an array nums sorted in non-decreasing order. Every number in the array except one
# appears twice. Find the single number in the array.
#
# Examples:
# Example 1:
# Input: nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
# Output: 4
# Explanation: Only the number 4 appears once in the array.
#
# Example 2:
# Input: nums = [1, 1, 3, 5, 5]
# Output: 3
# Explanation: Only the number 3 appears once in the array.
#
# Constraints:
# n == nums.length
# 1 <= n <= 10^4
# -10^4 <= nums[i] <= 10^4


"""
#Brute Force:
1. The single element is the one that differs from BOTH of its neighbours, so
   we can just scan and test that condition. But the endpoints only have one
   neighbour, so handle them first.
2. Check the left end: if the array has one element, or nums[0] != nums[1], the
   single element is nums[0]. Symmetrically, if nums[-1] != nums[-2], it's the
   last element.
3. Otherwise the single element is strictly inside. Walk i from 1 to n-2 and
   return the first nums[i] that equals neither nums[i-1] nor nums[i+1] — that
   is the element with no pair partner on either side.
TC -> O(N) (single linear pass in the worst case), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier. The alternatives to the linear scan (e.g.
XOR-ing every element) are still O(N); the next real improvement jumps straight
to the O(log N) binary search (optimal), so there is no sensible intermediate.

#Optimal Approach:
1. Exploit the index PARITY pattern created by the pairs. Before the single
   element, each pair occupies indices (even, odd): the first occurrence sits at
   an even index, its duplicate at the next odd index. After the single element
   this shifts to (odd, even). The single element is exactly where that pattern
   breaks — so the answer space is monotonic and binary-searchable.
2. Handle the endpoints first (same shortcuts as brute) so that inside the
   search every mid has both a mid-1 and mid+1 neighbour; then binary search the
   interior range [1, n-2].
3. At mid, if nums[mid] equals neither neighbour, it is the single element —
   done.
4. Otherwise decide which side is still "intact". If mid is even and its partner
   is mid+1 (nums[mid] != nums[mid-1]), OR mid is odd and its partner is mid-1
   (nums[mid] != nums[mid+1]), then the (even,odd) pattern still holds here, so
   the single element is to the RIGHT — move low = mid + 1.
5. In the complementary case the pattern has already broken at or before mid, so
   the single element is to the LEFT — move high = mid - 1. Repeat until found.
TC -> O(log N) (halve the interior each step), SC -> O(1)

#KEY INSIGHT:
- Duplicate pairs impose a parity invariant on indices: left of the single
  element the pair partner of an even index is the next index; right of it the
  invariant flips. Checking mid's parity against which neighbour it matches tells
  you which half still obeys the invariant, letting binary search converge on the
  break point in O(log N) instead of scanning in O(N).
"""

from typing import List


class Solution:
    def single_element_in_sorted_array_brute(self, nums: List[int]) -> int:
        ans = None
        if len(nums) == 1 or nums[0] != nums[1]:
            ans = nums[0]
        elif nums[-1] != nums[-2]:
            ans = nums[-1]
        else:
            for i in range(1, len(nums) - 1):
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    ans = nums[i]
                    break
        return ans

    def single_element_in_sorted_array_better(self, nums: List[int]) -> int:
        # SKIP: no distinct middle tier — the alternatives to the O(N) scan (e.g.
        # XOR) are still O(N); the next real gain is the O(log N) binary search.
        pass

    def single_element_in_sorted_array_optimal(self, nums: List[int]) -> int:
        ans = None
        if len(nums) == 1 or nums[0] != nums[1]:
            ans = nums[0]
        elif nums[-1] != nums[-2]:
            ans = nums[-1]
        else:
            low, high = 1, len(nums) - 2

            while low <= high:
                mid = low + (high - low) // 2

                if (nums[mid] != nums[mid + 1]) and (nums[mid] != nums[mid - 1]):
                    ans = nums[mid]
                    break

                # Eliminate Left Half if
                if (mid % 2 == 0 and nums[mid] != nums[mid - 1]) or (
                    mid % 2 == 1 and nums[mid] != nums[mid + 1]
                ):
                    low = mid + 1

                # Eliminate Right Half if
                elif (mid % 2 == 1 and nums[mid] != nums[mid - 1]) or (
                    mid % 2 == 0 and nums[mid] != nums[mid + 1]
                ):
                    high = mid - 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    print(sol.single_element_in_sorted_array_brute(nums))
    nums = [1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]
    print(sol.single_element_in_sorted_array_optimal(nums))
