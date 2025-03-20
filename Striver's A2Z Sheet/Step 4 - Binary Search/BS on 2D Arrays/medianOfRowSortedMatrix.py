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
    arr = []
    # traverse the matrix:
    for i in range(n):
        for j in range(m):
            arr.append(matrix[i][j])
    arr.sort()
    return arr[(n*m)//2]


  def upperBound(self, arr, target):
    low, high, ans = 0, len(arr)-1, len(arr)
    while (low <= high):
      mid = low + (high - low) // 2
      if (arr[mid] <= target):
        low = mid + 1
      else:
        ans = mid
        high = mid - 1
    return ans


  def calculateSmallEqual(self, matrix, row, element):
    cnt = 0
    for i in range(row):
      cnt += self.upperBound(matrix[i], element)
    return cnt

  def findSolution(self, matrix: List[List[int]]):
    n, m = len(matrix), len(matrix[0])
    low, high = math.inf, -math.inf
    for i in range(n):
      low = min(low, matrix[i][0])
      high = max(high, matrix[i][m-1])

    reqCnt = (n*m)//2
    while (low <= high):
      mid = low + (high - low) // 2
      smallEqual = self.calculateSmallEqual(matrix, n, mid)
      if (smallEqual <= reqCnt):
        low = mid + 1
      else:
        high = mid - 1
    return low

if __name__ == "__main__":
  arr = [[1, 4, 9], [2, 5, 6], [3, 8, 7]]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Median of Row Wise Sorted Matrix
Brute Force
1. Initialize empty arr and add all elements of the matrix to it.
2. Sort the arr and return the middle element.
TC -> O(n*m) + O(n*m(log(n*m))), SC -> O(n*m)

Optimal Approach
1. Initialize two pointers low = min(matrix), high = max(matrix)
2. In loop calculate mid = low + (high - low) // 2
3. Calculate Small Equal to get the number of elements <= mid using upper bound
4. If smallEqual <= (n*m)//2 eliminate left half low = mid + 1
5. Else high = mid - 1
6. Return low
TC -> O(log(10^9)) * O(m*log(n)), SC -> O(1)
"""