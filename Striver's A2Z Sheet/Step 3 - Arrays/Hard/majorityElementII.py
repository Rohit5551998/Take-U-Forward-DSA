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
    resp = []
    n = len(arr)//3

    for i in range(len(arr)):
      if (len(resp) == 0 or resp[0] != arr[i]):
        cnt = 1
        for j in range(i+1, len(arr)):
          if (arr[j] == arr[i]):
            cnt += 1
        if (cnt == n + 1):
          resp.append(arr[i])
      if (len(resp) == 2):
        break

    return resp
  
  def findSolution2(self, arr:List[int]):
    n = len(arr)//3
    hashMap = {}
    resp = []

    for i in range(len(arr)):
      if (arr[i] not in hashMap):
        hashMap[arr[i]] = 0
      hashMap[arr[i]] += 1

      if (hashMap[arr[i]] == n + 1):
        resp.append(arr[i])
    return resp
  
  def findSolution(self, arr:List[int]):
    cnt1, cnt2, el1, el2 = 0, 0, -math.inf, -math.inf
    resp = []
    for i in range(0, len(arr)):
      if (cnt1 == 0 and arr[i] != el2):
        el1 = arr[i]
        cnt1 += 1
      elif (cnt2 == 0 and arr[i] != el1):
        el2 = arr[i]
        cnt2 += 1
      elif (arr[i] == el1):
        cnt1 += 1
      elif (arr[i] == el2):
        cnt2 += 1
      else:
        cnt1 -= 1
        cnt2 -= 1

    cnt1, cnt2 = 0, 0
    for i in range(0, len(arr)):
      if (arr[i] == el1): cnt1 += 1
      if (arr[i] == el2): cnt2 += 1

    if (cnt1 > len(arr) // 3): resp.append(el1)
    if (cnt2 > len(arr) // 3): resp.append(el2)
    return resp

if __name__ == "__main__":
  # arr = [1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 4]
  arr = [11,33, 22, 33,11,33,11, 22]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Majority Element

Brute Force:
1. Run Two Nested Loops and Find Occurence of Each Element
2. Check if list is empty or if first is not equal to current element only then execute step 3
2. Check If it is greater than floor of n/3 and append it to final ans array. 
3. Max No of Elements is floor of (n/3) so break if this condition is met
TC -> O(n**2), SC -> O(1)

Better Approach:
1. Use HashMap to Store Occurence of Each Element
2. After storing element check if the occurence is equal to floor of (n/3)+1 and add to final output
TC -> O(n) / O(n*log(n)), SC -> O(n)

Optimal Approach (Extended Boyer Moore’s Voting Algorithm):
1. Initialize cnt1 = 0, cnt2 = 0 and el1 & el2
2. Run Through Array If cnt1 is 0 and the current element is not el2 then store the current element 
of the array as el1 along with increasing the cnt1 value by 1.
3. If cnt2 is 0 and the current element is not el1 then store the current element of the array as el2 
along with increasing the cnt2 value by 1.
4. If the current element and el1 are the same increase the cnt1 by 1.
5. If the current element and el2 are the same increase the cnt2 by 1.
6. Other than all the above cases: decrease cnt1 and cnt2 by 1.
7. The integers present in el1 & el2 should be the result we are expecting. 
So, using another loop, we will manually check their counts if they are greater than the floor(N/3).
TC -> O(2n), SC -> O(1)
"""