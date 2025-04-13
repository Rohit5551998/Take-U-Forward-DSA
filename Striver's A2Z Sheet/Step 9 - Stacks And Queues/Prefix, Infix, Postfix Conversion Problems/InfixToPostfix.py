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
    result = ""

    for char in input:
      if char.isalnum():
        result += char
      elif char == '(':
        stack.put(char)
      elif char == ')':
        while (not stack.empty() and stack.queue[-1] != '('):
          result += stack.get()
        stack.get()

      else:
        while (not stack.empty() and self.precedence(char) <= self.precedence(stack.queue[-1])):
          result += stack.get()
        stack.put(char)

    while (not stack.empty()):
      result += stack.get()
    
    return result

if __name__ == "__main__":
  input = "a+b*(c^d-e)^(f+g*h)-i"
  print(Solution().findSolution(input))