# QUESTION: 3 Sum
# Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short, you need to return  an array of all the unique triplets [arr[a.
#
# Examples:
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k
#
# Example 2:
# Input: nums=[-1,0,1,0]
# Output: Output: [[-1,0,1],[-1,1,0]]
# Explanation: Out of all possible unique triplets possible, [-1,0,1] and [-1,1,0] satisfy the condition of summing up to zero with i!=j!=k


"""
#Brute Force:
1. We need every triplet (a,b,c) of distinct indices summing to target, so just
   enumerate all of them with three nested loops i<j<k.
2. The ordering i<j<k picks each combination of POSITIONS once, but duplicate
   VALUES can still produce the same triplet, so we must dedup by value.
3. When the three values add to target, sort them and store the tuple in a set —
   sorting canonicalises the triplet so reorderings collapse into one entry.
4. Convert the set of tuples back to a list of lists at the end.
TC -> O(n^3), SC -> O(no. of triplets) for the answer set

#Better Approach:
1. Drop the innermost loop with the 2Sum-with-hashing idea: fix the first element i,
   then the other two must sum to target - nums[i].
2. Sweep j from i+1, keeping a hashSet of values seen so far in that sweep. For the
   running pair, the value still needed is target - nums[i] - nums[j]; if it's already
   in hashSet, a valid triplet exists.
3. Store that triplet sorted in a set to dedup by value (same reason as brute).
4. Add nums[j] to hashSet AFTER checking, so we only pair with EARLIER j's and never
   reuse an index. One outer loop x O(n) inner sweep = O(n^2); hashSet costs O(n) space.
TC -> O(n^2), SC -> O(n) for the per-sweep hashSet (+ answer)

#Optimal Approach:
1. Sort the array first so duplicates sit together and a two-pointer scan works.
2. Fix i (outer). The remaining two values must sum to target - nums[i], findable in
   O(n) by two pointers on the sorted range to the right of i.
3. Set j = i+1 and k = last index. Compute the 3-sum: if it's < target the smallest
   member is too small so move j right; if > target move k left; if equal, record it.
4. After recording, advance BOTH pointers and skip equal neighbours
   (nums[j]==nums[j-1], nums[k]==nums[k+1]) so the same value-pair isn't re-added.
5. Skip duplicate i (nums[i]==nums[i-1]) so each distinct first value is processed
   once — this dedup-by-adjacency is what removes the need for extra hashing.
6. One outer loop O(n) x two-pointer O(n) = O(n^2), with no auxiliary hash set.
TC -> O(n^2), SC -> O(1) extra (ignoring the sort and the output)

#KEY INSIGHT:
- Sorting turns 3Sum into "fix one, two-pointer the rest": the sorted order lets the
  two pointers converge in O(n) AND lets duplicates be skipped by comparing adjacent
  values — eliminating the better approach's hash set, so the same O(n^2) time now
  uses only O(1) extra space.
"""

from typing import List


class Solution:
    def three_sum_brute(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == target:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return [list(item) for item in ans]

    def three_sum_better(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        for i in range(0, len(nums)):
            hashSet = set()
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if (target - sum) in hashSet:
                    ans.add(tuple(sorted([nums[i], nums[j], target - sum])))
                hashSet.add(nums[j])
        return [list(item) for item in ans]

    def three_sum_optimal(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
                else:
                    ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return [list(item) for item in ans]


if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(sol.three_sum_brute(nums, target))
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(sol.three_sum_better(nums, target))
    nums = [-1, 0, 1, 2, -1, -4]
    target = 0
    print(sol.three_sum_optimal(nums, target))
