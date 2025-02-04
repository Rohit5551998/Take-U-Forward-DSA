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
  def findSolution1(self, arr1:List[int], arr2: List[int]):
    visited = [0] * len(arr2)
    intersection = []

    for i in range(len(arr1)):
      for j in range(len(arr2)):
        if (arr1[i] == arr2[j] and visited[j] == 0):
          intersection.append(arr1[i])
          visited[j] = 1
    return intersection

  
  def findSolution(self, arr1:List[int], arr2: List[int]):
    i, j = 0, 0
    intersection = []
    while (i < len(arr1) and j < len(arr2)):
      if (arr1[i] < arr2[j]):
        i += 1

      elif (arr1[i] > arr2[j]): 
        j += 1
      
      else:
        #With Duplicates
        intersection.append(arr1[i])

        #Without Duplicates
        #if (len(intersection) == 0 or intersection[-1] != arr1[i]):
        #  intersection.append(arr1[i])
        i += 1
        j += 1

    return intersection

if __name__ == "__main__":
  arr1 = [1, 2, 3, 3, 4, 5, 6]
  arr2 = [1, 3, 3, 6, 7, 10, 15, 19]
  resp = Solution().findSolution(arr1, arr2)
  print(resp)


"""
Intersection of Sorted Arrays
Brute Force
Use A Visited Array With Nested For Loops to Determine Whether to Add to Intersection Set

TC -> O((m+n)*(m+n))  SC-> O(m) Visited Array

Optimal Approach
Two Pointer Approach
Initialize Two Pointers With A While Loop Until Both are less than respective array lengths
If I < J increment I
Else if I > J increment J
Else Add to Intersection and increment both

TC -> O(m+n) SC-> O(m+n) Intersection of Two Elements

"""