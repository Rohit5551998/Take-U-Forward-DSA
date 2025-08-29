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
    maxPoints = 0
    sumPoints = 0
    n = len(arr)
    for i in range(0, k):
      sumPoints += arr[i]

    maxPoints = sumPoints

    for i in range(k-1, -1, -1):
      sumPoints -= arr[i]
      sumPoints += arr[n + i - k]
      maxPoints = max(maxPoints, sumPoints)

    return maxPoints

if __name__ == "__main__":
  arr = [1,2,3,4,5,6,1]
  k = 3
  print(Solution().findSolution(arr, k))

"""
Maximum Points From Cards
Optimal Approach
1. Initialize maxPoints, sumPoints to 0 and run a loop to find sum of first k elements and assign them to both variables defined.
2. Run another loop starting from k-1 till 0 and and decrement ith value from left and increment n-i+kth value from right in sum.
3. Once done update compute max of current sum and current max and at end of loop return maxSum
TC -> O(2K), SC -> O(1)
"""