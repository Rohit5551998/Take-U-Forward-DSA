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
  def findSolution1(self, arr:List[int]):
    for i in range(len(arr)):
      cnt = 0
      for j in range(len(arr)):
        if arr[j] == arr[i]:
          cnt += 1
      if cnt == 1:
        return arr[i]
      
  def findSolution2(self, arr:List[int]):
    map = defaultdict(int)
    for i in range(len(arr)):
      map[arr[i]] += 1
    
    for k, v in map.items():
      if v == 1:
        return k

  def findSolution(self, arr:List[int]):
    xor = 0
    for i in range(len(arr)):
      xor ^= arr[i]
    return xor

if __name__ == "__main__":
  arr = [1, 4, 2, 1, 4]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Number That Appears Once

Brute Force Approach:
Loop Through Length of Array and run another nested loop on array elements to check if i is present 
in the array twice. If not present then return i.
Time Complexity: O(n^2), Space Complexity: O(1)

Better Approach:
Use Hash Array or Map to Store Count of elements in the array
Loop through the array and update the count of elements in the hash map
Loop through the hash map and check if any element is not present twice then return that element
Time Complexity: O(n*log(m)) + O(m), Space Complexity: O(m), where m is the number of unique elements in the array
Considering UnOrdered Map, Time Complexity: O(n) + O(m), Space Complexity: O(n)

Optimal Approach:
Use XOR operation on all array elements to find the missing number and return it
Time Complexity: O(n), Space Complexity: O(1)
"""