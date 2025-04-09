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
  
  def deleteAtHeader(self, head):
    if (head == None):
      return None
    return head.next
  
  def deleteAtTail(self, head):
    if (head == None or head.next == None):
      return None
    
    temp = head
    while (temp.next.next is not None):
      temp = temp.next

    temp.next = None
    return head
  
  def deleteAtK(self, head, k):
    if (head == None): return None
    if (k == 1): return head.next

    temp = head
    prev = None
    cnt = 0
    while (temp is not None):
      cnt += 1
      if (cnt == k):
        prev.next = prev.next.next
        break
      prev = temp
      temp = temp.next
    return head
  
  def deleteValue(self, head, val):
    if (head == None): return None
    if (head.data == val): return head.next

    temp = head
    prev = None
    while (temp is not None):
      if (temp.data == val):
        prev.next = prev.next.next
        break
      prev = temp
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
  Solution().printLinkedList(head)
  head = Solution().deleteAtHeader(head)
  Solution().printLinkedList(head)
  head = Solution().deleteAtTail(head)
  Solution().printLinkedList(head)
  head = Solution().deleteAtK(head, 3)
  Solution().printLinkedList(head)
  head = Solution().deleteValue(head, 1)
  Solution().printLinkedList(head)