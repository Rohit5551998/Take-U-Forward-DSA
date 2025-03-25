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


# Node Class
class Node:
  def __init__(self, data): # data -> value stored in node
    self.data = data
    self.next = None

class Solution:

  def convertArr2LL(self, arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
      temp.next = Node(arr[i])
      temp = temp.next
    return head
  
  def insertAtHeader(self, head, x):
    temp = Node(x)
    temp.next = head
    return temp
  
  def insertAtTail(self, head, x):
    if (head == None):
      return Node(x)
    
    temp = head
    while (temp.next is not None):
      temp = temp.next

    temp.next = Node(x)
    return head

  def insertAtK(self, head, x, k):
    if (head == None):
      if (k == 1):
        return Node(x)
      else:
        return head
      
    if (k == 1):
      temp = Node(x)
      temp.next = head
      return temp
    
    cnt = 0
    temp = head
    while (temp.next is not None):
      cnt += 1
    
      if (cnt == k-1):
        node = Node(x)
        node.next = temp.next
        temp.next = node
        break
      temp = temp.next

    return head

  def insertBeforeValue(self, head, x, val):
    if (head == None):
        return head
      
    if (head.data == val):
      temp = Node(x)
      temp.next = head
      return temp
    
    temp = head
    while (temp.next is not None):
      if (temp.next.data == val):
        node = Node(x)
        node.next = temp.next
        temp.next = node
        break
      temp = temp.next

    return head
  
  def printLinkedList(self, head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  head = Solution().insertBeforeValue(head, 10, 7)
  Solution().printLinkedList(head)