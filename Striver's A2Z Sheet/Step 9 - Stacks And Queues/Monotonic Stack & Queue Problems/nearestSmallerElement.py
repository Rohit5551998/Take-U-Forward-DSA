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
  def findSolution(self, arr):
    stack = LifoQueue()
    ans = [0 for i in range(len(arr))] 
    for i in range(0, len(arr)):
      while(not stack.empty() and arr[i] <= stack.queue[-1]):
        stack.get()
      ans[i] = -1 if stack.empty() else stack.queue[-1]
      stack.put(arr[i])
    return ans


if __name__ == "__main__":
  # arr = [2, 4, 6, 7, 5, 1, 0]
  # arr = [1, 2, 3, 4, 5, 6, 7]
  arr = [ 39, 27, 11, 4, 24, 32, 32, 1 ]
  print(Solution().findSolution(arr))

"""
Next Smaller Element
Brute Force
1. Run a loop over the array and for every element run another loop till next previous smaller element is found.
2. If found add to answer and break loop else add -1 to ans array.
3. Return the final ans array
TC -> O(N**2), SC -> O(n)

Optimal Approach
1. Iterate over the array
2. While Stack is not empty and element is smaller than stack top pop stack elements
3. If stack is empty add -1 to ans array else add stack top to ans array
4. Push the current element to stack
5. Return the ans array
TC -> O((N + N/2) * log N), SC -> O(2n)
"""