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
  def findSolution(self, arr: List[int]):
    hashmap = {}

    n = len(arr)

    for i in range(1, n+1):
      hashmap[i] = 0

    for i in arr:
      hashmap[i] += 1

    return list(hashmap.values())
  
if __name__ == "__main__":
  # n = int(input("Please enter a number: \n"))
  arr = [2, 3, 2, 3, 5]
  print(Solution().findSolution(arr))


"""

"""