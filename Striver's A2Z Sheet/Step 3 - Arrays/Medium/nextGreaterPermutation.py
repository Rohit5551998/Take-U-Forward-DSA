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
  def reverse(self, arr, start, end):
    while (start < end):
      arr[start], arr[end] = arr[end], arr[start]
      start += 1
      end -= 1

  def findSolution(self, arr:List[int]):
    n = len(arr)
    breakPoint = -1
    for i in range(n-1, 0, -1):
      if (arr[i] > arr[i-1]):
        breakPoint = i-1
        break

    if (breakPoint == -1):
      self.reverse(arr, 0, n-1)
    else:
      for i in range(n-1, breakPoint, -1):
        if (arr[i] > arr[breakPoint]):
          arr[i], arr[breakPoint] = arr[breakPoint], arr[i]
          break
      self.reverse(arr, breakPoint+1, n-1)

    return arr

if __name__ == "__main__":
  arr = [2, 1, 5, 4, 3, 0, 0]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Next Greater Permutation:

Brute Force:
1. Find All Permutations of the given array using recursion in ascending order.
2. Search the current input in all the possible permutations.
3. Return the next greater permutation or the first one if the current input is the last one.
TC -> O(n!*n), SC -> O(1) excluding recursion stack.

Better Approach:
1. C++ STL has a function next_permutation() which can be used to find the next greater permutation.

Optimal Approach:
1. Find the first element from right which is smaller than the element 
next to it (referred as break point).
2. If not array is in decreasing order, reverse the array.
3. Find the first element from right which is greater than the element found in step 1.
4. Swap the elements found step 1(break point) and step 3.
5. Reverse the array from the (break point + 1) to the end.
TC -> O(3n), SC -> O(1).
"""