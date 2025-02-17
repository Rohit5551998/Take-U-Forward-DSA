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
        sum = 0
        for k in range(i, j+1):
          sum += arr[k]
        if (sum == n):
          cnt += 1
    return cnt
  
  def findSolution2(self, arr: List[int], k: int):
    cnt = 0
    for i in range(0, len(arr)):
      sum = 0
      for j in range(i, len(arr)):
        sum += arr[j]
        if (sum == k):
          cnt += 1
    return cnt

  def findSolution(self, arr: List[int], k: int):
    cnt = 0
    prefixSum = defaultdict(int)
    prefixSum[0] = 1  #Required If any element is k itself and the cnt should be incremented by 1
    preSum = 0

    for i in range(0, len(arr)):
      preSum += arr[i]           #Add Currenet Element to Temp PreSum
      remove = preSum - k        #Check If we previously stored preSum - k 
      cnt += prefixSum[remove]   #If Done That Means we have Subarray which match K
      prefixSum[preSum] += 1     #Increment the count of new preSum calculated by 1

    return cnt

  
if __name__ == "__main__":
  arr = [3, 1, 2, 4, -3, 3, 6, -6, 1, 1, 1, -3]
  k = 3
  # arr = [3, 1, 2, 4]
  # k = 6
  resp = Solution().findSolution(arr, k)
  print(resp)


"""
Count Subarray Sum Equal to K
#Brute Force:
1. Run two nested loops to select elements for sum of subarray.
2. Initialize third nested loop to calculate sum of each subarray
3. If it is equal to k increment count
TC -> O(n**3), SC -> O(1)

#Better Approach:
1. Run two nested loops to select elements for sum of subarray.
2. Initialize sum in outer loop and keep adding current element in inner loop
3. Check if this sum is equal to k and increment count
TC -> O(n**2), SC -> O(1)

#Optimal Solution (Prefix Sum Approach):
1. Initialize prefixSumHash with Default Value of ) with prefixSumHash[0] = 1 
(Required If any element is k itself and the cnt should be incremented by 1) & prefixSum = 0
2. Loop through the array by adding element to prefix sum
3. Check if x = prefixSum - k is present in prefixSumHash which means the subarray sum uptill that element 
can be encountered it's values times in the array
4. Store the current calculated prefixSum in prefixSumHash by incrementing it's count by 1
TC -> O(n*log(n)) / O(n) Depending on Map Used, SC -> O(n)
"""