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
  def findSolution(self, arr: List[List[int]]):
    n, m = len(arr), len(arr[0])
    top, right, bottom, left = 0, m-1, n-1, 0
    output = []
    while (top <= bottom and left <= right):
      for i in range(left, right+1):
        output.append(arr[top][i])
      top += 1

      for i in range(top, bottom+1):
        output.append(arr[i][right])
      right -= 1
      
      if (top <= bottom): #To avoid index issues for single row or column
        for i in range(right, left-1, -1):
          output.append(arr[bottom][i]) 
        bottom -= 1

      if (left <= right):
        for i in range(bottom, top-1, -1):
          output.append(arr[i][left])
        left += 1
    return output


if __name__ == "__main__":
  arr = [ [ 1, 2, 3, 4 ],
		      [ 5, 6, 7, 8 ],
		      [ 9, 10, 11, 12 ],
	              [ 13, 14, 15, 16 ] ]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Spiral Traversal of Matrix:

Optimal Approach:
1. Initialize Four Pointers top, right, left & bottom.
2. Direction for traversal will be from left -> right, top -> bottom, right -> left, bottom -> top
3. At end of each loop decrement or increment top, right, bottom and left as required
4. At beginning of 3rd & 4th direction check first if elements still need to be traversed or not
TC -> O(N*M), SC -> O(n) (For Storing Output)
"""