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
  def calculateTotalHours(self, arr: List[int], rate: int):
    hours = 0
    for i in range(0, len(arr)):
      hours += math.ceil(arr[i]/rate)
    return hours

  def findSolution1(self, arr: List[int], k:int):
    for i in range(1, max(arr)+1):
      hours = self.calculateTotalHours(arr, i)
      if (hours <= k):
        return i
    return -1

  def findSolution(self, arr: List[int], k:int):
    ans = max(arr)
    low, high = 1, max(arr)
    while (low <= high):
      mid = low + (high - low) // 2
      hours = self.calculateTotalHours(arr, mid)
      if (hours <= k): 
        ans = mid
        high = mid - 1
      else:
        low = mid + 1
    return ans


if __name__ == "__main__":
  arr = [7, 15, 6, 3]
  h = 8
  resp = Solution().findSolution(arr, h)
  print(resp)


"""
Koko Eating Bananas
Brute Force
1. Run a Loop From 1 to Max(arr) and calculate total hours for each hourly rate.
2. Inside Calculate Total Hours use array loop with logic hours += ceil(arr[i]/rate)
3. If the returned hours is less than k (limit) then return it
4. At end of loop return -1
TC -> O(max(arr)*n), SC -> O(1)

Optimal Approach
1. Initialize two pointers low = 1, high = max(arr), ans = max(arr)
2. In loop calculate mid = low + (high - low) // 2
3. Calculate Total Hours for Mid and If value is less than k assign it to ans and eliminate right half with high = mid - 1
4. Else assign low = mid + 1
5. Return ans.
TC -> O(log(n)), SC -> O(1)
"""