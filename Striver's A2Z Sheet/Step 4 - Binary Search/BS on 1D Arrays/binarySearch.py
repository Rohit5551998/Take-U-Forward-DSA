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

  def findSolution1(self, arr:List[int], k: int):
    resp = -1

    low, high = 0, len(arr)-1
    while (low <= high):
      mid = low + (high - low) // 2
      if arr[mid] == k:
        resp = mid
        break
      elif arr[mid] < k:
        low = mid + 1
      else:
        high = mid - 1
    return resp
  
  def binarySearch(self, arr: List[int], low: int, high: int, k: int):
    if low > high:
      return -1
    mid = (int)((low + high) / 2)
    if arr[mid] == k:
      return mid
    elif arr[mid] < k:
      return self.binarySearch(arr, mid + 1, high, k)
    else:
      return self.binarySearch(arr, low, mid - 1, k)

  def findSolution(self, arr:List[int], k: int):
    return self.binarySearch(arr, 0, len(arr) - 1, k)


if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  resp = Solution().findSolution(arr, 4)
  print(resp)


"""
Binary Search
1. Initialize resp = -1, low = 0, high = n-1
2. Initialize while loop until low <= high and calculate mid
3. If array[mid] == target return mid
4. Else If it is less than target low = mid + 1
5. Else high = mid - 1
TC -> O(logN), SC -> O(1)
"""