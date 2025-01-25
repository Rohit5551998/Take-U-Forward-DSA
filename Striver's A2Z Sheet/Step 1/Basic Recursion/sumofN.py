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

  def sumofNumbers(self, n: int) -> int:
    if (n > 0):
      return n + self.sumofNumbers(n-1)
    else:
      return 0
    
  def formulaSumofNumbers(self, n: int) -> int:
    return (int)(n*(n+1)/2)

  def findSolution(self, n:int): 
    print(self.sumofNumbers(n))
    print(self.formulaSumofNumbers(n))


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  Solution().findSolution(n)


"""
Given a number ‘N’, find out the sum of the first N natural numbers.
"""