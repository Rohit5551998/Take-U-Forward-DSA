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

  def calculateRootTillN(self, mid: int, k: int, n: int):
    product = 1
    for _ in range(1, n+1):
      product *= mid
      if (product > k): return 2
    if (product == k): return 1
    return 0

  def findSolution(self, n:int, k: int):
    low, high = 0, k
    ans = -1
    while (low <= high):
      mid = low + (high - low) // 2
      value = self.calculateRootTillN(mid, k, n)
      if (value == 1):
        return mid
      elif (value == 2):
        high = mid - 1
      else:
        low = mid + 1
    return ans


if __name__ == "__main__":
  resp = Solution().findSolution(4, 81)
  print(resp)


"""
Find Nth Root of Number if it exists
Optimal Approach
1. Initialize two pointers low = 0, high = n - 1
2. In loop calculate mid = low + (high - low) // 2
3. Check if mid ** n  == k, assign it to ans and assign it to ans and return it
Since it can be huge use for loop to calculate till < k.
4. If mid ** n < k, low = mid + 1
5. Else assign high = mid - 1
6. Return ans.
TC -> O(log(n)), SC -> O(1)
"""