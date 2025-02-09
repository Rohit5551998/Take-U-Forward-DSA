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
    resp = None
    n = len(arr)//2

    for i in range(len(arr)):
      cnt = 1
      for j in range(i+1, len(arr)):
        if (arr[j] == arr[i]):
          cnt += 1
      if (cnt > n):
        return arr[i]

    return resp
  
  def findSolution2(self, arr:List[int]):
    n = len(arr)//2
    hashMap = {}

    for i in range(len(arr)):
      if (arr[i] not in hashMap):
        hashMap[arr[i]] = 0
      hashMap[arr[i]] += 1

    for k,v in hashMap.items():
      if (v > n):
        return k

    return None
  
  def findSolution(self, arr:List[int]):
    counter, majorityElement = 1, arr[0]
    for i in range(1, len(arr)):
      if (counter == 0):
        majorityElement = arr[i]

      if (arr[i] == majorityElement):
        counter += 1
      else: 
        counter -= 1
    cnt = 0
    for i in range(len(arr)):
      if (arr[i] == majorityElement):
        cnt += 1
    if (cnt > len(arr)//2):
      return majorityElement
    return -1

if __name__ == "__main__":
  # arr = [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4]
  arr = [2, 2, 1, 1, 1, 2, 2]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Majority Element

Brute Force:
1. Run Two Nested Loops and Find Occurence of Each Element
2. Check If it is greater than floor of n/2 and return it found
TC -> O(n**2), SC -> O(1)

Better Approach:
1. Use HashMap to Store Occurence of Each Element
2. Run Through HashMap and check if any element has occurence > floor of n/2
TC -> O(n) + O(n*log(n)) / O(2n), SC -> O(n)

Optimal Approach (Moore's Voting Algorithm):
1. Initialize Counter = 1 and majorityElement = arr[0]
2. Run Through Array and Check If Majority Element is Same as Current Element and increment counter
3. Else Decrement Counter and If Counter becomes 0, Update Majority Element to Next Element and Counter to 1
4. Return Majority Element at the End If Proper Majority Element Always Exists as Per Statement
5. If not run another loop to check if the assumed majority element is actually majority element
TC -> O(n)/O(2n), SC -> O(1)
"""