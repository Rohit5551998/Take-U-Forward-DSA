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

  def firstOccurence(self, arr:List[int], k: int):
    resp = -1

    low, high = 0, len(arr)-1
    while (low <= high):
      mid = low + (high-low) // 2
      if arr[mid] == k:
        resp = mid
        high = mid - 1
      elif arr[mid] > k:
        high = mid - 1
      else:
        low = mid + 1 
    return resp
  
  def lastOccurence(self, arr:List[int], k: int):
    resp = -1

    low, high = 0, len(arr)-1
    while (low <= high):
      mid = low + (high-low) // 2
      if arr[mid] == k:
        resp = mid
        low = mid + 1
      elif arr[mid] < k:
        low = mid + 1
      else:
        high = mid - 1
    return resp

if __name__ == "__main__":
  arr = [3,4,13,13,13,20,40]
  resp1 = Solution().firstOccurence(arr, 5)
  if (resp1 == -1): print([-1, -1])
  else: print([resp1, Solution().lastOccurence(arr, 13)])


"""
First Position
1. Initialize resp = -1, low = 0, high = n-1
2. Initialize while loop until low <= high and calculate mid
3. If array[mid] == target resp = mid, high = mid - 1
4. Elif array[mid] > target, high = mid - 1
5. Else low = mid + 1
TC -> O(logN), SC -> O(1)

Last Position
1. Initialize resp = -1, low = 0, high = n-1
2. Initialize while loop until low <= high and calculate mid
3. If array[mid] == target resp = mid, low = mid + 1
4. Elif array[mid] < target, low = mid + 1
5. Else high = mid - 1
TC -> O(logN), SC -> O(1)
"""