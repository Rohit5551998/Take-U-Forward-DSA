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
  def calculateCapacity(self, arr: List[int], capacity: int):
    days = 1
    load = 0
    for i in range(0, len(arr)):
      if (load + arr[i] <= capacity):
        load += arr[i]
      else:
        load = arr[i]
        days += 1
    return days

  def findSolution1(self, arr: List[int], d:int):
    for i in range(max(arr), sum(arr)+1):
      days = self.calculateCapacity(arr, i)
      if (days <= d):
        return i
    return -1

  def findSolution(self, arr: List[int], d:int):
    ans = max(arr)
    low, high = max(arr), sum(arr)
    while (low <= high):
      mid = low + (high - low) // 2
      days = self.calculateCapacity(arr, mid)
      if (days <= d): 
        ans = mid
        high = mid - 1
      else:
        low = mid + 1
    return ans


if __name__ == "__main__":
  arr = [5,4,5,2,3,4,5,6]
  d = 5
  resp = Solution().findSolution(arr, d)
  print(resp)


"""
Capacity to Ship Packages in D Days
Brute Force
1. Run a Loop From Max(arr) to Sum(arr) and calculate total capacity based on each day's load.
2. Inside Calculate Capacity initialize days = 1 and load = 0
use array loop with logic if load + arr[i] < capacity threshold increment load by current weight
3. Else Increment Day By 1 and Set Load to Current Weight
5. If Calculated Capacity is less than or equal to limit return i 
6. At End of Loop Return -1
TC -> O(n * (sum(weights[]) - max(weights[]) + 1)), SC -> O(1)

Optimal Approach
1. Initialize two pointers low = max(arr), high = sum(arr), ans = -1
2. In loop calculate mid = low + (high - low) // 2
3. Inside Calculate Capacity initialize days = 1 and load = 0
use array loop with logic if load + arr[i] < capacity threshold increment load by current weight
4. Else Increment Day By 1 and Set Load to Current Weight4. If Days is greater than d assign low = mid + 1
6. Else high = mid - 1 and ans = mid
7. Return ans.
TC -> O(n * log(sum(weights[]) - max(weights[]) + 1)), SC -> O(1)
"""