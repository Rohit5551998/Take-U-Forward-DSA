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
    repeated, missing = -1, -1
    for i in range(1, len(arr)+1):
      cnt = 0
      for j in range(0, len(arr)):
        if (i == arr[j]):
          cnt += 1
      if (cnt == 2): repeated = i
      if (cnt == 0): missing = i
    return repeated, missing
  
  def findSolution2(self, arr: List[int]):
    repeated, missing = -1, -1
    hashMap = [0] * (len(arr)+1)

    for i in range(0, len(arr)):
      hashMap[arr[i]] += 1

    for i in range(1, len(hashMap)):
      if (hashMap[i] == 2):
        repeated = i
      if (hashMap[i] == 0):
        missing = i

      if (repeated != -1 and missing != -1):
        break

    return repeated, missing
  
  def findSolution3(self, arr: List[int]):
    S, S2, SN, S2N = 0, 0, 0, 0
    n = len(arr)
    SN = int(n*(n+1)/2)
    S2N = int(n*(n+1)*(2*n+1)/6)

    for i in range(0, len(arr)):
      S += arr[i]
      S2 += arr[i] ** 2

    # S-Sn = X-Y:
    val1 = S - SN

    # S2-S2n = X^2-Y^2:
    val2 = S2 - S2N

    # Find X+Y = (X^2-Y^2)/(X-Y):
    val2 = val2 // val1

    # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
    # Here, X-Y = val1 and X+Y = val2:
    x = (val1 + val2) // 2
    y = x - val1

    return [x, y]
  
  def findSolution(self, arr: List[int]):
    n = len(arr)
    xor = 0

    #Step 1: Find XOR of all elements:
    for i in range(len(arr)):
      xor ^= arr[i]
      xor ^= i+1

    #Step 2: Find the differentiating bit number(rightmost bit set from 0)
    bit = (xor & ~(xor - 1))

    #Step 3: Group the numbers in 0 & 1(both array elements and numbers from 1 to n):
    zero, one = 0, 0
    for i in range(0, len(arr)):
      if (arr[i] & bit != 0):
        one ^= arr[i]
      else:
        zero ^= arr[i]

    for i in range(1, n+1):
      if (i & bit != 0):
        one ^= i
      else:
        zero ^= i

    # Last step: Identify the numbers:
    cnt = 0
    for i in range(0, len(arr)):
      if (arr[i] == zero):
        cnt += 1
    if (cnt == 2): return [zero, one]
    else: return [one, zero]


if __name__ == "__main__":
  arr = [3,1,2,5,4,6,7,5]
  resp = Solution().findSolution(arr)
  print(resp)


"""
Find Missing & Repeating Elements
#Brute Force:
1. Use Two Nested Loops to count occurence of each element from 0 to n and arr elements.
2. If count == 0 then it is missing and if count == 2 then it is repeating
TC -> O(n**2), SC -> O(1)

#Better Approach:
1. Initialize HashSet and Store Occurence of Each Element.
2. Loop throught HashSet and If count == 0 then it is missing and if count == 2 then it is repeating
TC -> O(2n), SC -> O(n)

#Optimal Solution 1 (Sum and Sum of Squares Approach):
1. First, find out the values of S and Sn and then calculate S - Sn (Using the above formulas).
2. Then, find out the values of S2 and S2n and then calculate S2 - S2n.
3. After performing steps 1 and 2, we will be having the values of X + Y and X - Y. 
Now, by substitution of values, we can easily find the values of X and Y.
TC -> O(n), SC -> O(1)

#Optimal Solution 2 (XOR with Bit Manipulation - Difficult):
Step 1: Find the XOR of the repeating number(X) and the missing number(Y)
i.e. (X^Y) = (a[0]^a[1]^.....^a[n-1]) ^ (1^2^........^N)

In order to find the XOR of the repeating number and the missing number, we will first XOR all the 
array elements and with that value, we will again XOR all the numbers from 1 to N.
(X^Y) = (a[0]^a[1]^.....^a[n-1]) ^ (1^2^3^........^N)
Step 2: Find the first different bit from right between the repeating and the missing number 
i.e. the first set bit from right in (X^Y)

By convention, the repeating and the missing number must be different and since they are 
different they must contain different bits. Now, our task is to find the first different bit from the
right i.e. the end. We know, the XOR of two different bits always results in 1. The position of the first different bit from the end will be the first set bit(from the right) in (X^Y) that we have found in step 1.
Step 3: Based on the position of the different bits we will group all the elements 
( i.e. all array elements + all elements between 1 to N) into 2 different groups

Assume an imaginary array containing all the array elements and all the elements between 1 to N. 
Now, we will check that particular position for each element of that imaginary array and 
then if the bit is 0, we will insert the element into the 1st group otherwise, we will insert it into the 2nd group. 
After performing this step, we will get two groups. Now, if we XOR all the elements of those 2 groups, 
we will get 2 numbers. One of them will be the repeating number and the other will be the missing number. But until now, we do not know which one is repeating and which one is missing.

Last step: Figure out which one of the numbers is repeating and which one is missing
We will traverse the entire given array and check which one of them appears twice. And the number that appears twice is the repeating number and the other one is the missing number.
TC -> O(n), SC -> O(1)

"""