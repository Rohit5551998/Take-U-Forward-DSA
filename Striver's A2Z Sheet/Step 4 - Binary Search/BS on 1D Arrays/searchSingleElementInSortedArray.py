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

    if (len(arr) == 1): return arr[0]
    if (arr[0] != arr[1]): return arr[0]
    if (arr[n-1] != arr[n-2]): return arr[n-1]

    low, high = 1, len(arr)-2
    while (low <= high):
      mid = low + (high - low) // 2

      if (arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]):
        return arr[mid]

      elif ((mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid+1])):
        low = mid + 1
      
      else:
        high = mid - 1
    return -1


if __name__ == "__main__":
  arr = [1,1,2,2,3,3,4,5,5,6,6]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Search Single Element In Sorted Array
1. Check for Edge Cases Len(arr) = 1 or first element not equal to second or last element not equal to second last
and return ans if required
1. Initialize two pointers low = 1, high = n - 2
2. In loop calculate mid = low + (high - low) // 2
3. Check If Mid Is Not Equal to Previous and Next Element and Return It
4. Else Check If Index % 2 == 1 and arr[mid] == arr[mid - 1] or Index % 2 == 0 and arr[mid] == arr[mid + 1] which means we 
are in left portion of single element. Update low = mid + 1
5. Else Check If Index % 2 == 1 and arr[mid] == arr[mid + 1] or Index % 2 == 0 and arr[mid] == arr[mid - 1] which means we 
are in right portion of single element. Update high = mid - 1
TC -> O(log(n)), SC -> O(1)
"""