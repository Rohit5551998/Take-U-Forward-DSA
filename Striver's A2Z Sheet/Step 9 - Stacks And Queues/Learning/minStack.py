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

class Solution1:
  def __init__(self):
    self.stack = LifoQueue()

  def push(self, x):
    mini = x
    if (not self.stack.empty()):
      mini = min(self.stack.queue[-1]["second"], x)
    self.stack.put({"first": x, "second": mini})

  def pop(self):
    return self.stack.get()["first"]

  def Top(self):
    return self.stack.queue[-1]["first"]

  def getMin(self):
    return self.stack.queue[-1]["second"]

class Solution:
  def __init__(self):
    self.stack = LifoQueue()
    self.mini = math.inf

  def push(self, x):
    if (self.stack.empty()):
      self.mini = x
      self.stack.put(x)
    else:
      if (x < self.mini):
        self.stack.put(2*x - self.mini)
        self.mini = x
      else:
        self.stack.put(x)

  def pop(self):
    if (self.stack.empty()): return -1
    ele = self.stack.get()

    if (ele < self.mini):
      val = self.mini
      self.mini = 2 * self.mini - ele
      return val
    return ele
  
  def Top(self):
    if (self.stack.empty()): return -1

    ele = self.stack.queue[-1]
    if (ele < self.mini): return self.mini
    return ele
    
  def getMin(self):
    return self.mini


if __name__ == "__main__":
  stack = Solution()
  stack.push(16)
  stack.push(13)
  stack.push(15)
  stack.push(14)
  print(stack.getMin())
  print(stack.pop())
  print(stack.Top())
  print(stack.getMin())
  print(stack.pop())
  print(stack.pop())
  print(stack.getMin())
