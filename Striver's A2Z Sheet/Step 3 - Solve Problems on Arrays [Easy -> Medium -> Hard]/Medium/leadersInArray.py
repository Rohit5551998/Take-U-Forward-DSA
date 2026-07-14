# mypy: disable-error-code="empty-body"
# QUESTION: Leaders in an Array
# An element is a leader if it is strictly greater than all elements to its right.
# The last element is always a leader. Return all leaders in their original order.
# Example 1:
# Input: nums = [10, 22, 12, 3, 0, 6]
# Output: [22, 12, 6]
# Explanation: 22 > {12,3,0,6}, 12 > {3,0,6}, 6 > {} (last element).
# Constraints:
# 1 <= nums.length <= 10^6
# -10^9 <= nums[i] <= 10^9

"""
#Brute Force:
1. For each element check with an inner loop whether any element to its right is
   greater. If none is, it is a leader.
TC -> O(n^2), SC -> O(1) (excluding output)

#Better Approach:
SKIPPED — no distinct middle tier; the right-to-left suffix-max scan below is the
direct improvement over the brute.

#Optimal Approach:
1. Traverse from right to left tracking the maximum seen so far.
2. An element is a leader iff it is >= that running maximum (using >= keeps a
   leader equal to the current suffix max, matching the ">= to the right"
   convention for the last-max).
3. Update the running max and collect leaders; reverse at the end to restore the
   original left-to-right order.
TC -> O(n), SC -> O(1) (excluding output)

#KEY INSIGHT:
- "Greater than everything to the right" only depends on the running suffix
  maximum, so one right-to-left pass identifies every leader.
"""

from typing import List


class Solution:
    def reverse(self, arr: List[int], start: int, end: int) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def leaders_brute(self, nums: List[int]) -> List[int]:
        output: List[int] = []
        for i in range(len(nums)):
            if all(nums[j] <= nums[i] for j in range(i + 1, len(nums))):
                output.append(nums[i])
        return output

    def leaders_better(self, nums: List[int]) -> List[int]:
        # SKIP: no distinct better approach; suffix-max scan is the optimal.
        pass

    def leaders_optimal(self, nums: List[int]) -> List[int]:
        output: List[int] = []
        max_so_far = float("-inf")
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] >= max_so_far:
                max_so_far = nums[i]
                output.append(nums[i])
        self.reverse(output, 0, len(output) - 1)
        return output


if __name__ == "__main__":
    sol = Solution()
    print(sol.leaders_optimal([10, 22, 12, 3, 0, 6]))
