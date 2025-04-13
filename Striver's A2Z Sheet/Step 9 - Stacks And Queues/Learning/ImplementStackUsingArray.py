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
  def __init__(self):
    self.top = -1
    self.size = 1000
    self.arr = [0] * self.size

  def push(self, x: int):
    if (self.top + 1 <= self.size):
      self.top += 1
      self.arr[self.top] = x

  def pop(self):
    if (self.top != -1):
      element = self.arr[self.top]
      self.top -= 1
      return element
    return None
    
  def Top(self):
    if (self.top != -1):
      return self.arr[self.top]
    return None
  
  def Size(self):
    return self.top + 1

        

if __name__ == "__main__":
  stack = Solution()
  stack.push(3)
  stack.push(2)
  stack.push(5)
  stack.push(6)
  print(stack.Size())
  print(stack.pop())
  print(stack.Size())
  print(stack.Top())