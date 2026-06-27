# QUESTION: Two Sum
# Given an array of integers arr[] and an integer target.
# 1st variant: Return "YES" if there exist two numbers such that their sum
#              is equal to the target. Otherwise, return "NO".
# 2nd variant: Return the indices [i, j] of the two numbers such that
#              arr[i] + arr[j] == target. Otherwise, return [-1, -1].
#
# Examples:
# Input: N = 5, arr[] = {2,6,5,8,11}, target = 14
# Output : YES
# Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for first variant for second variant output will be : [1,3].
#
# Input: N = 5, arr[] = {2,6,5,8,11}, target = 15
# Output : NO.
# Explanation: There exist no such two numbers whose sum is equal to the target.


"""
#Brute Force:
1. Try every unordered pair: fix i, then scan every j > i and check if
   nums[i] + nums[j] == target. The j > i bound avoids reusing one element and
   avoids testing the same pair twice.
2. On a match, record [i, j] and break the inner loop; then `if ans: break` exits
   the outer loop too. So it short-circuits at the FIRST pair found (smallest i,
   then smallest j) instead of scanning the rest.
3. Returns [] if no pair sums to target. The early exit helps on lucky inputs, but
   the worst case (no pair, or pair only at the very end) still scans all pairs.
TC -> O(n^2), SC -> O(1)

#Better Approach (one-pass hashmap — returns INDICES):
1. For a fixed second element nums[i], its partner must be exactly
   complement = target - nums[i]. So instead of scanning for it, remember every
   value we've already seen in a map value -> index.
2. Walk once: before inserting nums[i], check if its complement is already in the
   map. If yes, that earlier index plus i is the answer [map[complement], i].
3. Otherwise store nums[i] -> i and continue. Checking-before-inserting guarantees
   the two indices are distinct.
4. O(1) average lookups replace the brute force's inner loop, and crucially this
   preserves ORIGINAL indices — so it's the best option for the index variant.
TC -> O(n), SC -> O(n)

#Optimal Approach (sort + two pointers — answers PRESENCE):
1. Sort the array, then place pointers left=0 and right=n-1. The sortedness lets a
   single sum comparison tell us which way to move.
2. Look at value = nums[left] + nums[right]: if it equals target we found a pair
   (return True). If it's too big, only shrinking helps, so right--. If it's too
   small, only growing helps, so left++.
3. The pointers march inward and never revisit, so the scan is linear after the
   sort; no extra hashmap, so O(1) space.
4. The trade-off: sorting DESTROYS original positions (and mutates the input), so
   this can report only WHETHER a pair exists, not the original indices. It also
   trades the hashmap's O(n) time for O(n log n) time to save O(n) space.
TC -> O(n log n), SC -> O(1)

#KEY INSIGHT:
- "Optimal" here depends on the variant. For the PRESENCE (yes/no) variant the
  sort + two-pointer wins on space (O(1) vs the hashmap's O(n)), at the cost of an
  O(n log n) sort. For the INDICES variant, sorting throws away the positions you
  need, so the O(n)/O(n) hashmap is the best achievable — there the "better"
  approach IS the optimal one.
"""

from typing import List


class Solution:
    def two_sum_brute(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    break
            if ans:
                break
        return ans

    def two_sum_better(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        ans = []

        for i in range(0, len(nums)):
            if (target - nums[i]) in hashMap:
                ans = [hashMap[target - nums[i]], i]
                break
            hashMap[nums[i]] = i

        return ans

    def two_sum_optimal(self, nums: List[int], target: int) -> bool:
        """
        Use this two-pointer approach ONLY for the presence (yes/no) variant: it is
        O(1) space but sorting destroys the original indices. If indices are
        required, the hashmap ("better") method is the one to use — and is in fact
        optimal there, since no approach can keep indices after sorting.
        Note: this also mutates the caller's array (sorts it in place).
        """
        ans = False
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            value = nums[left] + nums[right]
            if value == target:
                ans = True
                break
            if value > target:
                right -= 1
            else:
                left += 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [2, 6, 5, 8, 11]
    target = 14
    print(sol.two_sum_brute(nums, target))
    nums = [2, 6, 5, 8, 11]
    target = 14
    print(sol.two_sum_better(nums, target))
    nums = [2, 6, 5, 8, 11]
    target = 14
    print(sol.two_sum_optimal(nums, target))
