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

  def findSolution(self, arr:List[int]):
    mini = math.inf

    low, high = 0, len(arr)-1
    while (low <= high):
      mid = low + (high - low) // 2
      if (arr[low] <= arr[high]):
        mini = min(mini, arr[low])
        break

      if (arr[low] <= arr[mid]):
        mini = min(mini, arr[low])
        low = mid + 1
      else:
        mini = min(mini, arr[mid])
        high = mid - 1
    return mini


if __name__ == "__main__":
  arr = [4,5,6,7,0,1,2,3]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Minimum In Rotated Sorted Array (Without Duplicates)
1. Initialize two pointers low = 0, high = n - 1
2. In loop calculate mid = low + (high - low) // 2
3. Check if arr[low] <= arr[high], means subarray is completely sorted and return arr[low] and stop iteration.
4. Else Check if arr[low] <= arr[mid], means left part is sorted and check for minimum and eliminate this half.
5. Else If arr[mid] <= arr[high], means right part is sorted and check for minimum and eliminate this half.
TC -> O(log(n)), SC -> O(1)
"""