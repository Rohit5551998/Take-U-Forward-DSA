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
      ch = 'A'
      chrIndex = ord(ch) - 1
      for j in range(1, n-i+1):
        print(" ", end=" ")

      for j in range(1, 2*i):
        if (j<=i):
          chrIndex += 1
        else:
          chrIndex -= 1
        print(chr(chrIndex), end=" ")

      for j in range(1, n-i+1):
        print(" ", end=" ")  
      print("")
      


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  Solution().findSolution(n)


"""
        A
      A B A
    A B C B A
  A B C D C B A
A B C D E D C B A
"""