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
  def findSolution1(self, matrix: List[List[int]]):
    n = len(matrix)
    m = len(matrix[0])
    el = -math.inf
    # traverse the matrix:
    for i in range(n):
        for j in range(m):
          el = max(el, matrix[i][j])
    return el

  def binarySearch(self, arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
           return True
        elif arr[mid] < target:
           low = mid + 1
        else:
           high = mid - 1
    return False

  def findSolution(self, matrix: List[List[int]]):
    n, m = len(matrix), len(matrix[0])
    low, high = 0, m-1

    while (low <= high):
      mid = low + (high - low) // 2
      maxEl, maxIndex = -1, -1
      for i in range(n):
        if (matrix[i][mid] > maxEl):
          maxEl = matrix[i][mid]
          maxIndex = i
      left, right = -1, -1
      if mid - 1 >= 0: left = matrix[maxIndex][mid-1]
      if mid + 1 < m: right = matrix[maxIndex][mid+1]
      if (maxEl > left and maxEl > right):
        return [maxIndex, mid] 
        #return maxEl
      elif (maxEl < left):
        high = mid - 1
      else:
        low = mid + 1
    return -1


if __name__ == "__main__":
  arr = [[10,20,15],[21,30,14],[7,16,32]]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Peak Element II
Brute Force
1. Find the max element in matrix and return it
TC -> O(n*m), SC -> O(1)

Optimal Approach
1. Initialize two pointers low = 0, high = col-1
2. In loop calculate mid = low + (high - low) // 2
3. Initialize maxEl and maxIndex to -1 and find max element in column
4. Initialize left and right to -1 and if mid - 1 and mid + 1 is valid assign respective values to them
5. If maxEl is greater than both left and right then return it's indices.
5. ElIf maxEl is less than right set low = mid + 1 else high = mid - 1
TC -> O(n*log(m)), SC -> O(1)
"""