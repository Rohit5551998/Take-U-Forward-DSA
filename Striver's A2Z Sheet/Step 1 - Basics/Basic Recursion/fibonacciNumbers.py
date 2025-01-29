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

  def findSolution1(self, x:int, arr: List[int]) -> int:
    if x+1 <= len(arr):
      return arr[x]
    else:
      arr.append(arr[-1] + arr[-2])
      return self.findSolution1(x, arr)
    
  def findSolution(self, x:int) -> int:
    if (x <= 1):
      return x;
    return self.findSolution(x-1) + self.findSolution(x-2)  

if __name__ == "__main__":
  x = int(input("Enter the number: "))
  print(Solution().findSolution1(x, [0, 1]))
  print(Solution().findSolution(x))

"""
Reverse an array or string using recursion
"""