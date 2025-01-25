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
  def findSolution1(self, a:int, b: int): #Brute Force
    gcd = 1
    for i in range(min(a, b), 1, -1):
      if (a%i == 0 and b%i == 0):
        gcd = i;
        break;
    lcm = (int)((a * b)/gcd);
    return [lcm, gcd]
  
  def findSolution(self, a:int, b: int): #Optimized Eucldian Algorithm for GCD and LCM
    """
    assuming a > b
    GCD(a, b) = GCD(b, a%b)
    LCM(a, b) = (a*b)/GCD(a, b)
    """
    originalNumbers = [a, b];
    while (a > 0 and b > 0):
      if a > b:
        a = a % b
      else:
        b = b % a

    gcd = max(a, b)
    lcm = (int)((originalNumbers[0]*originalNumbers[1])/gcd)
    return [lcm, gcd]

if __name__ == "__main__":
  a = int(input("Please enter a number: \n"))
  b = int(input("Please enter a number: \n"))
  print(Solution().findSolution(a, b))


"""
Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. The function inputs two integers a and b and returns a list containing their LCM and GCD.
"""