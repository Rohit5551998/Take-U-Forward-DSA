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
    if len(arr) <= 1:
      return -1

    max = arr[0]
    secondMax = -1

    for i in range(1, len(arr)):
      if (arr[i] > max):
        secondMax = max
        max = arr[i]
      if (arr[i] > secondMax and arr[i] != max):
          secondMax = arr[i]

    return secondMax
    

if __name__ == "__main__":
  # arr = [18, 5, 4, 10, 3, 1, 6, 17, 2]
  # arr = [12, 35, 1, 10, 34, 1]
  arr = [10, 10, 10]
  n = len(arr)
  resp = Solution().findSolution(arr)
  print(resp)


"""
TC: O(n), SC: O(1)
"""