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
    maxProduct = -math.inf
    for i in range(0, len(arr)):
      for j in range(i, len(arr)):
        product = 1
        for k in range(i, j+1):
          product *= arr[k]
        maxProduct = max(maxProduct, product)
    return maxProduct
  
  def findSolution2(self, arr:List[int]):
    maxProduct = -math.inf
    for i in range(0, len(arr)):
      product = 1
      for j in range(i, len(arr)):
        product *= arr[j]
        maxProduct = max(maxProduct, product)
    return maxProduct
    
  def findSolution3(self, arr: List[int]):
    maxProduct = arr[0]
    prod1, prod2 = arr[0], arr[0]

    for i in range(1, len(arr)):
      prod1, prod2 = max(arr[i], arr[i]*prod1, arr[i]*prod2), min(arr[i], arr[i]*prod1, arr[i]*prod2)
      maxProduct = max(maxProduct, prod1)

    return maxProduct


  def findSolution(self, arr: List[int]):
    maxProduct = -math.inf
    prefix, suffix = 1, 1
    for i in range(0, len(arr)):
      if (prefix == 0): prefix = 1
      if (suffix == 0): suffix = 1
      prefix *= arr[i]
      suffix *= arr[len(arr)-1-i]
      maxProduct = max(prefix, suffix, maxProduct)
    return maxProduct

if __name__ == "__main__":
  arr = [1,2,-3,0,-4,-5]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Brute Force:
Calculate Product of All Subarrays Using 3 Loops
TC: O(n**3) SC: O(1)

Better Approach:
Calculate Product of All Subarrays Using 2 Loops and add the current element to the product of previous subarray
to get the product of current subarray instead of using another loop each time
TC: O(n**2), SC: O(1)

Optimal Approach #1:
1. Initialize variables prefix = 1, suffix = 1 to store prefix and suffix product
2. Run a loop and calculate prefix and suffix product for each element
3. If 0 is encountered, reset the prefix and suffix product to 1
4. Return the maximum product
TC: O(n), SC: O(1)

Optimal Approach #2 (Modified Kadane's Algorithm):
1. Initially store 0th index value in prod1, prod2 and result.
2. Traverse the array from 1st index. 
3. For each element, update prod1 and prod2.
4. Prod1 is maximum of current element, product of current element and prod1, product of current element and prod2
5. Prod2 is minimum of current element, product of current element and prod1, product of current element and prod2
6. Return maximum of result and prod1
TC: O(n) SC: O(1)
"""