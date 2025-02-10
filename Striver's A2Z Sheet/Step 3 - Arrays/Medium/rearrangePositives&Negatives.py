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
    positive, negative = [], []

    for i in range(0, len(arr)):
      if (arr[i] > 0):
        positive.append(arr[i])
      else:
        negative.append(arr[i])

    for i in range(0, (int)(len(arr)//2)):
      arr[2*i] = positive[i]
      arr[2*i+1] = negative[i]

    return arr
  
  def findSolution2(self, arr:List[int]):
    final = [0] * len(arr)
    positive, negative = 0, 1
    for i in range(0, len(arr)):
      if (arr[i] > 0):
        final[positive] = arr[i]
        positive += 2
      else:
        final[negative] = arr[i]
        negative += 2
    return final
    
  def findSolution(self, arr: List[int]):
    positive, negative = [], []

    for i in range(0, len(arr)):
      if (arr[i] > 0):
        positive.append(arr[i])
      else:
        negative.append(arr[i])

    for i in range(0, min(len(positive), len(negative))):
      arr[2*i] = positive[i]
      arr[2*i+1]= negative[i]

    # if (len(positive) > len(negative)):
    #   for i in range(len(negative), len(positive)):
    #     arr.append(positive[i])
    # elif (len(negative) > len(positive)):
    #   for i in range(len(positive), len(negative)):
    #     arr.append(negative[i])
    return arr

if __name__ == "__main__":
  arr = [3,1,-2,-5,2,-4]
  arr = [3,1,-2,-5,2,-4, -100, 10, 15]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Reaarange Positives & Negatives:

Brute Force(For Equal Positives & Negatives), Optimal for (Positives != Negatives):
1. Initialize Two Arrays For Positive & Negative Elements Respectively
2. Loop Through Array and add elements in respective positions
3. Run another loop either to n/2 or min of (positive & negative) depending on variant
4. Replace elements in primary array with positives at 2*i and negatives at 2*i+1
5. If Unequal number of elements are present run the loop through remaining elements of greater size array to replace
elements in original array
TC -> O(n + n/2) / O(2n), SC -> O(n)

Optimal Approach (Only For Equal Positives & Negatives):
1. Initialize Two Pointers in New Array holding next positive and negative elements positions
2. Loop through original array and depending on positive & negative element add to new array and increment pointer
3. Run till all elements in old array are exhausted
TC -> O(n), SC -> O(n)
"""