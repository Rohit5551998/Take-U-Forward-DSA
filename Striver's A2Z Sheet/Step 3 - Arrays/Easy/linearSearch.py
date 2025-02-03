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

  def findSolution(self, arr:List[int], k: int):
    resp = -1

    for i in range(len(arr)):
      if (arr[i] == k):
        resp = i
        break

    return resp

if __name__ == "__main__":
  arr = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
  resp = Solution().findSolution(arr, 4)
  print(resp)


"""
Linear Search

Check If Elements Exists In Loop or Return -1
"""