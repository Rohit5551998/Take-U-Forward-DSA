# QUESTION: Longest Consecutive Sequence in an Array
# Given an array nums of n integers. Return the length of the longest sequence of consecutive
# integers. The integers in this sequence can appear in any order.
#
# Examples:
# Example 1:
# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest sequence of consecutive elements in the array is [1, 2, 3, 4], which
# has a length of 4. This sequence can be formed regardless of the initial order of the
# elements in the array.
#
# Example 2:
# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9
# Explanation: The longest sequence of consecutive elements in the array is
# [0, 1, 2, 3, 4, 5, 6, 7, 8], which has a length of 9.
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9


"""
#Brute Force:
1. We want, for every element, to discover how long a run of consecutive
   integers starts at it. So pick each nums[i] as a candidate start.
2. From that start, ask "does nums[i]+1 exist?" by scanning the whole array
   (linear_search). If yes, ask for +2, then +3, ... extending the run by 1
   each time and stopping the moment the next integer is missing.
3. Track the best run length seen across all starting elements in maxLen.
4. The cost is high because each "does x exist?" check is an O(n) scan, and we
   do that for every step of every run — no use is made of what we already saw.
TC -> O(n^3) worst case (n starts x up to n steps x O(n) search), SC -> O(1)

#Better Approach:
1. The brute force is slow only because membership/order is unknown. Sorting
   fixes that: after nums.sort(), consecutive integers sit next to each other,
   so one linear pass can measure every run.
2. Walk left to right keeping `mini` = the last value we counted into the
   current run, and `cnt` = its length.
3. If nums[i] == mini+1 it continues the current run, so extend: cnt += 1 and
   advance mini. If nums[i] == mini it's a duplicate of the current value, so
   skip it (duplicates must not break or inflate the run).
4. Otherwise nums[i] jumps to a new value with a gap, so a fresh run starts:
   reset cnt = 1 and mini = nums[i].
5. Update maxLen after each element. Sorting dominates the cost.
TC -> O(n log n), SC -> O(1) (ignoring sort's stack)

#Optimal Approach:
1. We can reach O(n) by avoiding the sort and instead getting O(1) membership
   via a hash set built from all elements (duplicates collapse automatically).
2. Key idea: only spend work counting a run from its true starting point. A
   value x is a start iff x-1 is NOT in the set — otherwise some smaller element
   would have counted x already, so we skip x to avoid recounting.
3. When x is a genuine start, walk x+1, x+2, ... while each exists in the set,
   growing cnt, and record maxLen.
4. Although there is a nested while loop, each element is visited by the inner
   loop at most once (only from its own sequence's head), so total work is O(n),
   not O(n^2).
TC -> O(n), SC -> O(n)

#KEY INSIGHT:
- A hash set gives O(1) membership, but the real trick is starting a count ONLY
  at sequence heads (x where x-1 is absent). That guarantees each element is
  walked once, turning a seemingly O(n^2) nested loop into true O(n).
"""

import math
from typing import List


class Solution:
    def linear_search(self, nums: List[int], target: int) -> bool:
        ans = False
        for i in range(0, len(nums)):
            if nums[i] == target:
                ans = True
                break
        return ans

    def longest_consecutive_sequence_in_an_array_brute(self, nums: List[int]) -> int:
        maxLen = 0
        cnt = 0

        for i in range(0, len(nums)):
            cnt = 1
            x = nums[i] + 1
            while self.linear_search(nums, x) == True:
                x += 1
                cnt += 1
            maxLen = max(maxLen, cnt)

        return maxLen

    def longest_consecutive_sequence_in_an_array_better(self, nums: List[int]) -> int:
        nums.sort()
        maxLen = 0
        cnt = 0
        mini = -math.inf

        for i in range(0, len(nums)):
            if nums[i] == mini + 1:
                cnt += 1
                mini += 1
            elif nums[i] == mini:
                continue
            elif nums[i] != mini:
                cnt = 1
                mini = nums[i]
            maxLen = max(maxLen, cnt)

        return maxLen

    def longest_consecutive_sequence_in_an_array_optimal(self, nums: List[int]) -> int:
        hashSet = set()
        cnt = 0
        maxLen = 0

        for i in range(0, len(nums)):
            hashSet.add(nums[i])

        for item in hashSet:
            x = item
            # Do not start counting if current element is not starting point of subsequence
            # i.e. x - 1 exists in hashset
            if (x - 1) in hashSet:
                continue
            cnt = 1
            while (x + 1) in hashSet:
                cnt += 1
                x += 1
            maxLen = max(maxLen, cnt)

        return maxLen


if __name__ == "__main__":
    sol = Solution()
    nums = [102, 1, 101, 4, 3, 2, 100, 2, 1, 4, 1, 2]
    print(sol.longest_consecutive_sequence_in_an_array_brute(nums))
    nums = [102, 1, 101, 4, 3, 2, 100, 2, 1, 4, 1, 2]
    print(sol.longest_consecutive_sequence_in_an_array_better(nums))
    nums = [102, 1, 101, 4, 3, 2, 100, 2, 1, 4, 1, 2]
    print(sol.longest_consecutive_sequence_in_an_array_optimal(nums))
