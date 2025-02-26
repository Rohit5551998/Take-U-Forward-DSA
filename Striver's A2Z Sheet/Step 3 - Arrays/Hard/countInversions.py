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
  def findSolution1(self, arr: List[int]):
    cnt = 0
    for i in range(0, len(arr)):
      for j in range(i+1, len(arr)):
        if (arr[i] > arr[j]):
          cnt += 1
    return cnt


  def merge(self, arr: List[int], low: int, mid: int, high: int):
    left, right = low, mid+1
    cnt = 0
    temp = []
    while (left <= mid and right <= high):
      if (arr[left] <= arr[right]):
        temp.append(arr[left])
        left += 1
      else:
        cnt += (mid - left + 1)                 #Increase By Count of All Remaining Elements on Left Side
        temp.append(arr[right])
        right += 1

    while (left <= mid):
      temp.append(arr[left])
      left += 1
    
    while (right <= high):
      temp.append(arr[right])
      right += 1

    for i in range(low, high+1):
      arr[i] = temp[i-low]

    return cnt

  def mergeSort(self, arr: List[int], low: int, high: int):
    cnt = 0
    if (low < high):
      mid = (low + high) // 2
      cnt += self.mergeSort(arr, low, mid)
      cnt += self.mergeSort(arr, mid + 1, high)
      cnt += self.merge(arr, low, mid, high)
    return cnt


  def findSolution(self, arr: List[int]):
    return self.mergeSort(arr, 0, len(arr) - 1)

  
if __name__ == "__main__":
  arr = [5,3,2,1,4]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Count Inversions
#Brute Force:
1. Initialize two nested loops to traverse the given array of intervals.
2. Check for each pair if the condition is satisfied for A[i] > A[j] and add to count
3. Return Final Count
Tc -> O(N**2), SC -> O(1)

#Optimal Solution:
1. Use Modified Merge Sort Algorithm to Count the Number of Inversions If A[i] > A[j]
2. Increase Count By All Right Elements of Left Subarray If condition is met ie (mid - left + 1)
3. The count needs to be returned from merging algorithm and the count of left and right subarrays
4. Return the final count
TC -> O(n*log(n)), SC -> O(n)
"""