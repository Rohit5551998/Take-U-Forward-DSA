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

  def insertAtHead(self, head, x):
    temp = Node(x, head, None)
    head.prev = temp
    return temp

  def insertBeforeTail(self, head, x):
    if (head.next == None): 
      return self.insertAtHead(head, x)
    
    temp = head
    while (temp.next != None):
      temp = temp.next

    node = Node(x, temp, temp.prev)
    temp.prev.next = node
    temp.prev = node

    return head

  def insertAtK(self, head, x, k):
    if (not head):
      if (k == 1):
        return Node(x)
      else: 
        return head
    
    if (k == 1):
      return self.insertAtHead(head, x)
    
    cnt = 0
    temp = head
    while (temp.next is not None):
      cnt += 1

      if (cnt == k-1):
        node = Node(x, temp.next, temp)
        temp.next.prev = node
        temp.next = node
        break

      temp = temp.next
    return head
  
  def insertAtNode(self, node, val):
    prev = node.prev
    newNode = Node(val, node, prev)
    prev.next = newNode
    node.prev = newNode

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
  head = Solution().insertAtHead(head, 10)
  Solution().printLinkedList(head)
  head = Solution().insertBeforeTail(head, 20)
  Solution().printLinkedList(head)
  head = Solution().insertAtK(head, 30, 5)
  Solution().printLinkedList(head)
  Solution().insertAtNode(head.next, 50)
  Solution().printLinkedList(head)