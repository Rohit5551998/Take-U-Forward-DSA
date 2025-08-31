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
      mpp = {}
      maxFreq = 0
      for j in range(i, len(arr)):
        if (arr[j] not in mpp):
          mpp[arr[j]] = 0
        mpp[arr[j]] += 1

        maxFreq = max(maxFreq, mpp[arr[j]])

        changes = (j - i + 1) - maxFreq

        if (changes <= k):
          maxLen = max(maxLen, j - i + 1)
        else:
          break
    return maxLen

  def findSolution2(self, arr, k):
    maxLen = 0
    maxFreq = 0
    mpp = {}
    l = 0
    r = 0
    while (r < len(arr)):
      if (arr[r] not in mpp):
        mpp[arr[r]] = 0
      mpp[arr[r]] += 1

      maxFreq = max(maxFreq, mpp[arr[r]])

      while((r-l+1) - maxFreq > k):
        mpp[arr[l]] -= 1
        l += 1

      if ((r-l+1) - maxFreq <= k):
        maxLen = max(maxLen, r-l+1)

      r += 1
    return maxLen
  
  def findSolution(self, arr, k):
    maxLen = 0
    maxFreq = 0
    mpp = {}
    l = 0
    r = 0
    while (r < len(arr)):
      if (arr[r] not in mpp):
        mpp[arr[r]] = 0
      mpp[arr[r]] += 1

      maxFreq = max(maxFreq, mpp[arr[r]])

      if((r-l+1) - maxFreq > k):
        mpp[arr[l]] -= 1
        l += 1

      elif ((r-l+1) - maxFreq <= k):
        maxLen = max(maxLen, r-l+1)

      r += 1
    return maxLen

if __name__ == "__main__":
  arr = "AABABBA"
  k = 1
  print(Solution().findSolution(arr, k))

"""
Longest Repeating Character Replacement
Brute Force
1. Initialize Max Length to 0 and run a for loop for array elements with mpp initialized to {} and maxFreq = 0
2. Run another loop from i till len(array) and increment frequency in mpp by 1.
3. Compute Max Freq of current element and previous max and changes required till current index will be (j+i-1) - maxFreq
4. If this values is <= k compute maxLen else break out of inner loop
5. Return maxLen
TC -> O(N*N), SC -> O(1)

Optimal Approach 1
1. Initialize maxLen, maxFreq, left, right to 0, mpp to {} and run a loop till right < len(array)
2. Increment mpp[arr[r]] by 1 and compute maxFreq of current element and previous max
3. Run another while loop till (j+i-1) - maxFreq > k and decrement mpp[arr[left]] by 1 and increment left by 1
4. If (j+i-1) - maxFreq <= k Compute len and then perform max operation, increment r and return maxAns at end of loop
TC -> O(2N), SC -> O(1)

Optimal Approach 2 (Constant Max Window)
1. Initialize maxLen, maxFreq, left, right to 0, mpp to {} and run a loop till right < len(array)
2. Increment mpp[arr[r]] by 1 and compute maxFreq of current element and previous max
3. If (j+i-1) - maxFreq > k and decrement mpp[arr[left]] by 1 and increment left by 1
4. Elif (j+i-1) - maxFreq <= k Compute len and then perform max operation, increment r and return maxAns at end of loop
TC -> O(N), SC -> O(1)
"""