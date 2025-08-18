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
    sum = 0
    for i in range(0, len(arr)):
      mini = math.inf
      for j in range(i, len(arr)):
        mini = min(mini, arr[j])
        sum += (mini % (1e10+7))
    return int(sum)    
  
  def findNSE(self, arr):
    stack = LifoQueue()
    nse = [0 for _ in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
      while (not stack.empty() and arr[i] <= arr[stack.queue[-1]]):
        stack.get()
      nse[i] = stack.queue[-1] if not stack.empty() else len(arr)
      stack.put(i)
    return nse
      
  def findPSEE(self, arr):
    stack = LifoQueue()
    psee = [0 for _ in range(len(arr))]
    for i in range(0, len(arr)):
      while (not stack.empty() and arr[i] < arr[stack.queue[-1]]):
        stack.get()
      psee[i] = stack.queue[-1] if not stack.empty() else -1
      stack.put(i)
    return psee


  def findNGE(self, arr):
    stack = LifoQueue()
    nse = [0 for _ in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
      while (not stack.empty() and arr[i] >= arr[stack.queue[-1]]):
        stack.get()
      nse[i] = stack.queue[-1] if not stack.empty() else len(arr)
      stack.put(i)
    return nse
      
  def findPGEE(self, arr):
    stack = LifoQueue()
    psee = [0 for _ in range(len(arr))]
    for i in range(0, len(arr)):
      while (not stack.empty() and arr[i] > arr[stack.queue[-1]]):
        stack.get()
      psee[i] = stack.queue[-1] if not stack.empty() else -1
      stack.put(i)
    return psee

  def findSolution(self, arr):
    minSum, maxSum = 0, 0
    mod = int(1e9+7)
    nse = self.findNSE(arr)
    psee = self.findPSEE(arr)
    nge = self.findNGE(arr)
    pgee = self.findPGEE(arr)

    for i in range(0, len(arr)):
      left1 = i - psee[i]
      right1 = nse[i] - i
      left2 = i - pgee[i]
      right2 = nge[i] - i

      minSum += (((right1 * left1) % mod) * arr[i]) % mod
      maxSum += (((right2 * left2) % mod) * arr[i]) % mod

      # minSum %= mod
      # maxSum %= mod

    return int(maxSum - minSum)
    

if __name__ == "__main__":
  # arr = [1, 2, 3]
  # arr = [1, 3, 3]
  arr = [4,-2,-3,4,1]
  print(Solution().findSolution(arr))

"""
Sum of Subarray Minimums
Brute Force
1. Run two nested loops and generate all subarrays and compute min of each subarray.
2. Once done add it to final ans.
TC -> O(N**2), SC -> O(1)

Optimal Approach
1. Find NSE and PSEE index for a particular element and if not found assign n and -1 respectively.
2. Find NGE and PGEE index for a particular element and if not found assign n and -1 respectively.
2. Once done calculate no of contributions for smaller element from i and larger element from i.
3. Add (right1 * left1 * arr[i]) as the total minimum contribution for a particular element and add it to minSum
4. Add (right2 * left2 * arr[i]) as the total maximum contribution for a particular element and add it to maxSum
5. Return maxSum - minSum
TC -> O(5N), SC -> O(4N)
"""