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
  def findSolution(self, str, k):
    st = []
    for i, value in enumerate(str):
      while(st and k > 0 and st[-1] > value):
        k -= 1
        st.pop()
      st.append(value)
    
    if (not st): return "0"

    while(st and k > 0):
      k -= 1
      st.pop()

    while(st and st[0] == "0"):
      st = st[1:]

    if (not st): return "0"

    return "".join(st)

if __name__ == "__main__":
  # str, k = "1432219", 3
  # str, k = "10200", 1
  str, k = "010", 2
  print(Solution().findSolution(str, k))

"""
Remove K Digits
Optimal Approach
1. Iterate through string and keep removing the top of stack if current element is less than top of stack and k > 0 and append
current element to stack at end of while loop
2. If stack is empty, return "0"
3. If stack exists and k is still greater than 0, then keep removing the top of stack as string is in ascending order
4. Now remove any leading zeros from stack while stack is not empty then check if stack is empty, if it is return "0"
5. Else return the stack as string
TC -> O(N), SC -> O(N)
"""