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

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
  def __init__(self):
    self.start = -1
    self.end = -1
    self.currSize = 0
    self.maxSize = 16
    self.arr = [0] * self.maxSize

  def push(self, x: int):
    if (self.currSize == self.maxSize):
      print("Queue is full\nExiting...")
      sys.exit(1)

    if (self.end == -1):
      self.start = 0
      self.end = 0
    else:
      self.end = (self.end + 1) % self.maxSize
    self.currSize += 1
    print("The element pushed is", x)
    self.arr[self.end] = x

  def pop(self):
    if (self.start == -1):
      print("Queue Empty\nExiting...")
      sys.exit(1)
    popped = self.arr[self.start]
    if (self.currSize == 1):
      self.start = -1
      self.end = -1
    else:
      self.start = (self.start + 1) % self.maxSize
    self.currSize -= 1
    return popped
    
  def Top(self) -> int:
    if self.start == -1:
        print("Queue is Empty")
        sys.exit(1)
    return self.arr[self.start]
  
  def Size(self):
    return self.currSize
        

if __name__ == "__main__":
  Queue = Solution()
  Queue.push(3)
  Queue.push(2)
  Queue.push(5)
  Queue.push(6)
  print(Queue.Size())
  print(Queue.pop())
  print(Queue.Size())
  print(Queue.Top())