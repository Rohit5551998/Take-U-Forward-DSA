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

  def findSolution(self, arr:List[int], k: int):
    resp = len(arr)

    low, high = 0, len(arr)-1
    while (low <= high):
      mid = low + (high-low) // 2
      if arr[mid] >= k:
        resp = mid
        # look for smaller index on the left
        high = mid - 1
      else:
        low = mid + 1 # look on the right
    return resp

if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5, 6, 7, 9, 10]
  resp = Solution().findSolution(arr, 8)
  print(resp)


"""
Search Insert Position
1. Initialize resp = -1, low = 0, high = n-1
2. Initialize while loop until low <= high and calculate mid
3. If array[mid] >= target resp = mid, high = mid - 1
5. Else low = mid + 1
TC -> O(logN), SC -> O(1)
"""