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
  def assignCows(self, arr: List[int], distance: int, k: int):
    last = arr[0]
    cntCows = 1
    for i in range(1, len(arr)):
      if (arr[i] - last >= distance):
        cntCows += 1
        last = arr[i]
      if (cntCows >= k): 
        return True
    return False

  def findSolution1(self, arr: List[int], k:int):
    arr.sort()
    limit = arr[len(arr) - 1] - arr[0]

    for i in range(1, limit+1):
      if (not self.assignCows(arr, i, k)):
        return (i-1)
    return limit

  def findSolution(self, arr: List[int], k:int):
    arr.sort()
    ans = arr[-1]
    low, high = 1, arr[len(arr) - 1] - arr[0]
    while (low <= high):
      mid = low + (high - low) // 2
      if (self.assignCows(arr, mid, k)):
        ans = mid
        low = mid + 1
      else:
        high = mid - 1
    return ans


if __name__ == "__main__":
  arr = [0,3,4,7,10,9]
  k = 4
  resp = Solution().findSolution(arr, k)
  print(resp)


"""
Aggressive Cows
Brute Force
1. Run a Loop From 1 to Max-Min of sorted array and assign cows to stalls
2. Inside Assign Cows initialize cowCnt = 1 and last = arr[0]
use array loop with logic if arr[i] - last >= distance then set last to arr[i] and increment cowCnt
3. Inside Loop If cowCnt >= k return True else at end of loop return False
4. The Point at which the function returns false, the previous value is the answer 
6. At End of Loop Return -1
TC -> O(nlogn) + O(n *(max(stalls[])-min(stalls[]))), SC -> O(1)

Optimal Approach
1. Initialize two pointers low = 1, high = max-min, ans = arr[-1] in sorted array
2. In loop calculate mid = low + (high - low) // 2
3. Inside Assign Cows initialize cowCnt = 1 and last = arr[0]
use array loop with logic if arr[i] - last >= distance then set last to arr[i] and increment cowCnt
4. Inside Loop If cowCnt >= k return True else at end of loop return False
5. If the function returns true assign low = mid + 1 and ans = mid
6. Else high = mid - 1
7. Return ans.
TC -> O(nlogn) + O(n * log(max(stalls[])-min(stalls[]))), SC -> O(1)
"""