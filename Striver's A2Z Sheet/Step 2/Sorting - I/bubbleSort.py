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
  def bubbleSort(self, arr:List[int], n: int): 
    for i in range(n-1, 0, -1):
      didSwap = 0
      for j in range(i, n):
        if (arr[j] < arr[j-1]):
          arr[j], arr[j-1] = arr[j-1], arr[j]
          didSwap = 1
      if (didSwap == 0): #Optimization for already sorted array
        break


if __name__ == "__main__":
  arr = [5, 4, 10, 3, 1, 6, 17, 2]
  n = len(arr)
  Solution().bubbleSort(arr, n)
  print(arr)


"""
Compare Elements Side By Side (Adjacent Elements) & Push Max to Last of Array
Start With Max Window Size and decrement till lowest range. Logic works revers of Selection sort
TC: O(n**2) - Average & Worst
    O(n) - Best
"""