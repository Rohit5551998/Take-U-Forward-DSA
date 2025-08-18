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

from queue import PriorityQueue, Queue, LifoQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
  def findSolution1(self, arr):
    totalTrapped = 0
    n = len(arr)
    for i in range(0, len(arr)):
      leftMax = 0
      rightMax = 0
      j = i

      while (j >= 0):
        leftMax = max(leftMax, arr[j])
        j -= 1

      j = i
      while (j < n):
        rightMax = max(rightMax, arr[j])
        j += 1
      
      totalTrapped += min(leftMax, rightMax) - arr[i]
    return totalTrapped

  def findSolution2(self, arr):
    totalTrapped = 0
    n = len(arr)
    leftMax = [0 for _ in range (n)]
    rightMax = [0 for _ in range (n)]

    leftMax[0], rightMax[n-1] = arr[0], arr[n-1]
    for i in range(1, n):
      leftMax[i] = max(leftMax[i-1], arr[i])

    for i in range(n-2, -1, -1):
      rightMax[i] = max(rightMax[i+1], arr[i])

    for i in range(0, len(arr)):
      totalTrapped += min(leftMax[i], rightMax[i]) - arr[i]

    return totalTrapped
  
  def findSolution(self, arr):
    leftMax = 0
    rightMax = 0
    totalTrapped = 0
    left = 0
    right = len(arr) - 1

    while (left < right):
      if (arr[left] <= arr[right]):
        if (arr[left] < leftMax):
          totalTrapped += leftMax - arr[left]
        else:
          leftMax = arr[left]
        left += 1
      else:
        if (arr[right] < rightMax):
          totalTrapped += rightMax - arr[right]
        else:
          rightMax = arr[right]
        right -= 1
    return totalTrapped

if __name__ == "__main__":
  arr = [4, 2, 0, 3, 2, 5]
  print(Solution().findSolution(arr))

"""
Trapping Rainwater
Brute Force
1. Run a loop over the array and initialize leftMax = 0, rightMax = 0 and duplicate pointer with j = i
2. Calculate leftMax by looping through left elements of i and rightMax by looping through right elements
3. Once done calculate total trapped as min of leftMax, rightMax and subtracting current element from it.
TC -> O(N**2), SC -> O(1)

Better Approach
1. Initialize Left Max and Right Max arrays and assign first and last elements of respective arrays
2. Run loops over array to compute remaining elements for leftMax and rightMax arrays
3. Once done compute the total water trapped at each position.
TC -> O(3N), SC -> O(2N)

Optimal Approach
1. Use Two Pointer Approach and initialize leftMax, rightMax, totalTrapped and left pointer to 0 and right pointer to n-1
2. Run a loop while left<right and if arr[left] < leftMax then compute trapped water with leftMax - arr[left] else update
leftMax and increment left
3. Else if arr[right] < rightMax update trapped water with rightMax - arr[right] else update rightMax and decrement right
4. Return Total Trapped Water
TC -> O(N), SC -> O(1)
"""