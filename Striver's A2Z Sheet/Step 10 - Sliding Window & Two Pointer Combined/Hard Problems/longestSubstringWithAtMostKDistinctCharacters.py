
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
      fruits = set()
      for j in range(i, len(arr)):
        fruits.add(arr[j])
        if (len(fruits) <= k):
          maxLen = max(maxLen, j-i+1)
        else:
          break
    return maxLen

  def findSolution2(self, arr, k):
    maxLen = 0
    mpp = {}
    l = 0
    r = 0

    while (r < len(arr)):
      if (arr[r] not in mpp):
        mpp[arr[r]] = 0
      mpp[arr[r]] += 1

      while (len(mpp) > k):
        mpp[arr[l]] -= 1
        if (mpp[arr[l]] == 0):
          del mpp[arr[l]]
        l += 1

      if (len(mpp) <= k):
        maxLen = max(maxLen, r - l + 1)

      r += 1
    return maxLen

  def findSolution(self, arr, k):
    maxLen = 0
    mpp = {}
    l = 0
    r = 0

    while (r < len(arr)):
      if (arr[r] not in mpp):
        mpp[arr[r]] = 0
      mpp[arr[r]] += 1

      if (len(mpp) > k):
        mpp[arr[l]] -= 1
        if (mpp[arr[l]] == 0):
          del mpp[arr[l]]
        l += 1

      elif (len(mpp) <= k):
        maxLen = max(maxLen, r - l + 1)

      r += 1
    return maxLen

if __name__ == "__main__":
  arr = "aaabbccd"
  k = 2
  print(Solution().findSolution(arr, k))

"""
Longest Substring With At Most K Distinct Characters
Brute Force
1. Initialize Max Length to 0 and run a for loop for array elements with fruits initialized to empty set
2. Run another loop from i till len(array) and add arr[j] to set.
3. If size of set is less than k compute length and perform max operation else break out of inner loop
4. Return maxLen
TC -> O(N*N), SC -> O(1). Constant size set

Optimal Approach 1
1. Initialize maxLen, left, right to 0, mpp to {} and run a loop till right < len(array)
2. If arr[right] is not in mpp, set mpp[arr[right]] = 0 and increment it by 1
3. Run another while loop till size of mpp is greater than k and decrement mpp[arr[left]] by 1 for each arr[left], if it is 0 
remove it from mpp and increment left at end of while.
4. If size of mpp is <= k compute len and then perform max operation, increment r and return maxAns at end of loop
TC -> O(2N) + O(256), SC -> O(256)

Optimal Approach 2 (Constant Max Window)
1. Initialize maxLen, left, right to 0, mpp to {} and run a loop till right < len(array)
2. If arr[right] is not in mpp, set mpp[arr[right]] = 0 and increment it by 1
3. If size of mpp is greater than k and decrement mpp[arr[left]] by 1 for each arr[left], if it is 0 remove it from mpp and 
increment left at end of while.
4. Else if size of mpp is <= k compute len and then perform max operation, increment r and return maxAns at end of loop
TC -> O(N) + O(256), SC -> O(256)
"""