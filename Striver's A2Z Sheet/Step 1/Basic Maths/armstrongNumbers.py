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
  def findSolution(self, n: int):
    originalNumber = n;
    sum = 0

    while (n > 0):
      lastDigit = n % 10
      sum += lastDigit**3
      n = int(n / 10)

    return sum == originalNumber

if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  print(Solution().findSolution(n))


"""
You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 

Note: Return true if it is an Armstrong number else return false.
"""