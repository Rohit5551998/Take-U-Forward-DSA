
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
  def findSolution1(self, arr):
    count = 0
    for i in range(0, len(arr)):
      mpp = {}
      for j in range(i, len(arr)):
        mpp[arr[j]] = 1
        if (mpp.get('a', 0) + mpp.get('b', 0) + mpp.get('c', 0) == 3):
          count += len(arr) - j
          break
    return count

  def findSolution(self, arr):
    count = 0
    mpp = {
      'a': -1, 'b': -1, 'c': -1
    }
    for i in range(0, len(arr)):
      mpp[arr[i]] = i
      mini = min(mpp['a'], mpp['b'], mpp['c'])
      if (mini != -1):
        count += 1 + mini
    return count

if __name__ == "__main__":
  arr = "abcabc"
  print(Solution().findSolution(arr))

"""
Number of Substring Containing All 3 Characters
Brute Force
1. Initialize Count to 0 and run a for loop for array elements with mpp initialized to {}.
2. Run another loop from i till len(array) and set mpp[arr[j]] to 1.
3. If safe get of a, b, c == 3 add n - j to count and break out of inner loop
4. Return count
TC -> O(N*N), SC -> O(1)

Optimal Approach
1. Initialize count to 0, mpp with all elements to -1 and run a loop till right < len(array)
2. Set mpp[arr[i]] to i and compute minimum index of all characters
3. If minimum is != -1 which means all elements are found add 1 + minimum index to count indicating all previous characters
can also form valid substrings
4. At End of Loop Return Count
TC -> O(N), SC -> O(1)
"""