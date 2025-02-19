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
  def findSolution1(self, arr: List[int]):
    maxLen = 0
    for i in range(0, len(arr)):
      sum = arr[i]
      for j in range(i+1, len(arr)):
        sum += arr[j]
        if (sum == 0):
          maxLen = max(maxLen, j - i + 1)
    return maxLen
  
  def findSolution(self, arr: List[int]):
    maxLen, sum = 0, 0
    prefixSumHash = {}

    for i in range(0, len(arr)):
      sum += arr[i]

      if (sum == 0): maxLen = max(maxLen, i+1)
      else:
        remove = sum
        if (remove in prefixSumHash):
          maxLen = max(maxLen, i - prefixSumHash[remove])
        if (sum not in prefixSumHash):
          prefixSumHash[sum] = i
    return maxLen

  
if __name__ == "__main__":
  arr = [9, -3, 3, -1, 6, -5]
  resp = Solution().findSolution(arr)
  print(resp)


"""
#Brute Force:
1. Run two Nested Loops Calculating Sum along the way in inner loop
2. Check Whether this sum is equal to K
3. If it is equal to K take max of current longest and index range
TC -> O(n**2), SC -> O(1)

#Better Approach (Optimal If Array Contains Negatives):
1. Initialize Hash Map To Store Prefix Sum of Elements With Index Upto A Given Index
2. Check If Current Sum if Equal to K if yes then take max
3. When at element with sum x check whether k-x exists in prefixSumMap. 
4. If it exists Take Difference Of current position and stored index To Get Length of SubArray
5. Take Max of Current Longest and the New Length of SubArray
6. Edge Case: If Prefix Sum Already exists in Array do not update as in case of zeroes we want to take sum from
left most elements ie [2, 0, 0, 3] with k = 3 should have answer [0, 0, 3]
TC -> O(n*log(n)) or O(n) depending on type of Map & SC -> O(n)
"""