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
  def findSolution1(self, arr: List[int], k:int):
    for i in range(0, len(arr)):
      if (arr[i] <= k):
        k += 1
      else:
        return k
    return -1

  def findSolution(self, arr: List[int], k:int):
    low, high = 0, len(arr) - 1
    while (low <= high):
      mid = low + (high - low) // 2
      missing = (arr[mid] - (mid + 1))
      if (missing < k): 
        low = mid + 1
      else:
        high = mid - 1
    return low + k # low + k and high + 1 + k will point to same answer


if __name__ == "__main__":
  arr = [4,7,9,10]
  k = 4
  resp = Solution().findSolution(arr, k)
  print(resp)


"""
Kth Missing Positive Number
Brute Force
1. Inside the loop, If vec[i] <= k: we will simply increase the value of k by 1.
2. Otherwise, we will break out of the loop. Finally, we will return the value of k.
3. Note: The main idea is to shift k by 1 step if the current element is smaller or equal to k. 
And whenever we get a number > k, we can conclude that k is the missing number.
TC -> O(n), SC -> O(1)

Optimal Approach
1. Initialize two pointers low = 1, high = len(arr) - 1
2. In loop calculate mid = low + (high - low) // 2
3. Missing Numbers Can Be Calculated Using arr[mid] - (mid + 1) for pointer at mid
4. If mid is less than k set low = mid + 1 else high = mid - 1
5. Return either low + 1 or high + 1 + k

Explanation for Formula
So, in the given array, the preceding neighbor of the kth missing number is vec[high]. 
Now, we know, up to index ‘high’, the number of missing numbers = vec[high] - (high+1).
But we want to go further and find the kth number. To extend our objective, we aim to find the kth number in the sequence.
In order to determine the number of additional missing values required to reach the kth position, we can calculate this as
more_missing_numbers = k - (vec[high] - (high+1)).
Now, we will simply add more_missing_numbers to the preceding neighbor i.e. vec[high] to get the kth missing number.
kth missing number = vec[high] + k - (vec[high] - (high+1))
        =  vec[high] + k - vec[high] + high + 1
        = k + high + 1.
        = k + low (low = high + 1 at final position since crossover is performed) 
TC -> O(log(n)), SC -> O(1)
"""