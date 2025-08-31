
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
  def findSolution(self, arr, k):
    cnt = 0
    for i in range(0, len(arr)):
      mpp = {}
      for j in range(i, len(arr)):
        if (arr[j] not in mpp):
          mpp[arr[j]] = 0
        mpp[arr[j]] += 1
        if (len(mpp.keys()) == k):
          cnt += 1
        elif (len(mpp.keys()) > k):
          break
    return cnt

  def findSolution2(self, arr, k):
    return self.countSubArraysWithUptoKDistinct(arr, k) - self.countSubArraysWithUptoKDistinct(arr, k-1)

  def countSubArraysWithUptoKDistinct(self, arr, k):
    cnt = 0
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

      cnt += (r - l + 1)

      r += 1
    return cnt

if __name__ == "__main__":
  arr = [1,2,1,2,3]
  k = 2
  print(Solution().findSolution(arr, k))

"""
Longest Substring With At Most K Distinct Characters
Brute Force
1. Initialize cnt to 0 and run a for loop for array elements with fruits initialized to empty map
2. Run another loop from i till len(array) and increment arr[j] in mpp.
3. If size of map keys == k then add 1 to count else if it is > k break out of inner loop
4. Return maxLen
TC -> O(N*N), SC -> O(N)

Optimal Approach
1. Write helper function and initialize cnt, left, right to 0, mpp to {} and run a loop till right < len(array)
2. If arr[right] is not in mpp, set mpp[arr[right]] = 0 and increment it by 1
3. Run another while loop till size of mpp is greater than k and decrement mpp[arr[left]] by 1 for each arr[left], if it is 0 
remove it from mpp and increment left at end of while.
4. If size of mpp is <= k add (r - l + 1) to cnt, increment r and return cnt at end of loop
5. Call the written function with k & k-1 and return difference of counts
TC -> O(4N), SC -> O(N)
"""