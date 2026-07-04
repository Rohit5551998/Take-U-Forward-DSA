# QUESTION: Majority Element-I
# Given an integer array nums of size n, return the majority element of the
# array. The majority element of an array is an element that appears more
# than n/2 times in the array. The array is guaranteed to have a majority
# element.
#
# Examples:
# Example 1:
# Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
# Output: 7
# Explanation: The number 7 appears 5 times in the 9-sized array, making it the most frequent element.
#
# Example 2:
# Input: nums = [1, 1, 1, 2, 1, 2]
# Output: 1
# Explanation: The number 1 appears 4 times in the 6-sized array, making it the most frequent element.


"""
#Brute Force:
1. The majority element appears more than n/2 times, so check every candidate
   directly: for each index i, treat nums[i] as the candidate.
2. Scan the rest of the array (j from i+1) and count how many times nums[i]
   repeats, starting the count at 1 to include nums[i] itself.
3. If that count crosses the n/2 threshold (math.floor(n/2)), nums[i] is the
   answer — capture it and stop early. No clever structure, just exhaustive
   pair-counting, which is why it's the baseline.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Trade space for time: do a single pass building a frequency map
   value -> count, so each element's total occurrences is known after one sweep.
2. Walk the map once and return the first key whose count exceeds n/2. This
   removes the inner counting loop of the brute force, dropping time to linear.
3. Cost: the hashmap can hold up to n distinct keys, so the speed-up comes at
   O(n) extra space.
TC -> O(n), SC -> O(n)

#Optimal Approach (Boyer-Moore Voting):
1. Intuition: if one value occupies more than half the array, then pairing up
   each of its occurrences with a *different* value cancels both out — and the
   majority still has leftovers. So a running "vote" tally can never be fully
   cancelled by the minority.
2. Track a single candidate `element` (seeded with nums[0]) and a `count`
   (seeded at 1). Walk from index 1 to the end.
3. Whenever `count` drops to 0 the current candidate has been fully out-voted,
   so adopt the current element nums[i] as the new candidate before voting.
4. Vote: if nums[i] equals the candidate increment `count` (a supporting vote),
   otherwise decrement it (an opposing vote that cancels one supporter).
5. After the pass, `element` is the ONLY possible majority. Do a second pass to
   actually count it and confirm it exceeds n/2 before returning (here it's
   guaranteed to exist, but the verify step makes the routine safe in general).
6. Both passes are linear and only a couple of scalars are stored, so it beats
   the hashmap on space.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- A value present > n/2 times cannot be cancelled out: pair every majority
  occurrence against a distinct non-majority one and the majority survives.
  Boyer-Moore turns that into a single running counter, finding the candidate in
  O(n) time and O(1) space without sorting or extra memory.
"""

import math
from typing import List, Optional


class Solution:
    def majority_element_i_brute(self, nums: List[int]) -> Optional[int]:
        majority = math.floor(len(nums) / 2)
        ans = None

        for i in range(0, len(nums)):
            count = 1
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count > majority:
                ans = nums[i]
                break
        return ans

    def majority_element_i_better(self, nums: List[int]) -> Optional[int]:
        majority = math.floor(len(nums) / 2)
        hashMap = {}
        ans = None

        for i in range(0, len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1

        for k, v in hashMap.items():
            if v > majority:
                ans = k
                break

        return ans

    def majority_element_i_optimal(self, nums: List[int]) -> Optional[int]:
        majority = math.floor(len(nums) / 2)
        ans = None
        element = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                element = nums[i]

            if element == nums[i]:
                count += 1
            else:
                count -= 1

        count = 0
        for i in range(0, len(nums)):
            if nums[i] == element:
                count += 1
            if count > majority:
                ans = element
                break
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
    print(sol.majority_element_i_brute(nums))
    nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
    print(sol.majority_element_i_better(nums))
    nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
    print(sol.majority_element_i_optimal(nums))
