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
  # Brute Force
  def findSolution1(self, arr:List[int]):
    temp = []

    for i in range(len(arr)):
      if (arr[i] != 0):
        temp.append(arr[i])

    for i in range(len(temp)):
      arr[i] = temp[i]

    for i in range(len(temp), len(arr)):
      arr[i] = 0
    return arr
  
  # Optimal Approach
  def findSolution(self, arr:List[int]):
    j = -1
    for i in range(0, len(arr)):
      if (arr[i] == 0):
        j = i
        break

    if (j != -1):
      for i in range(j+1, len(arr)):
        if (arr[i] != 0):
          arr[i], arr[j] = arr[j], arr[i]
          j += 1

    return arr

if __name__ == "__main__":
  arr = [1, 1, 2, 0, 0, 2, 2, 0, 2, 3, 3, 0, 3, 0, 4]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Move Zeroes to End

Brute Force
Use a Temp Array to Store All Non-Zero Elements in First Iteration
Fill Array with this Temp Array and Fill Extra Positions with 0
TC -> O(N) + O(X) + O(N-X) = O(2N), SC -> O(N)

Optimal Approach
Two Pointer Approach
Initialize Pointer j to first zero element and i to next element
If i != 0 swap i, j and increment both else increment i only
"""