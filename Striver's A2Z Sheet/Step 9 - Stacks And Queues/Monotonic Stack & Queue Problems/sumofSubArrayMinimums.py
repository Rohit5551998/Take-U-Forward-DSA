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


  def findSolution(self, arr):
    mod = int(1e9+7)
    sum = 0
    nse = self.findNSE(arr)
    psee = self.findPSEE(arr)

    for i in range(0, len(arr)):
      left = i - psee[i]
      right = nse[i] - i

      sum += (((right * left) % mod) * arr[i])%mod
      sum %= mod

    return sum
    

if __name__ == "__main__":
  # arr = [3, 1, 2, 4]
  # arr = [1, 1]
  arr = [11,81,94,43,3]
  print(Solution().findSolution(arr))

"""
Sum of Subarray Minimums
Brute Force
1. Run two nested loops and generate all subarrays and compute min of each subarray.
2. Once done add it to final ans.
TC -> O(N**2), SC -> O(1)

Optimal Approach
1. Find NSE and PSEE index for a particular element and if not found assign n and -1 respectively.
2. Once done calculate no of contributions for smaller element from i.
3. Add (right * left * arr[i]) as the total minimum contribution for a particular element and return the sum
TC -> O(3N), SC -> O(2N)
"""