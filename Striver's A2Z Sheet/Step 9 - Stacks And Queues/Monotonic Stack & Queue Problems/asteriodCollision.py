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
    st = LifoQueue()

    for i in range(0, len(arr)):
      if (arr[i] > 0):
        st.put(arr[i])
      else:
        while (not st.empty() and st.queue[-1] > 0 and st.queue[-1] < abs(arr[i])):
          st.get()
        if (not st.empty() and st.queue[-1] == abs(arr[i])):
          st.get()
        elif (st.empty() or st.queue[-1] < 0):
          st.put(arr[i])
    return list(st.queue)

if __name__ == "__main__":
  # arr = [1, 2, 3]
  # arr = [1, 3, 3]
  # arr = [-5,-5,-4, -5 ]
  arr = [-3, 4, 7, 1, 1, 2, -3, -7, 17, 15, -18, -19]
  print(Solution().findSolution(arr))

"""
Asteriod Collision
Optimal Approach
1. Iterate through the asteriods array and if positive element is found, push it to the stack.
2. If negative element if found run a while loop to check whether stack is not empty with positive element less than 
absolute value of negative element and pop all elements till this condition is true.
3. After this check if stack is not empty and top element is equal to absolute value of negative element, pop the top element.
4. Else if stack is empty or top element is negative, push the current negative element to the stack.
5. At the end return the stack elements.
TC -> O(2N), SC -> O(N)
"""