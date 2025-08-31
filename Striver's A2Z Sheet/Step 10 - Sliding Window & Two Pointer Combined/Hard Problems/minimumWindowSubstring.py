
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
  def findSolution1(self, s, t):
    minLen = math.inf
    startIndex = -1

    for i in range(0, len(s)):
      mpp = {} 
      cnt = 0

      for j in range(0, len(t)):
        if (t[j] not in mpp):
          mpp[t[j]] = 0
        mpp[t[j]] += 1

      for j in range(i, len(s)):
        if (s[j] not in mpp):
          mpp[s[j]] = 0

        if (mpp[s[j]] > 0): cnt += 1

        mpp[s[j]] -= 1

        if (cnt == len(t)): 
          if ((j-i+1) < minLen):
            startIndex = i
            minLen = j - i + 1
            break

    return s[startIndex:startIndex+minLen] if startIndex != -1 else ""

  def findSolution(self, s, t):
    minLen = math.inf
    startIndex = -1
    cnt = 0
    mpp = {}
    l = 0
    r = 0

    for i in range(0, len(t)):
      if (t[i] not in mpp):
        mpp[t[i]] = 0
      mpp[t[i]] += 1

    while (r < len(s)):
      if (s[r] not in mpp): mpp[s[r]] = 0

      if (mpp[s[r]] > 0): cnt += 1

      mpp[s[r]] -= 1

      while(cnt == len(t)):
        if (r - l + 1 < minLen):
          minLen = r - l + 1
          startIndex = l

        mpp[s[l]] += 1

        if (mpp[s[l]] > 0): cnt -= 1

        l += 1

      r += 1  

    return s[startIndex:startIndex+minLen] if startIndex != -1 else ""

if __name__ == "__main__":
  s = "ADOBECODEBANC"
  t = "ABC"
  print(Solution().findSolution(s, t))

"""
Minimum Window Substring
Brute Force
1. Initialize MinLen to Infinity and Start Index to -1 and run a for loop for s string elements
2. Initialize mpp = {} and run another loop for t string till len(t) and increment each element in mpp.
3. Run another nested loop for s sting elements and increment cnt if mpp[s[j]] > 0(present in t string)
4. Decrement mpp[s[j]] by 1 and check if cnt == len(t) and if (j - i + 1) < minLen.
5. If it is update minLen and assign startIndex to i and break out of loop
6. Return s[startIndex:startIndex+minLen] if startIndex != -1 else ""
TC -> O(N*N), SC -> O(256). Constant size set

Optimal Approach
1. Initialize minLen to inf, left, rightm cnt to 0, mpp to {}, startIndex to -1 and run a loop to insert all t elements to mpp.
2. Run a while loop and if arr[right] is not in mpp, set mpp[arr[right]] = 0 and if mpp[arr[right]] > 0 then increment cnt by 1
3. Afterwards decrement mpp[arr[right]] by 1
4. Run another while loop till cnt == len(t) and if (j - i + 1) < minLen, update minLen to (j - i + 1) and startIndex to l, 
5. Increment hash[s[l]] by 1 and if hash[s[l]] > 0 then decrement cnt by 1 finally increment l in while
6. At End of Inner While Increment r
7. Return s[startIndex:startIndex+minLen] if startIndex != -1 else ""
TC -> O(2N) + O(M), SC -> O(256)
"""