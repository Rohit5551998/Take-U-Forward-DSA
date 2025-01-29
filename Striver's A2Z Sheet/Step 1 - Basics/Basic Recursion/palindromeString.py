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

  def findSolution(self, x:List[int], i:int, n:int) -> int:
    if len(x) in [0, 1]:
      return True
    else: 
      if (i <= abs((int)(n/2))):
        if (x[i] != x[n-i]):
          return False
        return self.findSolution(x, i+1, n)
      return True


if __name__ == "__main__":
  x = "A man, a plan, a canal: Panama"
  x = re.sub(r'[^a-zA-Z0-9]', '', x).lower()
  print(Solution().findSolution(x, 0, len(x)-1))

"""
Reverse an array or string using recursion
"""