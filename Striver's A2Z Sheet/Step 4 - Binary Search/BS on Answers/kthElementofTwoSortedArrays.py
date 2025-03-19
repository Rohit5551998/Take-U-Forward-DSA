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
  def findSolution1(self, a: List[int], b: List[int], k: int):
    arr3 = []
    m, n = len(a), len(b)
    # Apply the merge step:
    i, j = 0, 0
    while i < m and j < n:
        if a[i] < b[j]:
            arr3.append(a[i])
            i += 1
        else:
            arr3.append(b[j])
            j += 1

    # Copy the left-out elements:
    arr3.extend(a[i:])
    arr3.extend(b[j:])
    return arr3[k - 1]
  
  def findSolution2(self, a: List[int], b: List[int], k: int):
    m, n = len(a), len(b)
    ele = -1
    cnt = 0  # counter
    # apply the merge step:
    i, j = 0, 0
    while i < m and j < n:
        if a[i] < b[j]:
            if cnt == k - 1:
                ele = a[i]
            cnt += 1
            i += 1
        else:
            if cnt == k - 1:
                ele = b[j]
            cnt += 1
            j += 1

    # copy the left-out elements:
    while i < m:
        if cnt == k - 1:
            ele = a[i]
        cnt += 1
        i += 1
    while j < n:
        if cnt == k - 1:
            ele = b[j]
        cnt += 1
        j += 1
    return ele

  def findSolution(self, arr1: List[int], arr2: List[int], k: int):
    n1, n2 = len(arr1), len(arr2)
    if (n1 > n2): return self.findSolution(arr2, arr1, k)
    left = k
    low, high = max(0, k-n2), min(n1, k)
    while (low <= high):
      mid1 = (low + high)//2
      mid2 = left - mid1
      l1, l2, r1, r2 = -math.inf, -math.inf, math.inf, math.inf
      if (mid1 > 0): l1 = arr1[mid1-1]
      if (mid2 > 0): l2 = arr2[mid2-1]
      if (mid1 < n1): r1 = arr1[mid1]
      if (mid2 < n2): r2 = arr2[mid2]
      if (l1 <= r2 and l2 <= r1): return max(l1, l2)
      elif (l1 > r2): high = mid1 - 1
      else: low = mid1 + 1

    return 0

if __name__ == "__main__":
  arr1 = [1,2]
  arr2 = [3,4]
  k=4
  resp = Solution().findSolution(arr1, arr2, k)
  print(resp)


"""
Kth Element of 2 Sorted Arrays
Brute Force
1. Declare arr3 and initialize pointers i,j = 0, 0
2. Use Merge Operation to Combine both Arrays in arr3
3. Once done return element at index k-1
TC -> O(n1+n2), SC -> O(n1+n2)

Better Approach
1. Initialize pointers i,j = 0, 0, and cnt = 0
2. Check if cnt reaches either k-1 and assign el the value required
3. Return el
TC -> O(n1+n2), SC -> O(1)

Optimal Approach
1. Make sure arr1 is smaller than arr2 if not swap them
2. Calculate length of left half required = k
3. Initialize low = max(0, k-n2) and high = (n1, k)
4. Run a loop until low <= high and calculate mid1 = (low + high) // 2, mid2 = left - mid1
5. Calculate l1 = arr1[mid1-1], l2 = arr2[mid2-1], r1 = arr1[mid1], r2 = arr2[mid2] default values should be INT_MIN
for l1, l2 and INT_MAX for r1, r2
6. If l1 <= r2 && l2 <= r1, max(l1, l2) is the answer return it
7. Else If l1 > r2, high = mid1 - 1
8. Else If l2 > r1, low = mid1 + 1
TC -> O(log(min(n1,n2))), SC -> O(1)
"""