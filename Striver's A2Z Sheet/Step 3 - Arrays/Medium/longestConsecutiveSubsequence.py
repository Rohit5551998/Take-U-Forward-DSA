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
  def linearSearch(self, element, arr) :
    resp = False
    for i in range(0, len(arr)):
      if (arr[i] == element):
        resp = True
    return resp

  def findSolution1(self, arr:List[int]):
    maxLen, cnt = 1, 0
    for i in range(0, len(arr)):
      x = arr[i] 
      cnt = 1
      while (self.linearSearch(x+1, arr) == True):
        x += 1
        cnt += 1
      maxLen = max(maxLen, cnt)
    return maxLen

  def findSolution2(self, arr:List[int]):
    arr = sorted(arr)
    maxLen, cnt, lastSmaller = 1, 0, -math.inf
    for i in range(0, len(arr)):
      if (arr[i] == lastSmaller + 1):
        lastSmaller = arr[i]
        cnt += 1
        maxLen = max(maxLen, cnt)
      elif (arr[i] != lastSmaller):
        lastSmaller = arr[i]
        cnt = 1
    return maxLen
  
  def findSolution(self, arr: List[int]):
    hashSet = set()
    maxLen, cnt, curr = 1, 0, -math.inf
    for i in range(0, len(arr)):
      hashSet.add(arr[i])

    for key in hashSet:
      if (key-1 not in hashSet):
        curr, cnt = key, 1
        while(curr + 1 in hashSet):
          curr += 1
          cnt += 1
        maxLen = max(maxLen, cnt)
      
    return maxLen

if __name__ == "__main__":
  arr = [100, 200, 1, 3, 2, 4]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Longest Consecutive Subsequence:

Brute Force:
1. Initialize maxlength = 1, currentlength = 1 and run two nested loops performing linear search in inner loop for X+1 element in inner loop
2. For Each Found Element increment current length and perform max operation
TC -> O(n**2), SC -> O(1)

Better Approach:
1. Sort the entire array and initialize pointers cnt = 0, maxLength = 1 and lastSmaller = INT_MIN
2. If arr[i]-1 == lastSmaller increment cnt and perform max operation
3. If arr[i] == lastSmaller do nothing
4. If arr[i] != lastSmaller set cnt = 0, lastSmaller = arr[i]
TC -> O(n*log(n) + O(n)), SC -> O(1) If array sorted in place

Optimal Approach:
1. Initialize maxLength = 1, cnt = 0 and set data structure
2. Run loop to insert all elements in set
3. Run another in set to check if x-1 exists in set if it exists do nothing and continue iteration
4. If x-1 does not exist in set run another loop to check whether x+1 exists in set and keep incrementing and performing max
TC -> O(n) + O(2n) ~ O(3n), SC -> O(n)
"""