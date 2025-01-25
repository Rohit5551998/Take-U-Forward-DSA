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

  def printNos(self, i:int, n: int):
    if (i > n):
      return
    else:
      print(i, end=" ")
      self.printNos(i+1, n)

  def findSolution(self, n:int): 
    i = 1
    self.printNos(i, n)


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  Solution().findSolution(n)


"""
"""