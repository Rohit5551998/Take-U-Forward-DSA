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

  def findSolution1(self, arr:List[int]):
    output = []
    for i in range(0, len(arr)):
      flag = True
      for j in range(i+1, len(arr)):
        if (arr[j] > arr[i]):
          flag = False
          break
      if (flag):
        output.append(arr[i])
    return output

  def findSolution(self, arr:List[int]):
    output = []
    max = -math.inf

    for i in range(len(arr)-1, -1, -1):
      if (arr[i] >= max):
        max = arr[i]
        output.append(arr[i])
    self.reverse(output, 0, len(output)-1)
    return output


if __name__ == "__main__":
  arr = [10, 4, 2, 4, 1]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Leaders in an Array:

Brute Force:
1. Take each element and check if it is greater than all the elements to its right or not.
2. Use Two Nested Loops to check this condition and add to output array
TC -> O(n**2), SC -> O(1) excluding output array

Optimal Approach:
1. Start from end of the array and keep track of the maximum element found so far.
2. If the current element is greater than the maximum element found so far, then it is a leader.
3. Update the maximum element found so far to the current element.
4. Reverse the output array to get the leaders in the correct order.
TC -> O(n), SC -> O(1) excluding output array
"""