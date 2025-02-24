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
  def findSolution1(self, arr: List[int]):
    arr.sort()
    resp = []
    for i in range(0, len(arr)):
      start, end = arr[i][0], arr[i][1]

      #Skip Merged Intervals
      if (resp and end <= resp[-1][1]): 
        continue

      #Check the rest of the Intervals
      else:
        for j in range(i+1, len(arr)):
          if (arr[j][0] <= end):
            end = max(end, arr[j][1])
          else:
            break
        resp.append([start, end])

    return resp



  def findSolution(self, arr: List[int]):
    resp = []
    arr.sort()

    for i in range(0, len(arr)):
      if (not(resp) or arr[i][0] > resp[-1][1]):
        resp.append(arr[i])
      else:
        resp[-1][1] = max(resp[-1][1], arr[i][1])
    return resp

  
if __name__ == "__main__":
  arr = [[1,3],[2,6],[8,10],[15,18], [18, 20]]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Merge Overlapping SubIntervals
#Brute Force:
1. Initialize a loop to traverse the given array of intervals.
2. Take start and end as the interval's start and end
3. If resp is non empty and end of current interval lies in resp's last elements end then simply skip current interval
4. Else initialize new loop from next element and check if inner loops interval start is less than end of 
current interval then update end of current interval
5. Else break the inner loop and append the current interval to resp
Tc -> O(N*logN) + O(2*N), SC -> O(N)

#Optimal Solution:
1. Run a loop to traverse the given array of intervals
2. If resp is empty or start of current interval is greater than end of last interval in resp then append 
current interval to resp
3. Else update the end of resp's last interval as max of resp's last interval end and end of current interval
TC -> O(n*log(n)) + O(n), SC -> O(n)
"""