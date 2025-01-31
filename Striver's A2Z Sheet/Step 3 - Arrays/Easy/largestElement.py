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
    max = arr[0]

    for i in range(0, len(arr)):
      if (arr[i] > max):
        max = arr[i]

    return max
    

if __name__ == "__main__":
  arr = [5, 4, 10, 3, 1, 6, 17, 2]
  n = len(arr)
  resp = Solution().findSolution(arr)
  print(resp)


"""
TC: O(n), SC: O(1)
"""