from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter


class Solution:   

  def findSolution1(self, arr:List[int]):
    maxSum = -math.inf;
    for i in range(0, len(arr)):
      for j in range(i, len(arr)):
        sum = 0
        for k in range(i, j+1):
          sum += arr[k]
        maxSum = max(maxSum, sum)
    return maxSum
  
  def findSolution2(self, arr:List[int]):
    maxSum = -math.inf;
    for i in range(0, len(arr)):
      sum = 0
      for j in range(i, len(arr)):
        sum += arr[j]
        maxSum = max(maxSum, sum)
    return maxSum
    
  def findSolution(self, arr: List[int]):
    maxSum = -math.inf
    start = -1
    ansStart, ansEnd = -1, -1
    sum = 0
    for i in range(len(arr)):
      if (sum < 0):
        sum = 0
        start = i

      sum += arr[i]

      if (sum > maxSum):
        maxSum = sum
        ansStart = start
        ansEnd = i

    print("Subarray with Max Sum: ", arr[ansStart:ansEnd+1])
    return maxSum

if __name__ == "__main__":
  arr = [-2,1,-3,4,-1,2,1,-5,4]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Brute Force:
Calculate Sum of All Subarrays Using 3 Loops
TC: O(n**3) SC: O(1)

Better Approach:
Calculate Sum of All Subarrays Using 2 Loops and add the current element to the sum of previous subarray
to get the sum of current subarray instead of using another loop each time
TC: O(n**2), SC: O(1)

Optimal Approach (Kadane's Algorithm):
1. Initialize 3 variables: max_sum, current_sum, start_index = 0, ans_start_index = -1, ans_end_index = -1
2. Iterate through the array and add the current element to the current_sum
3. If the current_sum is less than 0, reset the current_sum to 0 and update the start_index to the next element
4. If the current_sum is greater than the max_sum, update the max_sum and ans_start_index and ans_end_index
as start_index and current index respectively
5. Return the subarray from ans_start_index to ans_end_index or return the max_sum as per question
TC: O(n) SC: O(1)
"""