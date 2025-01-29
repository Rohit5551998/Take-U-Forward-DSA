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

  def merge(self, arr:List[int], low: int, mid: int, high: int):
    temp = []
    left = low
    right = mid+1
    while (left <= mid and right <= high):
      if (arr[left] <= arr[right]):
        temp.append(arr[left])
        left += 1
      else: 
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

  def mergeSort(self, arr:List[int], low: int, high: int): 
    if (low < high):
      mid = (int)((low + high) / 2)
      self.mergeSort(arr, low, mid)
      self.mergeSort(arr, mid+1, high)
      self.merge(arr, low, mid, high)

if __name__ == "__main__":
  arr = [5, 4, 10, 3, 1, 6, 17, 2]
  n = len(arr)
  Solution().mergeSort(arr, 0, n-1)
  print(arr)


"""
Split Array my Middle Element untilt low < high
Then start merging array by putting elements in temp array by comparing smallest element using left & right pointers
Continue till both arrays are exhausted then resassign values in old array
TC: O(n*log(n)) SC: O(n)
"""