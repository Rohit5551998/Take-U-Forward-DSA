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
  def calculateBouquets(self, arr: List[int], day: int, k: int):
    bouquets = 0
    cnt = 0
    for i in range(0, len(arr)):
      if (arr[i] <= day):
        cnt += 1
      else:
        bouquets += cnt // k
        cnt = 0
    bouquets += cnt // k
    return bouquets

  def findSolution1(self, arr: List[int], m: int, k:int):
    if (len(arr) < m*k):
      return -1

    for i in range(min(arr), max(arr)+1):
      bouquets = self.calculateBouquets(arr, i, k)
      if (bouquets >= m):
        return i
    return -1

  def findSolution(self, arr: List[int], m: int, k:int):
    ans = -1
    low, high = min(arr), max(arr)
    while (low <= high):
      mid = low + (high - low) // 2
      bouquets = self.calculateBouquets(arr, mid, k)
      if (bouquets < m):
        low = mid + 1
      else:
        high = mid - 1 
        ans = mid
    return ans


if __name__ == "__main__":
  arr = [7, 7, 7, 7, 13, 11, 12, 7]
  m = 2
  k = 3
  # arr = [1, 10, 3, 10, 2]
  # m = 3
  # k = 2
  resp = Solution().findSolution(arr, m, k)
  print(resp)


"""
Minimum Days of Days to Make M Bouquets
Brute Force
1. Run a Loop From Min(arr) to Max(arr) and calculate total bouquets for each day.
2. Inside Calculate Bouquets initialize cnt and bouquets = 0 
use array loop with logic if arr[i] <= day increment count by 1
3. Else Bouquets += cnt // k and reset cnt
4. At End of Loop again add to bouquets cnt to handle remaining non empty count
5. If Bouquets is greater than or equal to m return i 
6. At End of Loop Return -1
TC -> O((max(arr[])-min(arr[])+1) * n), SC -> O(1)

Optimal Approach
1. Initialize two pointers low = 1, high = max(arr), ans = -1
2. In loop calculate mid = low + (high - low) // 2
3. Calculate Total Bouquets for Mid and If arr[i] <= day increment count by 1 Else Bouquets += cnt // k and reset cnt
4. If Bouquets is less than m assign low = mid + 1
5. Else high = mid - 1 and ans = mid
5. Return ans.
TC -> O(log(max(arr[])-min(arr[])+1) * n), SC -> O(1)
"""