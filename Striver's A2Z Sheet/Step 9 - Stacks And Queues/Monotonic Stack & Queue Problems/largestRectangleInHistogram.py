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

  def findNSE(self, arr):
    st = LifoQueue()
    ans = [0 for _ in range(len(arr))]
    for i in range(len(arr)-1, -1, -1):
      while(not st.empty() and arr[i] <= arr[st.queue[-1]]):
        st.get()
      ans[i] = len(arr) if st.empty() else st.queue[-1]
      st.put(i)
    return ans
  
  def findPSEE(self, arr):
    st = LifoQueue()
    ans = [0 for _ in range(len(arr))]
    for i in range(0, len(arr)):
      while(not st.empty() and arr[i] < arr[st.queue[-1]]):
        st.get()
      ans[i] = -1 if st.empty() else st.queue[-1]
      st.put(i)
    return ans

  def findSolution1(self, arr):
    nse = self.findNSE(arr)
    psee = self.findPSEE(arr)
    maxi = 0
    for i in range(0, len(arr)):
      maxi = max(maxi, (nse[i] - psee[i] - 1) * arr[i])
    return maxi

  def findSolution(self, arr):
    st = LifoQueue()
    maxi = 0

    for i in range(0, len(arr)):
      while(not st.empty() and arr[i] <= arr[st.queue[-1]]):
        # While Popping the first element will be whose area needs to be calculated
        # the next top element will be the previous smaller element and i will be the next smaller element
        element = arr[st.get()]
        pse = -1 if st.empty() else st.queue[-1]
        nse = i
        maxi = max(maxi, (nse - pse - 1) * element)
      st.put(i)

    while(not st.empty()):
      element = arr[st.get()]
      pse = -1 if st.empty() else st.queue[-1]
      nse = len(arr)
      maxi = max(maxi, (nse - pse - 1) * element)

    return maxi



if __name__ == "__main__":
  arr = [1, 2, 3]
  # arr = [1, 3, 3]
  # arr = [2,1,5,6,2,3]
  # arr = [2, 4]
  print(Solution().findSolution(arr))

"""
Largest Rectangle In Histogram
Brute Force
1. Run a loop over the array, initialize mini to infinity and for every element run another loop till n with j=i.
2. Find minimum element in inner loop and then calculate max area using formula max((j-i+1) * mini, maxi)
3. Return the maxi
TC -> O(N**2), SC -> O(1)

Optimal Approach 1
1. Find the nse and psee for each element in the array and initialize maxi to 0
2. Run a loop over array and calculate area using formula (nse[i] - psee[i] - 1) * arr[i]
3. Return the maxi
TC -> O(5N), SC -> O(4N)

Optimal Approach 2 (Single Pass Approach)
1. Initialize maxi to 0 and run a loop over array
2. Check in while whether current element is <= top of stack, if yes then pop it and compute array with arr[i] as popped 
element, nse = i(current smaller than arr[i]), pse = -1 / next top of stack
3. At end of while add current element to stack
4. At end of loop run another while loop to pop all elements from stack and compute area using formula (nse - pse - 1) * arr[i]
5. Return the maxi
TC -> O(2N), SC -> O(N)
"""