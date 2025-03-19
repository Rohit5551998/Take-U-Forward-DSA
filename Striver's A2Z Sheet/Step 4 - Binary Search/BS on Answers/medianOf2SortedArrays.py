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
  def findSolution1(self, arr1: List[int], arr2: List[int]):
    arr3 = []
    n1, n2 = len(arr1), len(arr2)
    i, j = 0, 0
    while (i < n1 and j < n2):
      if arr1[i] <= arr2[j]:
        arr3.append(arr1[i])
        i += 1
      else:
        arr3.append(arr2[j])
        j += 1

    while(i < n1):
      arr3.append(arr1[i])
      i += 1

    while(j < n2):
      arr3.append(arr2[j])
      j += 1

    if (len(arr3)%2 == 1): return arr3[len(arr3)//2]  
    return (arr3[len(arr3)//2] + arr3[len(arr3)//2-1])/2.0
  
  def findSolution2(self, arr1: List[int], arr2: List[int]):
    n1, n2 = len(arr1), len(arr2)
    cnt, i, j = 0, 0, 0
    ind1, ind2 = (n1+n2)//2 - 1,  (n1+n2)//2
    ind1el, ind2el = -1, -1
    while (i < n1 and j < n2):
      if (arr1[i] < arr2[j]):
        if (cnt == ind1): ind1el = arr1[i]
        if (cnt == ind2): ind2el = arr1[i]
        cnt += 1
        i += 1
      else:
        if (cnt == ind1): ind1el = arr2[j]
        if (cnt == ind2): ind2el = arr2[j]
        cnt += 1
        j += 1
    
    while (i < n1):
      if (cnt == ind1): ind1el = arr1[i]
      if (cnt == ind2): ind2el = arr1[i]
      cnt += 1
      i += 1 
    
    while (j < n2):
      if (cnt == ind1): ind1el = arr2[j]
      if (cnt == ind2): ind2el = arr2[j]
      cnt += 1
      j += 1  
    n = n1+n2
    if (n % 2 == 1): return ind2el
    return (ind1el+ind2el)/2.0

  def findSolution(self, arr1: List[int], arr2: List[int]):
    n1, n2 = len(arr1), len(arr2)
    if (n1 > n2): return self.findSolution(arr2, arr1)
    left = (n1+n2+1)//2
    low, high = 0, n1
    while (low <= high):
      mid1 = (low + high)//2
      mid2 = left - mid1
      l1, l2, r1, r2 = -math.inf, -math.inf, math.inf, math.inf
      if (mid1 > 0): l1 = arr1[mid1-1]
      if (mid2 > 0): l2 = arr2[mid2-1]
      if (mid1 < n1): r1 = arr1[mid1]
      if (mid2 < n2): r2 = arr2[mid2]
      if (l1 <= r2 and l2 <= r1):
        if (n1+n2)%2 == 1: return max(l1, l2)
        return (max(l1, l2)+min(r1, r2))/2.0
      elif (l1 > r2): high = mid1 - 1
      else: low = mid1 + 1

    return 0

if __name__ == "__main__":
  arr1 = [1,2]
  arr2 = [3,4]
  resp = Solution().findSolution(arr1, arr2)
  print(resp)


"""
Median of 2 Sorted Arrays
Brute Force
1. Declare arr3 and initialize pointers i,j = 0, 0
2. Use Merge Operation to Combine both Arrays in arr3
3. Once done if new array contains odd elements return arr3[len(arr3)//2]
4. Else return (arr3[len(arr3)//2] + arr3[len(arr3)//2-1])/2.0
TC -> O(n1+n2), SC -> O(n1+n2)

Better Approach
1. Initialize pointers i,j = 0, 0, ind2 = (n1+n2)/2 and ind1 = ((n1+n2)/2)-1 and cnt = 0
2. Check if cnt reaches either ind1 or ind2 and assign respective elements the values required
3. Once done if new array contains odd elements return ind2el
4. Else return (ind2el + ind1el)/2.0
TC -> O(n1+n2), SC -> O(1)

Optimal Approach
1. Make sure arr1 is smaller than arr2 if not swap them
2. Calculate length of left half required = (n1+n2+1)/2
3. Initialize low = 0 and high = n1
4. Run a loop until low <= high and calculate mid1 = (low + high) // 2, mid2 = left - mid1
5. Calculate l1 = arr1[mid1-1], l2 = arr2[mid2-1], r1 = arr1[mid1], r2 = arr2[mid2] default values should be INT_MIN
for l1, l2 and INT_MAX for r1, r2
6. If l1 <= r2 && l2 <= r1, odd: median = max(l1, l2) or even: median = (max(l1, l2) + min(r1, r2))/2.0
7. Else If l1 > r2, high = mid1 - 1
8. Else If l2 > r1, low = mid1 + 1
TC -> O(log(min(n1,n2))), SC -> O(1)
"""