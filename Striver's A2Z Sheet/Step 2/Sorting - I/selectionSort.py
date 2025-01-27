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
  def selectionSort(self, arr:List[int], n: int): 
    for i in range(0, n-1):
      mini = i
      for j in range(i, n):
        if (arr[mini] > arr[j]):
          mini = j
      arr[i], arr[mini] = arr[mini], arr[i]

if __name__ == "__main__":
  arr = [5, 4, 10, 3, 1, 6, 17, 2]
  n = len(arr)
  Solution().selectionSort(arr, n)
  print(arr)


"""
Select Minimum Element And Put In First Position of Array then decrease window size by 1
TC: O(n**2)
"""