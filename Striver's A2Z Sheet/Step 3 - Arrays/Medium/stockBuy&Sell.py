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
    maxProfit = 0

    for i in range(0, len(arr)):
      for j in range(i + 1, len(arr)):
        maxProfit = max(maxProfit, arr[j] - arr[i])

    return maxProfit
  
  def findSolution(self, arr:List[int]):
    maxProfit = 0
    mini = arr[0]
    for i in range(1, len(arr)):
      maxProfit = max(maxProfit, arr[i] - mini)
      mini = min(mini, arr[i])
    return maxProfit

if __name__ == "__main__":
  arr = [7, 1, 5, 3, 6, 4]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Stock Buy & Sell Problem:

Brute Force:
1. Run Two Nested Loops and Find Profit on Each Day
2. If Profit is Greater than Max Profit, Update Max Profit
TC -> O(n**2), SC -> O(1)

Optimal Approach:
1. Run a single loop and keep track of minPrice till ith element and maxProfit
2. Calculate profit on each day and update maxProfit if profit is greater than maxProfit
3. Update minPrice if price on ith day is less than minPrice
TC -> O(n), SC -> O(1)
"""