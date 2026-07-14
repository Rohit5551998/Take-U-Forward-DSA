# mypy: disable-error-code="empty-body"
# QUESTION: Majority Element (> n/2 times)
# Given an array nums of size n, return the element that appears more than n/2
# times. The majority element is guaranteed to exist.
# Example 1:
# Input: nums = [2, 2, 1, 1, 1, 2, 2]
# Output: 2
# Explanation: 2 appears 4 times which is more than 7/2 = 3.
# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

"""
#Brute Force:
1. For each element count how many times it appears using an inner loop.
2. Return the first element whose count exceeds n/2.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Build a frequency hashmap in one pass.
2. Return the key whose count exceeds n/2.
TC -> O(n), SC -> O(n)

#Optimal Approach (Boyer-Moore Voting):
1. Keep a candidate and a counter. Start counter at 0.
2. When counter hits 0 adopt the current element as the new candidate.
3. Increment the counter if the current element equals the candidate, else
   decrement it — opposite votes cancel out.
4. A true majority element (> n/2) survives all cancellations, so the final
   candidate is the answer. (Optionally re-verify with a second pass.)
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Because a > n/2 element outnumbers everything else combined, pairing off each
  of its votes with a different value can never zero it out — the last standing
  candidate must be it.
"""

from typing import List


class Solution:
    def majority_brute(self, nums: List[int]) -> int:
        half = len(nums) // 2
        for i in range(len(nums)):
            cnt = 1
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    cnt += 1
            if cnt > half:
                return nums[i]
        return -1

    def majority_better(self, nums: List[int]) -> int:
        half = len(nums) // 2
        freq: dict[int, int] = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        for key, value in freq.items():
            if value > half:
                return key
        return -1

    def majority_optimal(self, nums: List[int]) -> int:
        counter, candidate = 0, nums[0]
        for i in range(len(nums)):
            if counter == 0:
                candidate = nums[i]
                counter = 1
            elif nums[i] == candidate:
                counter += 1
            else:
                counter -= 1
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == candidate:
                cnt += 1
        return candidate if cnt > len(nums) // 2 else -1


if __name__ == "__main__":
    sol = Solution()
    print(sol.majority_optimal([2, 2, 1, 1, 1, 2, 2]))
