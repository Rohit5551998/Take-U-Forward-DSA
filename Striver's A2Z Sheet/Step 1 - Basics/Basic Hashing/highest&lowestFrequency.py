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

    for i in arr:
      if i not in hashmap:
        hashmap[i] = 0
      hashmap[i] += 1

    maxElement, maxFrequency = 0, 0
    minElement, minFrequency = 0, math.inf

    for key, value in hashmap.items():
      if value > maxFrequency:
        maxFrequency = value
        maxElement = key

      if value < minFrequency:
        minFrequency = value
        minElement = key

    return [maxElement, minElement] 

if __name__ == "__main__":
  # n = int(input("Please enter a number: \n"))
  arr = [2, 3, 2, 3, 5, 3, 2, 2, 1]
  print(Solution().findSolution(arr))


"""

"""