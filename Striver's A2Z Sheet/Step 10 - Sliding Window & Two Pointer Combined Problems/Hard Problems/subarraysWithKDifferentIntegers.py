# mypy: disable-error-code="empty-body"
# QUESTION: Subarrays with K Different Integers
# Given an integer array nums and an integer k, return the number of good
# subarrays of nums. A good array is an array where the number of DIFFERENT
# integers in that array is exactly k.
# (A subarray is a contiguous part of an array.)
#
# Example 1:
# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers:
# [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
#
# Example 2:
# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: [1,2,1,3], [2,1,3], [1,3,4]
#
# Constraints:
# 1 <= nums.length <= 2 * 10^4
# 1 <= nums[i], k <= nums.length

"""
#Brute Force:
1. For every start index i, keep a fresh frequency map and expand j to the right.
2. Insert nums[j] into the map; whenever the map has exactly k distinct keys, this
   window [i..j] is a good subarray, so add 1 to the count.
3. As soon as the distinct count EXCEEDS k, no larger j from this i can ever come
   back to exactly k (integers only get added), so break the inner loop early.
TC -> O(N*N), SC -> O(N)   (map holds at most N distinct values)

#Better Approach:
SKIPPED — no meaningful middle tier exists between the O(N^2) enumeration and the
"exactly = atMost(k) - atMost(k-1)" trick; the trick jumps straight to linear time.

#Optimal Approach:
1. Counting subarrays with EXACTLY k distinct is awkward because a sliding window
   cannot cleanly maintain an "exactly k" invariant. But "AT MOST k distinct" is a
   clean sliding-window count, and:  exactly(k) = atMost(k) - atMost(k-1).
2. atMost(k): expand right, add nums[r] to the map. While distinct > k, shrink from
   the left (decrement / delete keys, advance l). Every valid window ending at r
   contributes (r - l + 1) subarrays, so accumulate that each step.
3. Return atMost(k) - atMost(k-1).
TC -> O(N), SC -> O(N)   (two linear passes)

#KEY INSIGHT:
- "Exactly k" = "at most k" minus "at most k-1". The at-most count is monotonic and
  sliding-window-friendly (widening the window only adds constraints), which is why
  the difference gives an exact count in linear time.
"""

from typing import List


class Solution:
    def subarraysWithKDistinct_brute(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        for i in range(n):
            mpp: dict[int, int] = {}
            for j in range(i, n):
                mpp[nums[j]] = mpp.get(nums[j], 0) + 1
                if len(mpp) == k:
                    cnt += 1
                elif len(mpp) > k:
                    break
        return cnt

    def subarraysWithKDistinct_better(self, nums: List[int], k: int) -> int:
        # SKIP: no distinct middle approach; optimal jumps straight to linear time.
        pass

    def subarraysWithKDistinct_optimal(self, nums: List[int], k: int) -> int:
        return self._countAtMost(nums, k) - self._countAtMost(nums, k - 1)

    def _countAtMost(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        cnt = 0
        left = 0
        mpp: dict[int, int] = {}
        for r in range(len(nums)):
            mpp[nums[r]] = mpp.get(nums[r], 0) + 1
            while len(mpp) > k:
                mpp[nums[left]] -= 1
                if mpp[nums[left]] == 0:
                    del mpp[nums[left]]
                left += 1
            cnt += r - left + 1
        return cnt


if __name__ == "__main__":
    sol = Solution()
    print(sol.subarraysWithKDistinct_optimal([1, 2, 1, 2, 3], 2))  # 7
