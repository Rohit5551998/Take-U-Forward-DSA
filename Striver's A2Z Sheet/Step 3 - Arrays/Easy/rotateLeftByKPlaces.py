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

  def findLeftKSolution1(self, arr:List[int], k: int):
    if len(arr) > 1:
      k = k % len(arr)
      temp = []
      for i in range(k):
        temp.append(arr[i])

      for i in range(k, len(arr)):
        arr[i-k] = arr[i]

      for i in range(k):
        arr[len(arr)-k+i] = temp[i]

    return arr
  
  def findRightKSolution1(self, arr:List[int], k: int):
    if len(arr) > 1:
      k = k % len(arr)
      temp = []
      for i in range(len(arr)-k, len(arr)):
        temp.append(arr[i])

      for i in range(len(arr)-k-1, -1, -1):
        arr[i+k] = arr[i]

      for i in range(k):
        arr[i] = temp[i]

    return arr
    
  def reverse(self, arr, start, end):
    while (start < end):
      arr[start], arr[end] = arr[end], arr[start]
      start += 1
      end -= 1

  #Optimal Solutions
  def findLeftKSolution(self, arr:List[int], k: int):
    n = len(arr)
    k = k % n
    self.reverse(arr, 0, k-1)
    self.reverse(arr, k, len(arr)-1)
    self.reverse(arr, 0, len(arr)-1)
    return arr
  
  def findRightKSolution(self, arr:List[int], k: int):
    n = len(arr)
    k = k % n
    self.reverse(arr, n-k, n-1)
    self.reverse(arr, 0, n-k-1)
    self.reverse(arr, 0, len(arr)-1)
    return arr
  
if __name__ == "__main__":
  arr = [18, 5, 4, 10, 3, 1, 6, 17, 2]
  k = 3
  # resp = Solution().findLeftKSolution(arr, k)
  # print(resp)
  resp = Solution().findRightKSolution(arr, k)
  print(resp)


"""
Rotate Array By K Places
Brute Force:
Use Temp Array for Storing First(left) or Last(Right) K Elements
Then Shift the Elements Starting From K to N or N-K-1 to 0 Elements depending on directions
Lastly Shift the Stored Elements From Temp Array Into Required Positions
TC: O(n), SC: O(k)

Optimal:
Reverse First or Last Elements Depending on Direction
Reverse Remaining Elements Depending on Direction
Reverse The Entire Array Again To get Required Shifting Direction
TC: O(n), SC: O(1)
"""