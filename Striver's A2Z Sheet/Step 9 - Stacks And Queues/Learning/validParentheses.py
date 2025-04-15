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
  def findSolution(self, input: str) -> str:
    stack = LifoQueue()
    resp = False
    for char in input:
      if (char == '(' or char == '[' or char == '{'):
        stack.put(char)
      else:
        if (stack.empty()): return False
        top = stack.get()
        if ((top == '(' and char == ')') or (top == '[' and char == ']') or (top == '{' and char == '}')): continue
        else: 
          return False

    if (stack.empty()): resp = True

    return resp

if __name__ == "__main__":
  input = "()[{}()]"
  print(Solution().findSolution(input))