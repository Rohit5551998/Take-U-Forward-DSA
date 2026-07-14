# mypy: disable-error-code="empty-body"
# QUESTION: Count Number of Nice Subarrays
# Given an array of integers nums and an integer k, a continuous subarray is called
# "nice" if it contains exactly k odd numbers. Return the number of nice subarrays.
# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The nice subarrays are [1,1,2,1] and [1,2,1,1].
# Example 2:
# Input: nums = [2,4,6], k = 1
# Output: 0
# Constraints:
# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length

"""
#Brute Force:
1. Two loops pick every subarray; a third counts odd numbers in it.
2. Count subarrays whose odd-count equals k.
Why: exhaustive check of the "exactly k odds" rule.
TC -> O(N^3), SC -> O(1)

#Better Approach (prefix-count hashing):
1. Map each element to (element % 2), so the problem becomes "subarrays with sum == k".
2. Walk keeping running count of odds and a map preCount[sum -> occurrences], seeded {0:1}.
3. Add preCount[running - k] at each step, then bump preCount[running].
Why: reduces "exactly k odds" to the classic "subarray sum equals k" via parity.
TC -> O(N), SC -> O(N)

#Optimal Approach (two-pointer, atMost trick):
1. f(x) = number of subarrays with at most x odd numbers, via a sliding window on parity.
2. Answer = f(k) - f(k-1); guard f(x)=0 when x < 0.
Why: exactly-k = atMost(k) - atMost(k-1); each window is O(N) with O(1) extra space.
TC -> O(N), SC -> O(1)

#KEY INSIGHT:
- Treat odd as 1, even as 0; then "exactly k odds" is identical to
  "binary subarrays with sum k", solvable by atMost(k) - atMost(k-1).
"""

from typing import List


class Solution:
    def numberOfSubarrays_brute(self, nums: List[int], k: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                odds = sum(1 for x in nums[i : j + 1] if x % 2 == 1)
                if odds == k:
                    cnt += 1
        return cnt

    def numberOfSubarrays_better(self, nums: List[int], k: int) -> int:
        cnt = 0
        preCount: dict[int, int] = {0: 1}
        running = 0
        for num in nums:
            running += num % 2
            cnt += preCount.get(running - k, 0)
            preCount[running] = preCount.get(running, 0) + 1
        return cnt

    def _atMost(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        cnt = 0
        left = 0
        oddCount = 0
        for r in range(len(nums)):
            oddCount += nums[r] % 2
            while oddCount > k:
                oddCount -= nums[left] % 2
                left += 1
            cnt += r - left + 1
        return cnt

    def numberOfSubarrays_optimal(self, nums: List[int], k: int) -> int:
        return self._atMost(nums, k) - self._atMost(nums, k - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSubarrays_optimal([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
