# mypy: disable-error-code="empty-body"
# QUESTION: 4 Sum
# Given an array nums and a target, return all unique quadruplets
# [a, b, c, d] such that a + b + c + d = target. No duplicate quadruplets.
# Example 1:
# Input: nums = [1, 0, -1, 0, -2, 2], target = 0
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
# Explanation: All distinct quadruplets summing to 0.
# Constraints:
# 1 <= nums.length <= 200
# -10^9 <= nums[i], target <= 10^9

"""
#Brute Force:
1. Four nested loops over all quadruples.
2. On a match, sort the quad and add to a set to dedupe.
TC -> O(n^4), SC -> O(#quads)

#Better Approach:
1. Fix i and j with two loops; for the remaining two use a hash set to find the
   fourth value target-(nums[i]+nums[j]+nums[k]) while scanning k.
2. Store sorted quads in a set.
TC -> O(n^3 * log(#quads)), SC -> O(#quads) + O(n)

#Optimal Approach (Sort + Two Pointers):
1. Sort the array. Fix i and j (skipping duplicate i and duplicate j).
2. Two pointers k (j+1) and l (end) sweep inward: move k right if the sum is too
   small, l left if too big; on a hit record the quad.
3. After a hit, advance k and l past duplicates so quads stay unique — no set.
TC -> O(n^3), SC -> O(#quads)

#KEY INSIGHT:
- Fix two indices and reduce to a sorted two-pointer 2-sum; neighbour-skipping at
  all four levels removes duplicates without a set.
"""

from typing import List


class Solution:
    def four_sum_brute(self, nums: List[int], target: int) -> List[List[int]]:
        found: set[tuple[int, int, int, int]] = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for m in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[m] == target:
                            quad = tuple(sorted([nums[i], nums[j], nums[k], nums[m]]))
                            found.add(quad)  # type: ignore[arg-type]
        return [list(item) for item in found]

    def four_sum_better(self, nums: List[int], target: int) -> List[List[int]]:
        found: set[tuple[int, int, int, int]] = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                seen: set[int] = set()
                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])
                    if fourth in seen:
                        quad = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                        found.add(quad)  # type: ignore[arg-type]
                    seen.add(nums[k])
        return [list(item) for item in found]

    def four_sum_optimal(self, nums: List[int], target: int) -> List[List[int]]:
        ans: List[List[int]] = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, m = j + 1, n - 1
                while k < m:
                    total = nums[i] + nums[j] + nums[k] + nums[m]
                    if total < target:
                        k += 1
                    elif total > target:
                        m -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[m]])
                        k += 1
                        m -= 1
                        while k < m and nums[k] == nums[k - 1]:
                            k += 1
                        while k < m and nums[m] == nums[m + 1]:
                            m -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.four_sum_optimal([1, 0, -1, 0, -2, 2], 0))
