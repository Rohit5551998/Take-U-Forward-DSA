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
  def __init__(self, data, next1 = None, prev1 = None): # data -> value stored in node
    self.data = data
    self.next = next1
    self.prev = prev1

class Solution:
  def convertArr2LL(self, arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
      temp.next = Node(arr[i], None, temp)
      temp = temp.next
    return head

  def deleteHead(self, head):
    if (not head or head.next is None):
      return None
    
    prev = head
    head = head.next
    head.prev = None
    prev.next = None
    return head

  def deleteTail(self, head):
    if (not head or head.next is None):
      return None
    
    temp = head
    while (temp.next is not None):
      temp = temp.next

    prev = temp.prev
    prev.next = None
    temp.prev = None

    return head
  
  def deleteAtK(self, head, k):
    if (head is None):
      return None
    
    cnt = 0
    curr = head

    while (curr != None):
      cnt += 1
      if (cnt == k): break
      curr = curr.next

    prev = curr.prev
    front = curr.next

    if (prev == None and front == None):
      return None
    elif (prev == None):
      return self.deleteHead(head)
    elif (front == None):
      return self.deleteTail(head)
    else:
      prev.next = front
      front.prev = prev
      curr.prev = None
      curr.next = None
    return head

  def deleteNode(self, node):
    prev = node.prev
    front = node.next

    if (front == None):
      prev.next = None
      node.prev = None

    prev.next = front
    front.back = prev
    node.next = None
    node.prev = None

  def printLinkedList(self, head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")  

if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().deleteHead(head)
  Solution().printLinkedList(head)
  head = Solution().deleteTail(head)
  Solution().printLinkedList(head)
  head = Solution().deleteAtK(head, 3)
  Solution().printLinkedList(head)
  Solution().deleteNode(head.next)
  Solution().printLinkedList(head)