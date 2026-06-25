# QUESTION: Find the Duplicate Number
# Given an array of N + 1 size, where each element is between 1 and N
# (inclusive). Assuming there is only one duplicate number, find and return
# that duplicate number. You must solve the problem without modifying the
# array nums and uses only constant extra space.
#
# Examples:
# Example 1:
# Input: nums = [1, 3, 4, 2, 2]
# Output: 2
# Explanation: 2 appears twice in the array; all other numbers appear once.
#
# Example 2:
# Input: nums = [3, 1, 3, 4, 2]
# Output: 3
#
# Example 3:
# Input: nums = [1, 1]
# Output: 1
#
# Constraints:
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer
# which appears two or more times.
#
# Follow up: Can you solve the problem in linear runtime O(n) and without
# modifying the array? (Hint: Floyd's Tortoise and Hare cycle detection.)


"""
#Brute Force:
1. Sort the array so equal values become adjacent.
2. Scan from index 1; the first position where nums[i] == nums[i-1] is the
   duplicate, so capture it and stop.
3. Caveat: sorting mutates nums, which this problem explicitly forbids ("without
   modifying the array"), so it's only a baseline.
TC -> O(n log n), SC -> O(1)

#Better Approach:
1. Walk the array once, tallying each value's count in a hashmap.
2. The first value whose running count exceeds 1 is the duplicate — return it
   immediately without scanning the rest.
3. Trade-off: O(n) time, but the hashmap is O(n) extra space, which breaks the
   "constant extra space" constraint.
TC -> O(n), SC -> O(n)

#Optimal Approach (XOR):
1. The array is {1, 2, …, n} with exactly one EXTRA copy of the duplicate (size
   n+1). XOR's self-cancelling property (x ^ x = 0) lets us cancel every value
   against its "expected" counterpart and keep only the surplus.
2. XOR everything together: start ans = nums[0], then for i in 1..n do
   ans ^= nums[i] and ans ^= i. This folds in all array elements AND all the
   numbers 1..n.
3. Each number 1..n contributes once from the index sweep and once from the array
   (those cancel); only the duplicate's extra occurrence is left unpaired, so ans
   ends up equal to the duplicate.
4. O(n) time, O(1) space, and it never modifies the array — but it ONLY works when
   the duplicate appears EXACTLY twice (everything else exactly once). If a value
   repeats 3+ times the cancellation no longer isolates one number (hence the
   "only single duplicate" comment on the method).
TC -> O(n), SC -> O(1)

#Optimal Approach 2 — Floyd's tortoise & hare (the general optimal):
1. Read the array as a linked list: from index i the "next" pointer is nums[i].
   Because values lie in 1..n but there are n+1 indices, two indices must point to
   the same value — so the list contains a cycle, and the node where the cycle
   STARTS is exactly the duplicate value.
2. Phase 1 — detect the cycle: advance slow = nums[slow] one step and
   fast = nums[nums[fast]] two steps; they are guaranteed to meet somewhere inside
   the cycle (the fast pointer eventually laps the slow one).
3. Phase 2 — find the cycle entrance: reset fast to the start (nums[0]), then move
   slow and fast one step each; the point where they meet is the cycle's entrance.
   (Floyd's distance identity: start→entrance equals meeting-point→entrance.)
4. That entrance node is the duplicate. O(n) time, O(1) space, no modification, and
   unlike XOR it works for the general "appears two or more times" case — so this
   is the canonical optimal that satisfies every constraint.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Model the array as the function i -> nums[i]. The duplicate is the one value two
  indices map to, so the functional graph has a cycle whose ENTRANCE is the
  duplicate; Floyd's cycle detection locates it in O(n)/O(1) without touching the
  array. (XOR is a neat O(n)/O(1) shortcut too, but only valid when the duplicate
  occurs exactly twice.)
"""

from typing import List


class Solution:
    def find_the_duplicate_number_brute(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                ans = nums[i]
                break
        return ans

    def find_the_duplicate_number_better(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(0, len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1

            if hashMap[nums[i]] > 1:
                ans = nums[i]
                break
        return ans

    # Only works if single duplicate element in n+1 array
    def find_the_duplicate_number_optimal_variant_i(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(1, len(nums)):
            ans ^= nums[i]
            ans ^= i
        return ans

    # Linked List Based Slow Fast Pointer Approach
    def find_the_duplicate_number_optimal_variant_ii(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 4, 2, 2]
    print(sol.find_the_duplicate_number_brute(nums))
    nums = [1, 3, 4, 2, 2]
    print(sol.find_the_duplicate_number_better(nums))
    nums = [1, 3, 4, 2, 2]
    print(sol.find_the_duplicate_number_optimal_variant_i(nums))
    nums = [1, 3, 4, 2, 2]
    print(sol.find_the_duplicate_number_optimal_variant_ii(nums))
