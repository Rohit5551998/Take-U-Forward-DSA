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
  def markRow(self, arr:List[List[int]], n: int, m: int, i: int):
    for j in range(0, m):
      if (arr[i][j] != 0):
        arr[i][j] = -1

  def markCol(self, arr:List[List[int]], n: int, m: int, j: int):
    for i in range(0, n):
      if (arr[i][j] != 0):
        arr[i][j] = -1

  def findSolution1(self, arr:List[List[int]]):
    n, m = len(arr), len(arr[0])
    for i in range(0, n):
      for j in range(0, m):
        if arr[i][j] == 0:
          self.markRow(arr, n, m, i);
          self.markCol(arr, n, m, j);

    for i in range(0, n):
      for j in range(0, m):
        if arr[i][j] == -1:
          arr[i][j] = 0
    return arr

  def findSolution2(self, arr:List[List[int]]):
    n, m = len(arr), len(arr[0])
    row, col = [1] * n, [1] * m
    for i in range(0, n):
      for j in range(0, m):
        if arr[i][j] == 0:
          row[i], col[j] = 0, 0

    for i in range(0, n):
      for j in range(0, m):
        if (row[i] == 0 or col[j] == 0):
          arr[i][j] = 0
    return arr
  
  def findSolution(self, arr:List[List[int]]):
    n, m = len(arr), len(arr[0])
    row, col = 1, 1
    for i in range(0, n):
      if arr[i][0] == 0:
        col = 0
        break

    for j in range(0, m):
      if arr[0][j] == 0:
        row = 0
        break  

    for i in range(1, n):
      for j in range(1, m):
        if arr[i][j] == 0:
          arr[i][0], arr[0][j] = 0, 0

    for i in range(1, n):
      for j in range(1, m):
        if (arr[i][0] == 0 or arr[0][j] == 0):
          arr[i][j] = 0

    if (row == 0):
      for j in range(0, m):
        arr[0][j] = 0

    if (col == 0):
      for i in range(0, n):
        arr[i][0] = 0
    return arr



if __name__ == "__main__":
  arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5], [1, 0, 2, 5]]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Set Array Zeroes:

Brute Force:
1. Traverse the entire matrix and if any cell contains 0 value mark all values in row and cell as -1
2. Traverse the entire matrix again and assign all -1 equal to 0 in matrix
TC -> O((N*M)*(N + M)) + O(N*M), SC -> O(1)

Better Approach:
1. Use extra row and column array to store positions of 0 elements 
2. If any element in matrix is 0 mark the corresponding row & column 0 in extra arrays declared
3. Traverse the entire matrix again and if row or column array is 0 then mark the cell as 0
TC -> O(2*(N*M)), SC -> O(N+M)

Optimal Approach:
1. Traverse first row and column and if any element is zero in it store it in two variables
2. Use the first row and column as storage as discussed in better approach
3. Traverse the entire matrix again and if row or column array is 0 then mark the cell as 0
4. If row or column pointers is equal to 0 then set first row or column zero accordingly
TC -> O(2*(N*M) + O(2*(N+M))), SC -> O(1)
"""