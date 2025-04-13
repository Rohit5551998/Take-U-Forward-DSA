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
    self.front = None
    self.rear = None
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

  def enqueue(self, data):
    newNode = Node(data)

    if newNode is None: print("Queue is full")

    if self.front is None:
      self.front = newNode
      self.rear = newNode
    else:
      self.rear.next = newNode
      self.rear = newNode

    self.size += 1
  
  def dequeue(self):
    if (self.front == None):
      return -1
    popped = self.front
    self.front = self.front.next
    self.size -= 1
    return popped.data
  
  def Size(self):
    return self.size
  
  def peek(self):
    if (self.front == None):
      return -1
    return self.front.data
  
  def isEmpty(self):
    return self.size == 0


if __name__ == "__main__":
  queue = Solution()
  queue.enqueue(16)
  queue.enqueue(15)
  queue.enqueue(14)
  queue.enqueue(13)
  print(queue.Size())
  print(queue.dequeue())
  print(queue.Size())
  print(queue.peek())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.dequeue())
  print(queue.isEmpty())
