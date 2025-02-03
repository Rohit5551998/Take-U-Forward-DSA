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
    s = set()

    for i in range(len(arr1)):
      s.add(arr1[i])

    for i in range(len(arr2)):
      s.add(arr2[i])
     
    return sorted(list(s))
  
  def findSolution(self, arr1:List[int], arr2: List[int]):
    i, j = 0, 0
    union = []
    while (i < len(arr1) and j < len(arr2)):
      if (arr1[i] <= arr2[j]):
        if (len(union) == 0 or union[-1] != arr1[i]):
          union.append(arr1[i])
        i += 1

      else: 
        if (len(union) == 0 or union[-1] != arr2[j]):
          union.append(arr2[j])
        j += 1

    while (i < len(arr1)):
      if (union[-1] != arr1[i]):
        union.append(arr1[i])
      i += 1

    while (j < len(arr2)):
      if (union[-1] != arr2[j]):
        union.append(arr2[j])
      j += 1 
      
    return union

if __name__ == "__main__":
  arr1 = [1, 2, 3, 4, 5, 6]
  arr2 = [1, 7, 10, 15, 19]
  resp = Solution().findSolution(arr1, arr2)
  print(resp)


"""
Union of Sorted Arrays
Brute Force
Set or Map Based Approach -> Ordered Algos or Sort unordered ones

TC -> O((m+n)*log(m+n))  SC-> O(m+n) Union Array or O(1) Otherwise

Optimal Approach
Two Pointer Approach

Initialize Two Pointers With A While Loop Until Both are less than respective array lengths
if Arr1[i] <= Arr2[j] and if it is not in union' last position add it to union and increment i irrespective of addition
Else Check the same for j and increment irrespective of addition

Once Done Run Two More Loops till end of respective arrays and add to union if required by checking last element

TC -> O(m+n) SC-> O(m+n) Union Array or O(1) Otherwise

"""