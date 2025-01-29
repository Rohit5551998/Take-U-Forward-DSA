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

  def partitionArray(self, arr: List[int], low: int, high: int):
    i, j = low, high
    pivot = low

    while(i < j):
      while (arr[pivot] >= arr[i] and i < high):
        i += 1

      while (arr[pivot] < arr[j] and j > 0):
        j -= 1

      if (i < j):
        arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[pivot] = arr[pivot], arr[j]
    return j

  def quickSort(self, arr:List[int], low: int, high: int): 
    if (low < high):
      partition = self.partitionArray(arr, low, high)
      self.quickSort(arr, low, partition-1)
      self.quickSort(arr, partition+1, high)
    

if __name__ == "__main__":
  arr = [5, 4, 10, 3, 1, 6, 17, 2]
  n = len(arr)
  Solution().quickSort(arr, 0, len(arr)-1)
  print(arr)


"""
Select a pivot element any strategy works
Create Parititon by splitting all small elements to left and large elements to right of pivot
Once done replace pivot with final right pointer once crossover of left and right takes place and return new pivot position
Continue Sorting for either sides of partition

Worst Case Scenarion: Max or Min Element as Pivot TC: O(n**2)
TC: O(n*log(n)) SC: O(1) + O(n) Recursive Stack Space
"""