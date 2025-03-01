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

  def floor(self, arr:List[int], k: int):
    resp = -1

    low, high = 0, len(arr)-1
    while (low <= high):
      mid = low + (high-low) // 2
      if arr[mid] <= k:
        resp = mid
        low = mid + 1
      else:
        high = mid - 1
    return resp
  
  def ceil(self, arr:List[int], k: int):
    resp = len(arr)

    low, high = 0, len(arr)-1
    while (low <= high):
      mid = low + (high-low) // 2
      if arr[mid] >= k:
        resp = mid
        high = mid - 1
      else:
        low = mid + 1
    return resp

if __name__ == "__main__":
  # arr = [3, 4, 4, 7, 8, 10]
  arr = [5, 6, 8, 9, 6, 5, 5, 6]

  resp = Solution().floor(arr, 7)
  print(resp)
  resp = Solution().ceil(arr, 7)
  print(resp)


"""
Ceil
1. Initialize resp = -1, low = 0, high = n-1
2. Initialize while loop until low <= high and calculate mid
3. If array[mid] >= target resp = mid, high = mid - 1
5. Else low = mid + 1
TC -> O(logN), SC -> O(1)

Floor
1. Initialize resp = -1, low = 0, high = n-1
2. Initialize while loop until low <= high and calculate mid
3. If array[mid] <= target resp = mid, low = mid + 1
5. Else high = mid - 1
TC -> O(logN), SC -> O(1)
"""