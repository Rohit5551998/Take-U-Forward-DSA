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
    count, maxCount = 0, 0
    for i in range(len(arr)):
      if arr[i] == 1:
        count += 1
        if count > maxCount:
          maxCount = count
      else:
        count = 0
    return maxCount

if __name__ == "__main__":
  arr = [1,1,0,1,1,1,0, 0, 1, 0, 1, 1, 1, 1]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Max Consecutive Ones

Intuition:
Initialize maxCount and count to 0.
Update Count when 1 is encountered and reset it to 0 when 0 is encountered.
Check if count is greater than maxCount and update maxCount accordingly.
Return MaxCount.
Time Complexity: O(n), Space Complexity: O(1)
"""