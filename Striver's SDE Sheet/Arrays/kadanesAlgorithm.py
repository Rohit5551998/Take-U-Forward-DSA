# QUESTION: Kadane's Algorithm
# Given an integer array nums, find the subarray with the largest sum and
# return the sum of the elements present in that subarray. A subarray is a
# contiguous non-empty sequence of elements within an array.
#
# Examples:
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.


"""
#Brute Force:
1. Enumerate every possible subarray by fixing a start i and an end j (j >= i).
2. For each (i, j) pair, compute that subarray's sum from scratch with a third
   loop over k from i..j, and keep the running maximum `maxi`.
   The reason this is the naive baseline: we re-add the same elements again and
   again for overlapping subarrays, so almost all the work is repeated.
TC -> O(n^3), SC -> O(1)

#Better Approach:
1. Still fix a start i, but instead of a third loop, extend the end j one
   element at a time while maintaining a running `sum`.
2. The sum for subarray (i, j) is just the sum for (i, j-1) plus arr[j], so we
   reuse prior work instead of recomputing — that removes the innermost loop.
3. Update `maxi` on every extension.
TC -> O(n^2), SC -> O(1)

#Optimal Approach:
1. Walk the array once, carrying a running `sum` of the current subarray.
2. Whenever `sum` exceeds `maxi`, record it as the best so far (and capture the
   subarray's start/end via `start`/`ansStart`/`ansEnd`).
3. The moment `sum` drops below 0, reset it to 0: a negative running prefix can
   only drag down any subarray we'd build to its right, so we abandon it and let
   the next index begin a fresh subarray (start = i when sum == 0).
4. Because each position considers the best subarray ending there, one pass
   suffices.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- A running sum that has gone negative can never improve a future subarray's
  total, so reset it to 0 and start fresh; tracking max-so-far during the single
  pass yields the answer in O(n).
"""
from typing import List

def kadanes_algorithm_brute(arr: List[int]) -> int:
    maxi = arr[0]
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            sum = 0
            for k in range(i, j+1):
                sum += arr[k]
            maxi = max(maxi, sum)
    return maxi 


def kadanes_algorithm_better(arr: List[int]) -> int:
    maxi = arr[0]
    for i in range(0, len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            maxi = max(maxi, sum)
    return maxi 


def kadanes_algorithm_optimal(arr: List[int]) -> int:
    sum = 0
    start = 0
    ansStart = 0
    ansEnd = 0
    maxi = arr[0]

    for i in range(0, len(arr)):

        if (sum == 0):
            start = i

        sum += arr[i]

        if (sum > maxi):
            ansStart = start
            ansEnd = i
            maxi = sum

        if (sum < 0):
            sum = 0

    print(ansStart, ansEnd)
    return maxi



arr = [-2,1,-3,4,-1,2,1,-5,4]
print(kadanes_algorithm_brute(arr))
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(kadanes_algorithm_better(arr))
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(kadanes_algorithm_optimal(arr))