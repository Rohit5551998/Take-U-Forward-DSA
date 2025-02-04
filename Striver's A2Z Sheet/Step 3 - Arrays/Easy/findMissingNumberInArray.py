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
    n = len(arr)
    for i in range(0, n + 1):
      flag = -1
      for j in range(0, len(arr)):
        if arr[j] == i:
          flag = 1
          break
      if flag == -1:
        return i
      
  def findSolution2(self, arr:List[int]):
    hashArray = [0] * (len(arr) + 1)

    for i in range(len(arr)):
      hashArray[arr[i]] += 1
    
    for i in range(len(hashArray)):
      if (hashArray[i] == 0):
        return i

  def findSolution3(self, arr:List[int]):
    n = len(arr)
    sum = (n)*(n+1)//2

    for i in range(n):
      sum -= arr[i]

    return sum

  def findSolution(self, arr:List[int]):
    xor1 = 0
    xor2 = 0
    for i in range(len(arr)):
      xor1 ^= i        # XOR of all elements from 0 to n-1
      xor2 ^= arr[i]   # XOR of all elements in the array
    xor1 ^= len(arr)   # XOR of all elements from 0 to n from first step
    return xor1 ^ xor2

if __name__ == "__main__":
  arr = [3, 1, 0, 2]
  arr = [0, 1]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Missing Number In Array

Brute Force Approach:
Loop Through Length of Array and check if i is present in the array or not. If not present then return i.
Time Complexity: O(n^2), Space Complexity: O(1)

Better Approach:
Use Hash Array or Map to Store Array Elements as visited
Loop through the array and mark the elements as visited in the hash array
Loop through the hash array and check if any element is not visited then return that element
Time Complexity: O(2n), Space Complexity: O(n)

Optimal Approach 1:
Use Sum of n natural numbers formula to calculate the sum of n natural numbers
sum = n*(n+1)/2
subtract all array elements to get the missing number and return it.
Time Complexity: O(n), Space Complexity: O(1)
Might be slow for extemenly large numbers or array

Optimal Approach 2:
Use XOR operation to find the missing number
Note: XOR of same number is 0
XOR of all elements in the array and XOR of all elements from 0 to n
XOR of both the results will give the missing number
"""