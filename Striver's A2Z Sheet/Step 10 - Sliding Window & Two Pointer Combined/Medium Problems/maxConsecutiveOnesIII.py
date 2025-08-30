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

from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
  def findSolution1(self, arr, k):
    maxLen = 0
    for i in range(0, len(arr)):
      zeroes = 0
      for j in range(i, len(arr)):
        if (arr[j] == 0):
          zeroes += 1
        if (zeroes <= k): 
          length = j - i + 1
          maxLen = max(maxLen, length)
        else:
          break
    return maxLen

  def findSolution2(self, arr, k):
    maxLen = 0
    zeroes = 0
    l = 0
    r = 0
    while (r < len(arr)):
      if (arr[r] == 0):
        zeroes += 1

      while(zeroes > k):
        if (arr[l] == 0):
          zeroes -= 1
        l += 1

      maxLen = max(maxLen, r-l+1)

      r += 1
    return maxLen
  
  def findSolution(self, arr, k):
    maxLen = 0
    zeroes = 0
    l = 0
    r = 0
    while (r < len(arr)):
      if (arr[r] == 0):
        zeroes += 1

      if (zeroes > k):
        if (arr[l] == 0):
          zeroes -= 1
        l += 1
      else:
        maxLen = max(maxLen, r-l+1)

      r += 1
    return maxLen

if __name__ == "__main__":
  arr = [1,1,1,0,0,0,1,1,1,1,0]
  k = 2
  print(Solution().findSolution(arr, k))

"""
Max Consecutive Ones III
Brute Force
1. Initialize Max Length to 0 and run a for loop for array elements with zeroes initialized to 0
2. Run another loop from i till len(array) and if arr[j] == 0 increment zeroes by 1.
3. If count of zeroes is less than k compute length and perform max operation else break out of inner loop
4. Return maxLen
TC -> O(N*N), SC -> O(1)

Optimal Approach 1
1. Initialize maxLen, zeroes, left, right to 0 and run a loop till right < len(array)
2. If arr[right] == 0 increment zeroes by 1
3. Run another while loop till zeroes is greater than k and decrement zeroes for each arr[left] == 0 and increment left by 1
4. Compute len and then perform max operation, increment r and return maxAns at end of loop
TC -> O(2N), SC -> O(1)

Optimal Approach 2 (Constant Max Window)
1. Initialize maxLen, zeroes, left, right to 0 and run a loop till right < len(array)
2. If arr[right] == 0 increment zeroes by 1
3. Check if zeroes is greater than k and decrement zeroes for each arr[left] == 0 and increment left by 1
4. Else compute len and then perform max operation and increment r in both cases
return maxAns at end of loop
TC -> O(N), SC -> O(1)
"""