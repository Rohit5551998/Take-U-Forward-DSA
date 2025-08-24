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

from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
  def findSolution(self, arr, k):
    queue = deque()
    ans = []
    for i in range(0, len(arr)):
      #Remove elements from queue till window is valid
      if(queue and queue[0] < i-k+1):
        queue.popleft()

      #Remove elements from monotonic stack till new element is greater than top of stack
      while(queue and arr[queue[-1]] <= arr[i]):
        queue.pop()

      queue.append(i)

      #If window is valid, add the max element to the answer
      if (i >= k-1): ans.append(arr[queue[0]])

    return ans

if __name__ == "__main__":
  arr = [1,3,-1,-3,5,3,6,7]
  arr = [1,3,1,2,0,5]
  k = 3
  print(Solution().findSolution(arr, k))

"""
Sliding Window Maximum
Optimal Approach
1. Iterate through the array and first check if queue is not empty and current window is out of bound for i(queue[0] < i-k+1).
If it is remove from front of queue.
2. While queue is not empty and current element is greater than the top of queue, then remove queue top. (To maintain monotonic
stack)
3. Now append the current element to the queue and if window is valid, add the bottom of stack to the answer.
TC -> O(2N), SC -> O(K)
"""