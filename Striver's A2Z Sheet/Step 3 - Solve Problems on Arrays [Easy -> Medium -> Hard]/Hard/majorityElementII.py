# mypy: disable-error-code="empty-body"
# QUESTION: Majority Element II (> n/3 times)
# Given an array nums of size n, return all elements that appear more than n/3
# times. At most two such elements can exist.
# Example 1:
# Input: nums = [11, 33, 22, 33, 11, 33, 11, 22]
# Output: [11, 33]
# Explanation: n = 8, n/3 = 2. Both 11 and 33 appear 3 times (> 2).
# Constraints:
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9

"""
#Brute Force:
1. For each element (skipping ones already collected) count its occurrences with
   an inner loop.
2. If a count exceeds n/3 add it to the answer; stop once two are found.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Build a frequency hashmap in one pass.
2. Add an element to the answer the moment its running count reaches floor(n/3)+1.
TC -> O(n), SC -> O(n)

#Optimal Approach (Extended Boyer-Moore Voting):
1. There can be at most two elements above n/3, so keep two candidates and two
   counters.
2. For each element: if it matches a candidate bump that counter; else if a
   counter is 0 (and the element isn't the other candidate) adopt it; otherwise
   decrement both counters.
3. Candidates are only *potential* winners, so re-count both in a second pass and
   keep those actually exceeding n/3.
TC -> O(2n), SC -> O(1)

#KEY INSIGHT:
- At most two values can each exceed n/3; two vote counters cancel out everything
  else, leaving the two candidates that only need a verification pass.
"""

from typing import List


class Solution:
    def majority_ii_brute(self, nums: List[int]) -> List[int]:
        ans: List[int] = []
        threshold = len(nums) // 3
        for i in range(len(nums)):
            if nums[i] not in ans:
                cnt = 1
                for j in range(i + 1, len(nums)):
                    if nums[j] == nums[i]:
                        cnt += 1
                if cnt > threshold:
                    ans.append(nums[i])
            if len(ans) == 2:
                break
        return ans

    def majority_ii_better(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        freq: dict[int, int] = {}
        ans: List[int] = []
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            if freq[nums[i]] == threshold + 1:
                ans.append(nums[i])
        return ans

    def majority_ii_optimal(self, nums: List[int]) -> List[int]:
        cnt1, cnt2 = 0, 0
        el1, el2 = float("-inf"), float("-inf")
        for i in range(len(nums)):
            if cnt1 == 0 and nums[i] != el2:
                el1 = nums[i]
                cnt1 += 1
            elif cnt2 == 0 and nums[i] != el1:
                el2 = nums[i]
                cnt2 += 1
            elif nums[i] == el1:
                cnt1 += 1
            elif nums[i] == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        ans: List[int] = []
        cnt1, cnt2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == el1:
                cnt1 += 1
            if nums[i] == el2:
                cnt2 += 1
        if cnt1 > len(nums) // 3:
            ans.append(int(el1))
        if cnt2 > len(nums) // 3:
            ans.append(int(el2))
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.majority_ii_optimal([11, 33, 22, 33, 11, 33, 11, 22]))
