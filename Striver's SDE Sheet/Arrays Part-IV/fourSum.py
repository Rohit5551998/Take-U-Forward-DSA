# QUESTION: 4 Sum
# Given an array of N integers, find unique quadruplets that add up to give
# a target value. Return an array of all the unique quadruplets
# [arr[a], arr[b], arr[c], arr[d]] such that:
#   - 0 <= a, b, c, d < N and a, b, c, d are distinct indices
#   - arr[a] + arr[b] + arr[c] + arr[d] == target
# You may return the answer in any order.
#
# Examples:
# Example 1:
# Input: nums = [1, 0, -1, 0, -2, 2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
# Example 2:
# Input: nums = [2, 2, 2, 2, 2], target = 8
# Output: [[2,2,2,2]]
#
# Constraints:
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9


"""
#Brute Force:
1. We need every quadruplet (a,b,c,d) of distinct indices summing to target, so
   just enumerate all of them with four nested loops i<j<k<l.
2. The index ordering i<j<k<l guarantees each combination of POSITIONS is picked
   once, but the same VALUES can still recur (e.g. duplicate numbers), so we must
   dedup by value, not by index.
3. When the four values add to target, sort them and store as a tuple in a set —
   sorting canonicalises the quad so [-2,-1,1,2] and [1,-2,2,-1] collapse to one.
4. Convert the set of tuples back to a list of lists at the end.
TC -> O(n^4), SC -> O(no. of quads) for the answer set

#Better Approach:
1. Drop the innermost loop using the 2Sum-with-hashing idea: fix the first two
   elements i and j, then the remaining two must sum to target - nums[i] - nums[j].
2. Sweep k from j+1, maintaining a hashSet of values already seen in that sweep.
   For the running 3-sum `sum = nums[i]+nums[j]+nums[k]`, the 4th value needed is
   target - sum; if it's already in hashSet, a valid quad exists.
3. Store that quad sorted in a set to dedup by value (same reason as brute).
4. Add nums[k] to hashSet AFTER checking, so we only pair with EARLIER k's and never
   reuse an index. Two outer loops x O(n) inner sweep = O(n^3); hashSet costs O(n) space.
TC -> O(n^3), SC -> O(n) for the per-sweep hashSet (+ answer)

#Optimal Approach:
1. Sort the array first so duplicates sit together and a two-pointer scan works.
2. Fix i (outer) and j (second). For each fixed pair, the remaining two values must
   sum to target - nums[i] - nums[j], findable in O(n) by two pointers on a sorted range.
3. Set k = j+1 and l = last index. Compute the 4-sum: if it's < target the smallest
   member is too small so move k right; if > target move l left; if equal, record the quad.
4. After recording, advance BOTH pointers and skip over equal neighbours
   (nums[k]==nums[k-1], nums[l]==nums[l+1]) so the same value-pair isn't re-added.
5. Skip duplicate i (nums[i]==nums[i-1]) and duplicate j (nums[j]==nums[j-1] for j>i+1)
   so each distinct (i,j) value-pair is processed once — this is what removes the need
   for extra hashing and keeps space at O(1).
6. Two nested loops O(n^2) x two-pointer O(n) = O(n^3), but with no auxiliary hash set.
TC -> O(n^3), SC -> O(1) extra (ignoring the sort and the output)

#KEY INSIGHT:
- Sorting turns 4Sum into "fix two, two-pointer the rest": the sorted order lets the
  two pointers converge in O(n) AND lets duplicates be skipped by comparing adjacent
  values — eliminating the better approach's hash set, so the same O(n^3) time now
  uses only O(1) extra space.
"""

from typing import List


class Solution:
    def four_sum_brute(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    for l in range(k + 1, len(nums)):
                        sum = nums[i] + nums[j] + nums[k] + nums[l]
                        if sum == target:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))

        return [list(item) for item in ans]

    def four_sum_better(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                hashSet = set()
                for k in range(j + 1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if (target - sum) in hashSet:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k], target - sum])))
                    hashSet.add(nums[k])
        return [list(item) for item in ans]

    def four_sum_optimal(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum < target:
                        k += 1
                    elif sum > target:
                        l -= 1
                    else:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k], nums[l]])))
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1

        return [list(item) for item in ans]


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(sol.four_sum_brute(nums, target))
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(sol.four_sum_better(nums, target))
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(sol.four_sum_optimal(nums, target))
