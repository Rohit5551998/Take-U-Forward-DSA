# mypy: disable-error-code="empty-body"
# QUESTION: Binary Subarrays With Sum
# Given a binary array nums and an integer goal, return the number of non-empty
# subarrays with a sum equal to goal.
# Example 1:
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are [1,0,1], [1,0,1,0] (wait) -> the four with sum 2:
#   [1,0,1], [1,0,1,0], [0,1,0,1], [1,0,1] (indices vary). Total = 4.
# Example 2:
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15
# Constraints:
# 1 <= nums.length <= 3 * 10^4
# nums[i] is 0 or 1.
# 0 <= goal <= nums.length

"""
#Brute Force:
1. Two loops pick every subarray [i..j]; a third sums it.
2. Count subarrays whose sum equals goal.
Why: exhaustive; correct but cubic.
TC -> O(N^3), SC -> O(1)

#Better Approach (prefix-sum hashing):
1. Walk once keeping running preSum and a map count[preSum -> occurrences], seeded {0:1}.
2. At each step add count[preSum - goal] (each such earlier prefix marks a subarray
   summing to goal).
3. Increment count[preSum].
Why: turns "find subarray of sum goal" into "find earlier prefix equal to preSum-goal".
TC -> O(N), SC -> O(N)

#Optimal Approach (two-pointer, count <= goal trick):
1. Define f(x) = number of subarrays with sum <= x via a sliding window
   (grow r adding nums[r]; while sum > x shrink l; add r-l+1).
2. Answer = f(goal) - f(goal-1)  (exactly-goal = atMost(goal) - atMost(goal-1)).
3. Guard f(x)=0 when x < 0.
Why: exactly-K is the difference of two atMost-K windows; each window is O(N), O(1) space.
TC -> O(N), SC -> O(1)

#KEY INSIGHT:
- "Exactly goal" = atMost(goal) - atMost(goal-1); atMost is a clean monotonic
  sliding window on a non-negative (binary) array.
"""

from typing import List


class Solution:
    def numSubarraysWithSum_brute(self, nums: List[int], goal: int) -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                total = sum(nums[i : j + 1])
                if total == goal:
                    cnt += 1
        return cnt

    def numSubarraysWithSum_better(self, nums: List[int], goal: int) -> int:
        cnt = 0
        prefix: dict[int, int] = {0: 1}
        preSum = 0
        for num in nums:
            preSum += num
            cnt += prefix.get(preSum - goal, 0)
            prefix[preSum] = prefix.get(preSum, 0) + 1
        return cnt

    def _atMost(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        cnt = 0
        left = 0
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum > k:
                currSum -= nums[left]
                left += 1
            cnt += r - left + 1
        return cnt

    def numSubarraysWithSum_optimal(self, nums: List[int], goal: int) -> int:
        return self._atMost(nums, goal) - self._atMost(nums, goal - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubarraysWithSum_optimal([1, 0, 1, 0, 1], 2))
