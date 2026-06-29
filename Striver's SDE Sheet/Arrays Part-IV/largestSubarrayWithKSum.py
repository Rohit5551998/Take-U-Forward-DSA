# QUESTION: Largest Subarray with K sum
# Given an array containing both positive and negative integers, find the length of the longest subarray whose elements sum to a given value k.


"""
NOTE: "Better" vs "Optimal" here depends on the input:
- General array (positives AND negatives): the prefix-sum + hashMap below is the
  true OPTIMAL (sliding window cannot be used — see why in the Optimal section).
- Positives-only array: the sliding window is OPTIMAL (O(1) space) and the hashMap
  is merely BETTER (it still pays O(n) space). The tier labels follow this latter case.

#Brute Force:
1. The length of the longest subarray summing to k is unknown, so just try every
   subarray. Fix a start index i, then extend an end index j from i rightward.
2. Maintain a running `sum` as j moves so each extension is O(1) — no need to
   re-add from scratch. sum now holds the sum of nums[i..j].
3. Whenever sum == k, this subarray is a candidate; update maxLen with its
   length (j - i + 1). Keep going (a longer one summing to k may appear later
   for this same i, e.g. trailing zeros).
4. Repeat for every start i. Two nested loops over the array give the cost.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Instead of re-summing subarrays, use prefix sums: prefixSum at index i is the
   sum of nums[0..i]. A subarray (j+1..i) sums to k iff prefixSum[i] - prefixSum[j] == k.
2. Rearrange: prefixSum[j] == prefixSum[i] - k. So as we sweep i, we ask "have we
   seen a prefix sum equal to (current prefixSum - k) before?" — an O(1) hashMap lookup.
3. hashMap maps a prefix-sum value -> the EARLIEST index where it occurred. Earliest,
   because we want the longest subarray, so the largest (i - j) span.
4. Edge case: if prefixSum itself == k, the whole prefix nums[0..i] is valid, length i+1.
5. Compute rem = prefixSum - k; if rem is in the map, candidate length is i - hashMap[rem];
   update maxLen.
6. Only insert prefixSum if it's NOT already present — keeping the first (smallest)
   index. This is what correctly handles 0s / repeated prefix sums for the LONGEST span.
TC -> O(n), SC -> O(n)

#Optimal Approach:
1. (Positives only.) Use a sliding window [left, right] and grow it from the right,
   keeping `sum` = sum of the current window.
2. Add nums[right] FIRST, then shrink from the left while sum > k. Adding before
   shrinking is essential: it lets the just-included element trigger the trim, so
   a window that only becomes valid after trimming is checked this same iteration.
   (Shrinking before the add misses such windows — e.g. [2,2,3], k=3.)
3. After shrinking, if sum == k the window is valid; update maxLen with right-left+1.
4. Advance right and repeat. Each index enters the window once (right++) and leaves
   at most once (left++), so total work is O(2n).
5. Why positives only: with negatives, a window's sum can be > k yet a LONGER valid
   window may still lie ahead, so shrinking on sum > k would wrongly discard it.
   That is exactly why the general case needs the prefix-sum + hashMap approach.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- For positives, monotonic growth lets a two-pointer window shrink safely (sum only
  grows when you extend, only shrinks when you trim) → O(1) space. The moment
  negatives appear that monotonicity breaks, and the prefix-sum identity
  prefixSum[j] = prefixSum[i] - k (earliest index wins for longest span) becomes the
  only reliable O(n) tool.
"""

from typing import List


class Solution:
    def largest_subarray_with_k_sum_brute(self, nums: List[int], k: int) -> int:
        maxLen = 0

        for i in range(0, len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum += nums[j]

                if sum == k:
                    maxLen = max(maxLen, (j - i + 1))

        return maxLen

    # Optimal for Sum with Positives + Negatives, Better for only Positives
    def largest_subarray_with_k_sum_better(self, nums: List[int], k: int) -> int:
        maxLen = 0
        hashMap = {}
        prefixSum = 0

        for i in range(0, len(nums)):
            prefixSum += nums[i]

            # Whole prefix nums[0..i] already sums to k -> candidate length i + 1.
            # (No earlier prefix of 0 is stored, so this case is handled explicitly.)
            if prefixSum == k:
                maxLen = max(maxLen, i + 1)

            # A subarray (j+1..i) sums to k iff prefixSum[i] - prefixSum[j] == k.
            # So look for an earlier prefix equal to rem = prefixSum - k; if found,
            # the subarray after that index sums to k.
            rem = prefixSum - k

            if rem in hashMap:
                maxLen = max(maxLen, i - hashMap[rem])

            # Store the EARLIEST index for each prefix-sum value (don't overwrite),
            # since the longest subarray needs the smallest j -> largest span.
            # This is also what keeps repeated sums / 0s working correctly.
            if prefixSum not in hashMap:
                hashMap[prefixSum] = i

        return maxLen

    # Only works for Positive Elements
    def largest_subarray_with_k_sum_optimal(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        maxLen = 0
        sum = 0

        while (right < len(nums)):
            sum += nums[right]

            while left <= right and sum > k:
                sum -= nums[left]
                left += 1

            if sum == k:
                maxLen = max(maxLen, right - left + 1)

            right += 1

        return maxLen


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 0, 1, 0, 1, 1, 3, 2, 1, 3, 1]
    k = 3
    print(sol.largest_subarray_with_k_sum_brute(nums, k))
    nums = [1, 2, 3, 0, 1, 0, 1, 1, 3, 2, 1, 3, 1]
    k = 3
    print(sol.largest_subarray_with_k_sum_better(nums, k))
    nums = [1, 2, 3, 0, 1, 0, 1, 1, 3, 2, 1, 3, 1]
    k = 3
    print(sol.largest_subarray_with_k_sum_optimal(nums, k))
