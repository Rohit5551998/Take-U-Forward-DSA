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
    maxCnt = 0
    # traverse the matrix:
    for i in range(n):
        cnt = 0
        for j in range(m):
          if (matrix[i][j] == 1):
            cnt += m-j
            break
        maxCnt = max(maxCnt, cnt)
    if (maxCnt == 0): return -1
    return maxCnt

  def lowerBound(self, arr, target):
    low, high, ans = 0, len(arr)-1, len(arr)
    while (low <= high):
      mid = low + (high - low) // 2
      if (arr[mid] < target):
        low = mid + 1
      else:
        ans = mid
        high = mid - 1
    return ans

  def findSolution(self, matrix: List[List[int]]):
    n, m = len(matrix), len(matrix[0])
    maxCnt, maxInd = -1, -1
    for i in range(0, n):
      cnt = m - self.lowerBound(matrix[i], 1)
      if (cnt > 0 and cnt > maxCnt):
        maxCnt = cnt
        maxInd = i
    return maxInd
  
if __name__ == "__main__":
  arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Find Row With Max 1
Brute Force
1. Initialize maxCnt = -1 and Run two loops and initialize cnt inside first loop to count number of 1s
2. Next, for every row, add m - the first occurence of 1.
3. Update maxCount if required and return it at end of loop if non-zero else return -1
TC -> O(n*m), SC -> O(1)

Optimal Approach
1. Initialize maxCnt = -1, maxIndex = -1
2. Loop through rows and calculate lowerbound of 1 for each row 
3. Set Count to col - lowerbound and if it is greater than 0 and maxCnt update maxCnt and maxIndex
4. At End of Loop return maxIndex or maxCnt as required
TC -> O(n*log(m)), SC -> O(1)
"""