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
  def findSolution1(self, arr):
    stack = LifoQueue()
    ans = [0 for i in range(len(arr))] 
    for i in range(len(arr)-1, -1, -1):
      while(not stack.empty() and arr[i] > stack.queue[-1]):
        stack.get()
      ans[i] = -1 if stack.empty() else stack.queue[-1]
      stack.put(arr[i])
    return ans
  
  def findSolution(self, arr):
    stack = LifoQueue()
    ans = {} 
    for i in range(len(arr)-1, -1, -1):
        while(not stack.empty() and arr[i] > stack.queue[-1]):
            stack.get()
        ans[arr[i]] = -1 if stack.empty() else stack.queue[-1]
        stack.put(arr[i])
    
    return ans

if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  arr = [1, 2, 3, 4, 5, 6, 7]
  print(Solution().findSolution(arr))

"""
Next Greater Element
Optimal Approach
1. Check if head or head.next is None and return head as LL is already sorted
2. Find the first middle element and split the linked list in half recursively
3. Once done apply merging algorithm on left and right halves to get sorted LL and update head of new linked list
4. Return the updated head
TC -> O((N + N/2) * log N), SC -> O(1)
"""