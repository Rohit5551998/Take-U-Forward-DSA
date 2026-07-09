# mypy: disable-error-code="empty-body"
# QUESTION: Subset Sums
# Given an array, print the sum of every subset generated from it, in increasing order.
#
# Examples:
# Input: N = 3, arr[] = {5,2,1}
# Output: 0,1,2,3,5,6,7,8
# Explanation: The generated subsets are [], [5], [2], [5,2], [1], [5,1], [2,1], [5,2,1],
# so the subset sums are 0, 5, 2, 7, 1, 6, 3, 8 which sorted give 0,1,2,3,5,6,7,8.
#
# Input: N=3,arr[]= {3,1,2}
# Output: 0,1,2,3,3,4,5,6
# Explanation: The generated subsets are [], [3], [1], [3,1], [2], [3,2], [1,2], [3,1,2],
# so the subset sums are 0, 3, 1, 4, 2, 5, 3, 6 which sorted give 0,1,2,3,3,4,5,6.


"""
#Brute Force:
1. Every subset is a series of independent include/exclude choices, one per
   element, so with n elements there are exactly 2^n possible subsets. Encode
   each subset as an integer `mask` from 0 to 2^n - 1, where bit i being set
   means "include nums[i]".
2. Compute the number of masks as `1 << n` (i.e. 2^n) and iterate over every
   value in that range — each value is one distinct subset.
3. For a given mask, walk all n bit positions; whenever bit i is set
   (`mask & (1 << i)`), add nums[i] into that subset's running sum.
4. Append each subset's sum to the answer list.
5. Sort the answer ascending, since the problem asks for sums in increasing order.
   (Cost note: the inner n-bit scan is re-done for all 2^n masks — that redundant
   re-summation is what the optimal approach removes.)
TC -> O(2^n * n) to build + O(2^n log(2^n)) to sort, SC -> O(2^n) for the output

#Better Approach:
SKIPPED — no distinct intermediate exists. Both viable solutions still enumerate
all 2^n subsets; the only real gain is dropping the per-subset re-summation, which
is exactly the optimal recursion below. There is no sensible tier between them.

#Optimal Approach:
1. Rather than rebuilding each subset's total from scratch, thread a running
   `sum` down the recursion so every subset total is maintained incrementally
   in O(1) per step.
2. At each `index`, branch into two recursive calls — one that PICKS nums[index]
   (recurse with sum + nums[index]) and one that SKIPS it (recurse with sum
   unchanged). These two choices, taken over all indices, enumerate all 2^n
   include/exclude combinations.
3. Base case: when `index == len(nums)` every element has been decided, so the
   accumulated `sum` is one complete subset's sum — append it to the answer.
4. Each of the 2^n leaves does O(1) work (no inner loop over n like the bitmask),
   so generation is O(2^n) — a full factor of n faster than the brute force.
5. Sort the answer ascending for the required increasing-order output.
TC -> O(2^n) to build + O(2^n log(2^n)) to sort, SC -> O(2^n) output + O(n) stack

#KEY INSIGHT:
- Carry the running sum down the recursion instead of a subset list: each of the
  2^n subset sums is then produced in O(1), so you only pay to enumerate the
  subsets, never to re-add their elements.
"""

from typing import List


class Solution:
    def subset_sums_brute(self, nums: List[int]) -> List[int]:
        ans = []

        # Each element is set/unset independently, so n elements -> 2^n subset masks
        combs = 1 << (len(nums))

        for comb in range(0, combs):
            sum = 0
            for index in range(0, len(nums)):
                # Bit `index` set in the mask -> nums[index] is part of this subset
                if comb & (1 << index) > 0:
                    sum += nums[index]
            ans.append(sum)
        ans.sort()
        return ans

    def subset_sums_better(self, nums: List[int]) -> List[int]:
        # SKIP: no distinct middle tier — both solutions enumerate all 2^n subsets;
        # the only improvement is dropping per-subset re-summation, which IS the
        # optimal recursion (subset_sums_optimal).
        pass

    def find_subset_sum(self, nums: List[int], ans: List[int], index: int, sum: int) -> None:
        # Every element has been decided (picked/skipped) once index reaches n,
        # so the accumulated sum is one complete subset's sum
        if index == len(nums):
            ans.append(sum)
        else:
            self.find_subset_sum(nums, ans, index + 1, sum + nums[index])
            self.find_subset_sum(nums, ans, index + 1, sum)
        return

    def subset_sums_optimal(self, nums: List[int]) -> List[int]:
        ans: List[int] = []
        self.find_subset_sum(nums, ans, 0, 0)
        ans.sort()
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 2, 1]
    print(sol.subset_sums_brute(nums))
    nums = [5, 2, 1]
    print(sol.subset_sums_optimal(nums))
