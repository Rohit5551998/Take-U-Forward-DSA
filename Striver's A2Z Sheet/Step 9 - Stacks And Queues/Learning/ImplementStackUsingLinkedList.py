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

from queue import PriorityQueue, Queue, LifoQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter


# Node Class
class Node:
  def __init__(self, data, next1 = None): # data -> value stored in node
    self.data = data
    self.next = next1

class Solution:
  def __init__(self):
    self.top = None
    self.size = 0

  def convertArr2LL(self, arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
      temp.next = Node(arr[i], None)
      temp = temp.next
    return head

  def printLinkedList(self, head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")  

  def push(self, data):
    newNode = Node(data)
    newNode.next = self.top
    self.top = newNode
    self.size += 1
  
  def pop(self):
    if (self.top == None):
      return -1
    popped = self.top
    self.top = self.top.next
    self.size -= 1
    return popped.data
  
  def Size(self):
    return self.size
  
  def Top(self):
    if (self.top == None):
      return -1
    return self.top.data
  
  def isEmpty(self):
    return self.size == 0


if __name__ == "__main__":
  stack = Solution()
  stack.push(16)
  stack.push(15)
  stack.push(14)
  stack.push(13)
  print(stack.Size())
  print(stack.pop())
  print(stack.Size())
  print(stack.Top())
  print(stack.pop())
  print(stack.pop())
  print(stack.isEmpty())
