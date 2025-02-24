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
  def findSolution1(self, n: int, m: int, arr1: List[int], arr2: List[int]):
    arr3 = []
    left, right = 0, 0
    while (left < n and right < m):
      if (arr1[left] <= arr2[right]):
        arr3.append(arr1[left])
        left += 1
      else:
        arr3.append(arr2[right])
        right += 1
    
    while (left < n):
      arr3.append(arr1[left])
      left += 1

    while (right < m):
      arr3.append(arr2[right])
      right += 1

    for i in range(0, len(arr3)):
      if (i < n): arr1[i] = arr3[i]
      else: arr2[i-n] = arr3[i]
    return arr1,arr2

  def findSolution2(self, n: int, m: int, arr1: List[int], arr2: List[int]):
    end, start = len(arr1)-1, 0
    while (end > 0 and start < len(arr2)):
      if (arr1[end] > arr2[start]):
        arr1[end], arr2[start] = arr2[start], arr1[end]
        end -= 1
        start += 1
      else:
        break
    arr1.sort()
    arr2.sort()
    return arr1, arr2
  
  def swapArr(self, arr1: List[int], arr2: List[int], left, right):
    if (arr1[left] > arr2[right]):
      arr1[left], arr2[right] = arr2[right], arr1[left]

  def findSolution(self, n: int, m: int, arr1: List[int], arr2: List[int]):
    len = n + m
    gap = (len // 2) + (len % 2)
    while (gap > 0):
      left = 0
      right = left + gap

      while (right < len):
        #Both Elements In Different Arrays
        if (left < n and right >= n):
          self.swapArr(arr1, arr2, left, right-n)
        #Both Elements In Arr2
        elif (left >= n):
          self.swapArr(arr2, arr2, left-n, right-n)
        #Both Elements In Arr1
        else:
          self.swapArr(arr1, arr1, left, right)
        left += 1
        right += 1
      
      if gap == 1:
        break
      gap = (gap // 2) + (gap % 2)

    return arr1, arr2
  
if __name__ == "__main__":
  n = 4 
  arr1 = [1, 4, 8, 10] 
  m = 5 
  arr2 = [2, 3, 5, 6, 9]
  resp = Solution().findSolution(n, m, arr1, arr2)
  print(resp)


"""
Merge Two Sorted Arrays
#Brute Force:
1. Use 3rd Array to Store Sorted Output of Both Arrays
2. Use Loops to compare and store elements in third array and exhaust both arrays in case length in not reached
3. Once done run loop till length of 3rd Array and if i < n then assign tof first array
4. Else arr2[i-n] = arr[i]
TC ->O(n+m) + O(n+m), SC -> O(1)

#Optimal Solution 1:
1. Start from end of first array and start of second array
2. Exchange elements till arr1[end] > arr2[start] break once not found anymore
3. Sort both arrays
TC -> O(min(n, m)) + O(n*logn) + O(m*logm), SC -> O(n+m)

#Optimal Solution 2 (Gap Method --> Shell Sort):
1. Compute Gap = ceil((size of arr1 + size of arr2)/2) and assume both elements as single array
2. Initialize left as 0 and right = left + gap and run a loop while right < len(arr2) 
3. If left > right swap both elements (ensure swapping is done based on array positions and 
only if left element is greater than right)
4. Decrease gap = ceil(gap/2) and continue till old gap is not 1
TC -> O((n+m)*log(n+m)), SC -> O(1)
"""