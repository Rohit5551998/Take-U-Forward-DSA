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
  def calculateSumOfDivisor(self, arr: List[int], divisor: int):
    sum = 0
    for i in range(0, len(arr)):
      sum += math.ceil(arr[i] / divisor)
    return sum

  def findSolution1(self, arr: List[int], limit:int):
    for i in range(1, max(arr)):
      sum = self.calculateSumOfDivisor(arr, i)
      if (sum <= limit):
        return i
    return -1

  def findSolution(self, arr: List[int], limit:int):
    ans = -1
    low, high = 1, max(arr)
    while (low <= high):
      mid = low + (high - low) // 2
      sum = self.calculateSumOfDivisor(arr, mid)
      if (sum <= limit): 
        ans = mid
        high = mid - 1
      else:
        low = mid + 1
    return ans


if __name__ == "__main__":
  arr = [1,2,3,4,5]
  limit = 8
  # arr = [8,4,2,3]
  # limit = 10
  resp = Solution().findSolution(arr, limit)
  print(resp)


"""
Find Smallest Divisor For Threshold
Brute Force
1. Run a Loop From 1 to Max(arr) and calculate sum after division from current divisor.
2. Inside Calculate Sum of Divisors do the operation sum += ceil(arr[i]/divisor)
3. If Sum is less than or equal to m return i 
4. At End of Loop Return -1
TC -> O(max(arr[])*N), SC -> O(1)

Optimal Approach
1. Initialize two pointers low = 1, high = max(arr), ans = -1
2. In loop calculate mid = low + (high - low) // 2
3. Inside Calculate Sum of Divisors do the operation sum += ceil(arr[i]/divisor)
4. If Sum is less than or equal to m return i 
5. At End of Loop Return -1
6. Return ans.
TC -> O(log(max(arr[]))*N), SC -> O(1)
"""