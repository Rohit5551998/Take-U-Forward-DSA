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
  def allocateArrays(self, arr: List[int], threshold: int):
    sumofSubArray = 0
    subArrayCnt = 1
    for i in range(0, len(arr)):
      if (sumofSubArray + arr[i] <= threshold):
        sumofSubArray += arr[i]
      else:
        sumofSubArray = arr[i]
        subArrayCnt += 1
    return subArrayCnt


  def findSolution1(self, arr: List[int], m:int):
    if (m > len(arr)):
      return -1
    
    for i in range(max(arr), sum(arr) + 1):
      subArrays = self.allocateArrays(arr, i)
      if (subArrays == m): return i
    return max(arr)

  def findSolution(self, arr: List[int], m:int):
    low, high, ans = max(arr), sum(arr), max(arr)
    while (low <= high):
      mid = low + (high - low) // 2
      subArrays = self.allocateArrays(arr, mid)
      if (subArrays <= m):
        ans = mid
        high = mid - 1
      else:
        low = mid + 1
    return ans

if __name__ == "__main__":
  arr = [25, 46, 28, 49, 24]
  m = 4
  resp = Solution().findSolution(arr, m)
  print(resp)


"""
Split Array Largest Sum
Brute Force
1. Run a Loop From Max(arr) to Sum(arr) and allocate arrays for i only if m > n is not valid(return -1)
2. Inside Allocate Arrays initialize subArrayCnt = 1 and sumofSubArray = 0
use array loop with logic if sumofSubArray + arr[i] <= pages threshold then add pages to current array sum
3. Else Increment subArrayCnt By 1 and Set sumofSubArray to Current Pages
5. If Allocated subArrayCnt is equal to limit return i 
6. At End of Loop Return max(arr)
TC -> O(n * (sum(arr[])-max(arr[])+1)), SC -> O(1)

Optimal Approach
1. Initialize two pointers low = max(arr), high = sum(arr), ans = max(arr) only if m > n is not valid(return -1)
2. In loop calculate mid = low + (high - low) // 2
3. Inside Allocate Arrays initialize subArrayCnt = 1 and sumofSubArray = 0
use array loop with logic if sumofSubArray + arr[i] <= pages threshold then add pages to current array sum
4. Else Increment subArrayCnt By 1 and Set sumofSubArray to Current Pages
5. If Allocated subArrayCnt is greater than m then set low = mid + 1
6. Else high = mid - 1 and ans = mid
7. Return ans.
TC -> O(n * log(sum(arr[])-max(arr[])+1)), SC -> O(1)
"""