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
  def findSolution1(self, n:int): #Brute Force
    response = True
    for i in range(2, n):
      if n%i == 0:
        response = False
        break
    return response

  def findSolution(self, n:int): #Optimized Sqrt Method
    """
    Prime Numbers can be found by iterating from 2 to sqrt(n) and checking if n%i == 0
    """
    response = True
    if (n <= 1):
      response = False
    else:
      for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
          response = False
          break
    return response

if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  print(Solution().findSolution(n))


"""
Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. The function inputs two integers a and b and returns a list containing their LCM and GCD.
"""