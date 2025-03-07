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
    n = len(arr)

    if (len(arr) == 1): return 0
    if (arr[0] > arr[1]): return 0
    if (arr[n-1] > arr[n-2]): return n-1

    low, high = 1, len(arr)-2
    while (low <= high):
      mid = low + (high - low) // 2

      if (arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]):
        return mid

      elif (arr[mid] > arr[mid - 1]):
        low = mid + 1
      
      elif (arr[mid] > arr[mid + 1]):
        high = mid - 1

      else:
        low = mid + 1
    return -1


if __name__ == "__main__":
  arr = [1,2,1,3,5,6,4]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Find Peak Element
1. Check for Edge Cases Len(arr) = 1 or first element > second or last element > to second last
and return ans if required
1. Initialize two pointers low = 1, high = n - 2
2. In loop calculate mid = low + (high - low) // 2
3. Check If Mid > Previous and Mid > Next Element and Return Index
4. Else Check If Arr[mid] > Arr[mid - 1](Increasing Slope). Update low = mid + 1
5. Else Check If Arr[mid] > Arr[mid + 1](Decreasing Slope)_. Update high = mid - 1
6. Else For Multiple Slopes(Edge Case Lowest Point between two peaks). Update either low = mid + 1 or high = mid - 1
TC -> O(log(n)), SC -> O(1)
"""