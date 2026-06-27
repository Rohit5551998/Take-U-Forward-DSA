# QUESTION: Majority Element-II
# Given an integer array nums of size n. Return all elements which appear more than n/3 times in the array. The output can be returned in any order.
#
# Examples:
# Example 1:
# Input: nums = [1, 2, 1, 1, 3, 2]
# Output: [1]
# Explanation: Here, n / 3 = 6 / 3 = 2.
# Therefore, the elements appearing 3 or more times are: [1].
#
# Example 2:
# Input: nums = [1, 2, 1, 1, 3, 2, 2]
# Output: [1, 2]
# Explanation: Here, n / 3 = 7 / 3 = 2.
# Therefore, the elements appearing 3 or more times are: [1, 2].


"""
#Brute Force:
1. We need every value occurring more than n/3 times. The direct way is to count
   each value's occurrences explicitly, like Majority Element-I but collecting
   ALL qualifying values instead of one.
2. For each index i, first skip it if nums[i] is already recorded in ans — this
   avoids counting (and adding) the same value twice.
3. Otherwise scan the rest of the array (j from i+1) counting how many times
   nums[i] appears, starting cnt at 1 to include nums[i] itself.
4. If cnt exceeds n//3, nums[i] is a majority element — append it to ans.
5. Optimization to stop early: at most TWO distinct values can each exceed n/3
   (three such values would total > n elements), so once ans holds 2 elements we
   break immediately.
TC -> O(n^2), SC -> O(1)  (ans holds at most 2 values; the `in ans` check is O(1))

#Better Approach:
1. Replace the repeated inner scans with a single frequency map value -> count,
   built in one pass over the array — each value's total is then known directly.
2. Walk the map's entries and collect every key whose count exceeds n//3 into
   ans. Since at most two values can qualify, break once ans reaches 2.
3. This trades O(n) extra space for the hashmap to bring time down from quadratic
   to linear.
TC -> O(n), SC -> O(n)

#Optimal Approach (Extended Boyer-Moore Voting):
1. At most two values can occur more than n/3 times, so generalize Boyer-Moore
   from one candidate to TWO: track candidates el1, el2 with counters cnt1, cnt2.
2. Intuition: each element either supports one of the two candidates or, if it
   matches neither, cancels one vote from BOTH. A value present > n/3 times has
   too many supporters to be fully cancelled, so it survives as a candidate.
3. Seed el1, el2 with -inf — a marker that can never appear in integer input, so
   an empty slot is never confused with a real value (a plain -1 would break this
   since negatives are valid data).
4. When cnt1 hits 0 the first slot is free, so adopt nums[i] as el1 — but only if
   it isn't already the other candidate el2 (the two slots must stay distinct).
   Symmetrically refill el2 when cnt2 is 0 and nums[i] != el1.
5. Vote for slot 1: if nums[i] == el1 increment cnt1; else (and it's not el2)
   decrement cnt1. Vote for slot 2 the same way against el2.
6. Pass 1 only yields two CANDIDATES, not guaranteed winners. Reset the counters
   and do a second pass counting el1 and el2 for real.
7. Append el1 and/or el2 to the answer only if its true count exceeds n//3.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Strictly fewer than 3 values can each exceed n/3, so two candidates suffice.
  Extended Boyer-Moore keeps two running tallies — a non-matching element cancels
  one vote from each — then a verification pass confirms which candidates are
  genuine. The "no candidate yet" sentinel must be a value that can never appear
  in the input (here -inf), or real data would be mistaken for the empty marker.
"""

import math
from typing import List


class Solution:
    def majority_element_ii_brute(self, nums: List[int]) -> List[int]:
        ans = []
        majority = len(nums) // 3

        for i in range(0, len(nums)):
            cnt = 1

            if nums[i] in ans:
                continue

            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1

            if cnt > majority:
                ans.append(nums[i])

            if len(ans) == 2:
                break

        return ans

    def majority_element_ii_better(self, nums: List[int]) -> List[int]:
        hashMap = {}
        ans = []
        majority = len(nums) // 3

        for i in range(0, len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1

        for k, v in hashMap.items():
            if v > majority:
                ans.append(k)
            if len(ans) == 2:
                break

        return ans

    def majority_element_ii_optimal(self, nums: List[int]) -> List[int]:
        cnt1, cnt2 = 0, 0
        el1, el2 = -math.inf, -math.inf
        ans = []
        majority = len(nums) // 3

        for i in range(0, len(nums)):
            if cnt1 == 0 and nums[i] != el2:
                el1 = nums[i]

            if cnt2 == 0 and nums[i] != el1:
                el2 = nums[i]

            if nums[i] == el1:
                cnt1 += 1
            elif nums[i] != el2:
                cnt1 -= 1

            if nums[i] == el2:
                cnt2 += 1
            elif nums[i] != el1:
                cnt2 -= 1

        cnt1, cnt2 = 0, 0

        for i in range(0, len(nums)):
            if nums[i] == el1:
                cnt1 += 1
            if nums[i] == el2:
                cnt2 += 1

        if cnt1 > majority:
            ans.append(el1)
        if cnt2 > majority:
            ans.append(el2)

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 1, 1, 3, 2, 2]
    print(sol.majority_element_ii_brute(nums))
    nums = [1, 2, 1, 1, 3, 2, 2]
    print(sol.majority_element_ii_better(nums))
    nums = [1, 2, 1, 1, 3, 2, 2]
    print(sol.majority_element_ii_optimal(nums))
