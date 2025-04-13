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

from queue import PriorityQueue, Queue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
  def __init__(self):
    self.queue = Queue()

  def push(self, x: int):
    s = self.queue.qsize()
    self.queue.put(x)
    for i in range(s):
      self.queue.put(self.queue.get())

  def pop(self):
    return self.queue.get()
    
  def Top(self):
    return self.queue.queue[0]
  
  def Size(self):
    return self.queue.qsize()

        

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