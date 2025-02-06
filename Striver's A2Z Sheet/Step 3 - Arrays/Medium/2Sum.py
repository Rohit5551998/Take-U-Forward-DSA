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

  def findSolution1(self, arr:List[int], k: int):
    for i in range(len(arr)):
      for j in range(len(arr)):
        if (i != j and arr[i] + arr[j] == k):
          return [i, j]

  def findSolution2(self, arr:List[int], k: int):
    hashMap = {}

    for i in range(len(arr)):
      if ((k - arr[i]) in hashMap):
        return [hashMap[(k-arr[i])], i]
      
      hashMap[arr[i]] = i

  def findSolution(self, arr:List[int], k: int):
    copy = sorted(arr)
    left, right = 0, len(arr) - 1
    temp, ans = [], []
    while(left < right):
        sum = copy[left] + copy[right]
        if (sum < k):
            left += 1

        elif (sum > k):
            right -= 1 

        else:
            temp = [copy[left], copy[right]]
            break
    if (len(temp) == 2):
        for i in range(len(arr)):
            if (arr[i] == temp[0] or arr[i] == temp[1]):
                ans.append(i)
        return ans
    return [-1, -1]

if __name__ == "__main__":
  arr = [1, 2, 7, 11, 15]
  arr = [3, 2, 4]
  resp = Solution().findSolution(arr, 6)
  print(resp)


"""
2 Sum

Brute Force:
Run Two Nested Loops To Check If Elements are different and Sum Is Equal to K Return The Indexes
TC -> O(n**2), SC -> O(1)

Better:
Use Hash Map to Store Element Along With Index
Check If k-x(current Element) is present in HashMap
If Exists Then Return Index of Current ELement & Stored k-x
TC -> O(n*log(n)) or O(n) depending on hashmap, SC -> O(n)

Optimal (Two Pointer Approach):
Sort The Array
Take Two Pointers Left & Right at Start & End
If Sum is Less Than K Move Left Pointer 
If Sum is Greater Than K Move Right Pointer
If Sum is Equal to K Return Indexes
TC -> O(n*log(n)) + O(n) / O(n*log(n)) + O(2*n), SC -> O(1) / O(n)
"""