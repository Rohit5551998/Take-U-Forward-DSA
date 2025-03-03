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
    resp = False

    low, high = 0, len(arr)-1
    while (low <= high):
      mid = low + (high-low) // 2
      if (arr[mid] == k):
        resp = True
        break
      if (arr[low] == arr[mid] and arr[mid] == arr[high]):
        low += 1
        high -= 1
        continue

      if (arr[low] <= arr[mid]):
        if (arr[low] <= k and k <= arr[mid]):
          high = mid - 1
        else:
          low = mid + 1
      else:
        if (arr[mid] <= k and k <= arr[high]):
          low = mid + 1
        else:
          high = mid - 1
    return resp


if __name__ == "__main__":
  # arr = [4, 5, 1, 2, 3]
  arr = [1,0,1,1,1]
  resp = Solution().findSolution(arr, 0)
  print(resp)


"""
Search In Rotated Sorted Array (With Duplicates)
1. Initialize two pointers low = 0, high = n - 1
2. In loop calculate mid = low + (high - low) // 2 and check if it is equal to target and return True
3. Check if arr[low] == arr[mid] == arr[high] increment low, decrement high and continue
4. Check if first half is sorted with arr[low] <= arr[mid], if true search within this half by checking if target
lies between arr[low] and arr[mid] and eliminate right half or else eliminate this half
5. If second half is sorted, check if target lies between arr[mid] and arr[high] and eliminate left half or else 
eliminate this half.
6. If mid points to target return True or else return False.
TC -> O(log(n)), SC -> O(1)
"""