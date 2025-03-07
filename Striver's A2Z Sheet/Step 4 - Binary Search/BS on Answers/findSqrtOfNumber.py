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

  def findSolution(self, k:int):
    low, high = 0, k
    ans = 1
    while (low <= high):
      mid = low + (high - low) // 2
      if (mid * mid <= k):
        ans = mid
        low = mid + 1
      else:
        high = mid - 1
    return ans


if __name__ == "__main__":
  resp = Solution().findSolution(28)
  print(resp)


"""
Find Sqrt of Number
Optimal Approach
1. Initialize two pointers low = 0, high = n - 1
2. In loop calculate mid = low + (high - low) // 2
3. Check if mid * mid <= k, assign it to ans and assign low = mid + 1
4. Else assign high = mid - 1
5. Return ans.
TC -> O(log(n)), SC -> O(1)
"""