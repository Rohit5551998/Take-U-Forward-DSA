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
  def findSolution1(self, matrix: List[List[int]], target:int):
    n = len(matrix)
    m = len(matrix[0])

    # traverse the matrix:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False

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

  def findSolution2(self, matrix: List[List[int]], target:int):
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        flag = self.binarySearch(matrix[i], target)
        if (flag):
          return True
    return False

  def findSolution(self, matrix: List[List[int]], target:int):
    n, m = len(matrix), len(matrix[0])
    row, col = 0, m - 1
    while row < n and col >=0:
      value = matrix[row][col]
      if value == target:
        return True
      elif value < target:
        row += 1
      else:
        col -= 1
    return False

if __name__ == "__main__":
  arr = [[1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]]
  k = 32
  resp = Solution().findSolution(arr, k)
  print(resp)


"""
Search In 2D Matrix - II
Brute Force
1. We will use a loop(say i) to select a particular row at a time.
2. Next, for every row, we will use another loop(say j) to traverse each column.
3. Inside the loops, we will check if the element i.e. matrix[i][j] is equal to the ‘target’. 
If we find any matching element, we will return true.
Otherwise, after completing the traversal, we will return false.
TC -> O(n*m), SC -> O(1)

Better Approach
1. We will use a loop(say i) to select a particular row at a time.
2. Next, for every row, i, we will check if it contains the target.
3. So, we will apply binary search on each row and check if the ‘target’ is present. If it is present, we will return 
true from this step. 
4. Otherwise, at end of loop we will return false.
TC -> O(n * log(m)), SC -> O(1)

Optimal Approach
1. Start at cell (0, m-1) with row = 0 and col = m-1
2. Run a loop until row < n and col >= 0
3. If matrix[row][col] is equal to target return True
4. ElIf matrix[row][col] is less than target set row += 1 
5. ElIf matrix[row][col] is greater than target set col -= 1
TC -> O(N+M), SC -> O(1)
"""