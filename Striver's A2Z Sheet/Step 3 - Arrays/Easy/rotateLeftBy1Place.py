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

  def findLeftSolution(self, arr:List[int]):
    if len(arr) > 1:
      temp = arr[0]
      for i in range(1, len(arr)):
        arr[i-1] = arr[i]
      arr[len(arr)-1] = temp

    return arr
  
  def findRightSolution(self, arr:List[int]):
    if len(arr) > 1:
      temp = arr[len(arr)-1]
      for i in range(len(arr)-2, -1, -1):
        arr[i+1] = arr[i]
      arr[0] = temp

    return arr
    
  
if __name__ == "__main__":
  arr = [18, 5, 4, 10, 3, 1, 6, 17, 2]
  # resp = Solution().findLeftSolution(arr)
  # print(resp)
  resp = Solution().findRightSolution(arr)
  print(resp)


"""
Rotate Array By 1 Position

Brute Force:
Use Temp Array for Rotating Elements
TC: O(n), SC: O(n)

Optimal:
Use Single Temp Location For First or Last(Right Rotate) Element
TC: O(n), SC: O(1)
"""