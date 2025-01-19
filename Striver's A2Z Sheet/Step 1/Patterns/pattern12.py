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
    for i in range(1, n+1):
      for j in range(1, i+1):
        print(j, end=" ")

      for j in range(1, 2*(n-i)+1):
        print(" ", end=" ")

      for j in range(1, i+1):
        print(i-j+1, end=" ")
      print("")
      


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  Solution().findSolution(n)


"""
1             1 
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1

[number, space, number]
[1, 6, 1]
[2, 4, 2]
[3, 2, 3]
[4, 0, 4]
"""