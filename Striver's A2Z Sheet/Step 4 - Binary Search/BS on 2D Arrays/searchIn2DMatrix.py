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
       if (matrix[i][0] <= target and target <= matrix[i][m-1]):
          return self.binarySearch(matrix[i], target)
    return False

  def findSolution(self, matrix: List[List[int]], target:int):
    n, m = len(matrix), len(matrix[0])
    low, high = 0, n * m - 1
    while low <= high:
      mid = low + (high - low) // 2
      row = mid // m
      col = mid % m
      if matrix[row][col] == target:
        return True
      elif matrix[row][col] < target:
        low = mid + 1
      else:
        high = mid - 1
    return False

if __name__ == "__main__":
  arr = [[1, 2, 3, 4,], [5, 6, 7, 8], [9, 10, 11, 12]]
  k = 8
  resp = Solution().findSolution(arr, k)
  print(resp)


"""
Search In 2D Matrix
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
3. If matrix[i][0] <= target && target <= matrix[i][m-1]: If this condition is met, we can conclude that row i 
has the possibility of containing the target.
4. So, we will apply binary search on row i, and check if the ‘target’ is present. If it is present, we will return 
true from this step. Otherwise, we will return false.
TC -> O(n + log(m)), SC -> O(1)

Optimal Approach
1. Initialize two pointers low = 0, high = n * m - 1
2. In loop calculate mid = low + (high - low) // 2
3. Convert mid to 2D index using row = mid // m and col = mid % m
4. If matrix[row][col] is equal to target return True
5. ElIf matrix[row][col] is less than target set low = mid + 1 else high = mid - 1
TC -> O(log(n*m)), SC -> O(1)
"""