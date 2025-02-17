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
  def findSolution1(self, arr:List[List[int]]):
    n = len(arr)
    output = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(0, n):
      for j in range(0, n):
        output[j][(n-1)-i] = arr[i][j]
    return output

  def reverse(self, arr: List[int], start: int, end: int):
    while(start <= end):
      arr[start], arr[end] = arr[end], arr[start]
      start += 1
      end -= 1

  def findSolution(self, arr: List[List[int]]):
    n = len(arr)
    
    for i in range(0, n):
      for j in range(i+1, n):
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    for i in range(0, n):
      self.reverse(arr[i], 0, n-1)

    return arr


if __name__ == "__main__":
  arr = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Rotate Matrix By 90:

Brute Force:
1. Use Another Array to Store Elements after rotation.
2. After Rotation a[i][j] will be a[j][(n-1)-i]
TC -> O(N*N), SC -> O(N*N)

Optimal Approach:
1. Transpose the matrix bu swapping elements across diagonal excluding the diagonal.
2. Then reverse each row to get final output
TC -> O(2*(N*N)), SC -> O(1)
"""