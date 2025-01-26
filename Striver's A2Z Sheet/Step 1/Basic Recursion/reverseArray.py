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

  def findSolution(self, x:List[int], l: int, r: int) -> int:
    if (l < r):
      x[l], x[r] = x[r], x[l]
      self.findSolution(x, l+1, r-1)


if __name__ == "__main__":
  x = [1, 2, 3, 4, 5, 6]
  Solution().findSolution(x, 0, len(x)-1)
  print(x)


"""
Reverse an array or string using recursion
"""