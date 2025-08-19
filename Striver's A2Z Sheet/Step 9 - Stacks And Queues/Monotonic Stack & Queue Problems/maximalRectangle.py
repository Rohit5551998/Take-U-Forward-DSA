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

from queue import PriorityQueue, Queue, LifoQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:

  def largestRectangleInHistogram(self, arr):
    st = []
    maxi = 0

    for index, value in enumerate(arr):
      while(st and value <= arr[st[-1]]):
        element = arr[st.pop()]
        pse = -1 if not st else st[-1]
        nse = index
        maxi = max(maxi, (nse - pse - 1) * element)
      st.append(index)
    
    while(st):
      element = arr[st.pop()]
      pse = -1 if not st else st[-1]
      nse = len(arr)
      maxi = max(maxi, (nse - pse - 1) * element)
    
    return maxi

  def findSolution(self, arr):
    maxi = 0
    n = len(arr)
    m = len(arr[0])
    pseudoArray = [[0 for _ in range(m)] for _ in range(n)]

    for j in range(0, m):
      sum = 0
      for i in range(0, n):
        sum += int(arr[i][j])
        if (int(arr[i][j]) == 0):
          sum = 0
        pseudoArray[i][j] = sum

    for i in range(0, n):
      maxi = max(maxi, self.largestRectangleInHistogram(pseudoArray[i]))

    return maxi

if __name__ == "__main__":
  arr = matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
  print(Solution().findSolution(arr))

"""
Maximal Rectangle
Optimal Approach
1. Iterate through the matrix and generate pseudo array by looping throught columns them rows and adding 1 to previous element
and resetting value to 0 if current element is 0 assign the sum value to pseudoArray[i][j].
2. Run a loop to call largestRectangleInHistogram function to find the maximum area of the histogram for each row.
3. Return the maximum area.
TC -> O(N*M) + O(N*2M), SC -> O(N*M) + O(M)
"""