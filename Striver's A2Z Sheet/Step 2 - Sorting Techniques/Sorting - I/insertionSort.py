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
  def insertionSort(self, arr:List[int], n: int): 
    for i in range(1, n):
      for j in range(i, -1, -1):
        if (j+1 < n and arr[j] > arr[j+1]):
          arr[j], arr[j+1] = arr[j+1], arr[j]
      print(arr)

  def insertionSortRecursive(self, arr: List[int], n: int):
    for i in range(n, -1, -1):
      if (i+1 < n and arr[i] > arr[i+1]):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
    if (n < len(arr)):
      self.insertionSortRecursive(arr, n+1)

if __name__ == "__main__":
  arr = [5, 4, 10, 3, 1, 6, 17, 2]
  n = len(arr)
  Solution().insertionSort(arr, n)
  arr = [9717, 8876, 5460, 449, 4716, 9333]
  n = len(arr)
  Solution().insertionSortRecursive(arr, 1)
  print(arr)


"""
Start with small window size and push the latest element in it's correct position in windows by adjacent swaps.
Once done increase window size
TC: O(n**2)
"""