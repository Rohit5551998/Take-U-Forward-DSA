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
      for j in range(1, i):
        print("  ", end="")

      for j in range(1, 2*(n-i+1)):
        print("* ", end="")

      for j in range(1, i):
        print("  ", end="")
      print("")


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  Solution().findSolution(n)


"""
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *  

[0, 9, 0]
[1, 7, 1]
[2, 5, 2]
[3, 3, 3]
[4, 1, 4]

Space  ,  Stars, Space
(i-1), (2*(n-i)+1),  (i-1)
"""