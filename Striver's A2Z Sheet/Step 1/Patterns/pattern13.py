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
    x = 0
    for i in range(1, n+1):
      for j in range(1, i+1):
        x += 1
        print(x, end=" ")
      print("")
      


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  Solution().findSolution(n)


"""
1 
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""