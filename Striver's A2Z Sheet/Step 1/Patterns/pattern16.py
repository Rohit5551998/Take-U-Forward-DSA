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
    ch = 'A'
    chrIndex = ord(ch)
    for i in range(1, n+1):
      for j in range(1, i+1):
        print(chr(chrIndex), end=" ")
      chrIndex += 1
      print("")
      


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  Solution().findSolution(n)


"""
A 
B B
C C C
D D D D
E E E E E
"""