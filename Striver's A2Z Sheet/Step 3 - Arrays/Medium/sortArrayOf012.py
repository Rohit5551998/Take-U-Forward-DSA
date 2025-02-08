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

  def findSolution1(self, arr:List[int]):
    return sorted(arr)

  def findSolution2(self, arr: List[int]):
    cnt = {
      0: 0,
      1: 0,
      2: 0
    };

    for i in range(len(arr)):
      cnt[arr[i]] += 1

    for i in range(0, cnt[0]):
      arr[i] = 0

    for i in range(cnt[0], cnt[0]+cnt[1]):
      arr[i] = 1

    for i in range(cnt[0]+cnt[1], len(arr)):
      arr[i] = 2

    return arr
    
  def findSolution(self, arr: List[int]):
    n = len(arr)
    low, mid, high =  0, 0, n-1

    while (mid <= high):
      if (arr[mid] == 0):
        arr[low], arr[mid] = arr[mid], arr[low]
        mid += 1
        low += 1

      elif (arr[mid] == 1):
        mid += 1
      
      else:
        arr[high], arr[mid] = arr[mid], arr[high]
        high -= 1
    return arr


if __name__ == "__main__":
  arr = [0, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 1, 2, 0, 1, 2]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Brute Force:
Sort The Entire Array
TC: O(n*log(n)) SC: O(n)

Better Approach:
Use 3 Counters to Store Number of Each Element
Initialize Another Loop to Update the array based on Counters
TC: O(2n), SC: O(1)

Optimal Approach (Dutch National Flag Algo):
1. Initialize 3 Pointers low, mid & high
2. Space between 0 to low - 1 always contains 0 in sorted order
3. Space between low to mid - 1 always contains 1 in sorted order
4. Space between high and n - 1 always contains 2 in sorted order
5. Space between mid to high - 1 in unsorted and needs to be sorted
6. If arr[mid] == 0 swap low and mid and increment both
7. If arr[mid] == 1 increment mid
8. If arr[mid] == 2 swap mid and high and decrement high
9. Run till mid & high do not cross
TC: O(n), SC: O(1)
"""