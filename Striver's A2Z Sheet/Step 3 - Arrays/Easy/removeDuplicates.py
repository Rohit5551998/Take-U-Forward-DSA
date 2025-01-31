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

  def findSolution(self, arr:List[int]):
    i = 0
    for j in range(1, len(arr)):
      if (arr[i] != arr[j]):
        i += 1
        arr[i] = arr[j]
    print(arr)
    return i+1

if __name__ == "__main__":
  arr = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Remove Duplicates From Sorted Array

Brute Force:
Initialize Set With All Array Elements then fill set elements into array
TC: O(nlogn), SC: O(n)

Optimal:
Two Pointer Approach
Initialize Pointers i=0, j=1
If Current is not equal to arr[i] Increment i and swap with j
Return i+1 to find unique elements
TC: O(n), SC: O(1)
"""