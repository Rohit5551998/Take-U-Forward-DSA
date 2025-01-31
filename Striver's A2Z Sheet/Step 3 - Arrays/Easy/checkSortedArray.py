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

  def findSolutionWithRotation(self, arr:List[int]):
    isSorted = 1 
    for i in range(1, len(arr)):
      if (arr[i-1] > arr[i]):
        isSorted = 0
        break

    return (isSorted == 1)
  
  def findSolution(self, arr:List[int]):
    count = 0
    for i in range(0, len(arr)):
      if (arr[i-1] > arr[i]):
        count += 1
    return (count <= 1)
    

if __name__ == "__main__":
  arr = [18, 5, 4, 10, 3, 1, 6, 17, 2]
  arr1 = [1, 2, 3, 4, 5, 6]
  arr2 = [3, 4, 5, 1, 2]
  resp = Solution().findSolution(arr)
  resp1 = Solution().findSolution(arr1)
  resp2 = Solution().findSolution(arr2)
  print(resp, resp1, resp2)


"""
Compare Last Element with Current Element to check if it is smaller or not
TC: O(n), SC: O(1)

For Sorted Array the number of rotation points should be less than equal to 1
This means atmost you can encounter one position where a[i-1] > a[i]
If this count exceeds 1 then the rotated array is not sorted
"""