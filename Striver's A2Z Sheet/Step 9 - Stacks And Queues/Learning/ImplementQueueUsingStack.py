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
import sys

from queue import PriorityQueue, Queue, LifoQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
  def __init__(self):
    self.input = LifoQueue()
    self.output = LifoQueue()

  def push(self, x: int):
    while (not self.input.empty()):
      self.output.put(self.input.get())

    print("The element pushed is", x)
    self.input.put(x)

    while (not self.output.empty()):
      self.input.put(self.output.get())

  def pop(self):
    if self.input.qsize() == 0:
      print("Stack is empty")
      sys.exit(0)
    val = self.input.get()
    return val
    
  def Top(self):
    if self.input.qsize() == 0:
      print("Stack is empty")
      sys.exit(0)
    return self.input.queue[-1]
  
  def Size(self):
    return self.input.qsize()

if __name__ == "__main__":
  Queue1 = Solution()
  Queue1.push(3)
  Queue1.push(2)
  Queue1.push(5)
  Queue1.push(6)
  print(Queue1.Size())
  print(Queue1.pop())
  print(Queue1.Size())
  print(Queue1.Top())