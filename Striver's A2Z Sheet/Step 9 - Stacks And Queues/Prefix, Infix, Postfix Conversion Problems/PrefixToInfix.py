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
import sys

from queue import PriorityQueue, Queue, LifoQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
  def precedence(self, op: str) -> int:
    if (op == '^'):
      return 3
    elif (op == '*' or op == '/'):
      return 2
    elif (op == '+' or op == '-'):
      return 1
    else:
      return 0

  def findSolution(self, input: str) -> str:
    stack = LifoQueue()
    for i in range(len(input) - 1, -1, -1):
      char = input[i]
      if char.isalnum():
        stack.put(char)
      else:
        t1 = stack.get()
        t2 = stack.get()
        exp = '(' + t1 + char + t2 + ')'
        stack.put(exp)

    return stack.get()

if __name__ == "__main__":
  input = "*+PQ-MN"
  print(Solution().findSolution(input))