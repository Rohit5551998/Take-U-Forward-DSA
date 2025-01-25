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
  def findSolution(self, n:int):
        dividend = n
        i = 0
        while (n > 0):
            lastDigit = n%10
            if (lastDigit != 0 and dividend % lastDigit == 0):
                i += 1
            
            n = int(n/10)
            
        return i  

  def countDigits1(self, n:int): #O(log10(n) + 1)
        i = 0
        while (n > 0):
            i += 1
            n = int(n/10)
        return i  

  def countDigits2(self, n:int): #O(log10(n) + 1)
        i = math.log(n, 10) + 1
        return i  

if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  print(Solution().findSolution(n))


"""
Given a positive integer n, count the number of digits in n that divide n evenly (i.e., without leaving a remainder). Return the total number of such digits.

A digit d of n divides n evenly if the remainder when n is divided by d is 0 (n % d == 0).
Digits of n should be checked individually. If a digit is 0, it should be ignored because division by 0 is undefined.
"""