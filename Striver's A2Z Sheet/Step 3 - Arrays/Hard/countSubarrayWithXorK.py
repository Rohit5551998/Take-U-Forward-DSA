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
  def findSolution1(self, arr: List[int], n: int):
    cnt = 0
    for i in range(0, len(arr)):
      for j in range(i, len(arr)):
        xor = 0
        for k in range(i, j+1):
          xor ^= arr[k]
        if (xor == n):
          cnt += 1
    return cnt
  
  def findSolution2(self, arr: List[int], k: int):
    cnt = 0
    for i in range(0, len(arr)):
      xor = 0
      for j in range(i, len(arr)):
        xor ^= arr[j]
        if (xor == k):
          cnt += 1
    return cnt

  def findSolution(self, arr: List[int], k: int):
    cnt = 0
    prefixXorHash = defaultdict(int)
    prefixXorHash[0] = 1
    prefixXor = 0

    for i in range(0, len(arr)):
      prefixXor ^= arr[i]
      remove = prefixXor ^ k
      if (remove in prefixXorHash):
        cnt += prefixXorHash[remove]
      prefixXorHash[prefixXor] += 1

    return cnt

  
if __name__ == "__main__":
  arr = [4, 2, 2, 6, 4]
  k = 6
  # arr = [3, 1, 2, 4]
  # k = 6
  resp = Solution().findSolution(arr, k)
  print(resp)


"""
Count Subarray Xor Equal to K
#Brute Force:
1. Run two nested loops to select elements for xor of subarray.
2. Initialize third nested loop to calculate xor of each subarray
3. If it is equal to k increment count
TC -> O(n**3), SC -> O(1)

#Better Approach:
1. Run two nested loops to select elements for xor of subarray.
2. Initialize xor in outer loop and keep adding current element in inner loop
3. Check if this xor is equal to k and increment count
TC -> O(n**2), SC -> O(1)

#Optimal Solution (Prefix Xor Approach):
1. Initialize prefixXorHash with Default Value of ) with prefixXorHash[0] = 1 
(Required If any element is k itself and the cnt should be incremented by 1) & prefixXor = 0
2. Loop through the array by adding element to prefix xor
3. Check if x = prefixXor ^ k is present in prefixXorHash which means the subarray xor uptill that element 
can be encountered it's values times in the array
4. Store the current calculated prefixXor in prefixXorHash by incrementing it's count by 1
TC -> O(n*log(n)) / O(n) Depending on Map Used, SC -> O(n)
"""