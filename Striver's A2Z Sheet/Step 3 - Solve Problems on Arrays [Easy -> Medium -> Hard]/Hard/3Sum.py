# mypy: disable-error-code="empty-body"
# QUESTION: 3 Sum
# Given an array nums, return all unique triplets [a, b, c] such that a + b + c = 0.
# The solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation: These are the two distinct triplets summing to 0.
# Constraints:
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5

"""
#Brute Force:
1. Try every triple (i, j, k) with three nested loops.
2. When the sum is 0, sort the triple and insert into a set to dedupe.
TC -> O(n^3 * log(#triplets)), SC -> O(#triplets)

#Better Approach:
1. Fix i, then scan j; for each pair the needed third value is -(nums[i]+nums[j]).
2. Keep a hash set of values seen between i and j; if the needed value is present
   record the sorted triplet in a result set.
TC -> O(n^2 * log(#triplets)), SC -> O(#triplets) + O(n)

#Optimal Approach (Sort + Two Pointers):
1. Sort the array. Fix i and skip duplicate i values.
2. Use two pointers j (i+1) and k (end): move j right if the sum is too small, k
   left if too big; on a hit record the triplet.
3. After a hit, advance j and k past duplicates so triplets stay unique — no set
   needed.
TC -> O(n log n) + O(n^2), SC -> O(#triplets)

#KEY INSIGHT:
- Sorting lets the inner search be a two-pointer sweep (O(n) instead of a hash
  set), and skipping equal neighbours removes duplicates without a set.
"""

from typing import List


class Solution:
    def three_sum_brute(self, nums: List[int]) -> List[List[int]]:
        found: set[tuple[int, int, int]] = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triple = tuple(sorted([nums[i], nums[j], nums[k]]))
                        found.add(triple)  # type: ignore[arg-type]
        return [list(item) for item in found]

    def three_sum_better(self, nums: List[int]) -> List[List[int]]:
        found: set[tuple[int, int, int]] = set()
        for i in range(len(nums)):
            seen: set[int] = set()
            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])
                if third in seen:
                    triple = tuple(sorted([nums[i], nums[j], third]))
                    found.add(triple)  # type: ignore[arg-type]
                seen.add(nums[j])
        return [list(item) for item in found]

    def three_sum_optimal(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.three_sum_optimal([-1, 0, 1, 2, -1, -4]))
