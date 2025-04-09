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
  def __init__(self, data, next1 = None): # data -> value stored in node
    self.data = data
    self.next = next1

class Solution:
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

  def middleElement1(self, head):
    if head is None or head.next is None:
      return head

    cnt = 1
    temp = head

    while (temp.next is not None):
      temp = temp.next
      cnt += 1

    mid = cnt // 2 + 1

    temp = head
    cnt = 1
    while (cnt != mid):
      cnt += 1
      temp = temp.next

    return temp
  
  def detectLoop1(self, head):
    hashMap = {}

    temp = head
    resp = False
    while (temp is not None):
      if (temp in hashMap):
        resp = True
        break

      hashMap[temp] = 1
      temp = temp.next

    return resp  
  
  def detectLoop(self, head):
    slow, fast = head, head
    resp = False
    while (fast is not None and fast.next is not None):
      slow = slow.next
      fast = fast.next.next

      if (slow == fast):
        resp = True
        break

    return resp
    
if __name__ == "__main__":
  arr = [1, 2, 3, 2, 1]
  head = Solution().convertArr2LL(arr)
  head.next.next.next.next = head.next.next
  print(Solution().detectLoop(head))

"""
Detect Loop In Linked List
Brute Force
1. Initialize HashMap and store all nodes in hashmap by looping over list
2. Before Adding to HashMap check if Node already exists in Linked List and Return True
3. At End of Loop Return False
TC -> O(n * 2log(n)), SC -> O(n)

Optimal Approach
1. Initialize slow = head, fast = head and Run a loop till fast is not None or fast.next is not None.
2. If At Point slow == fast, return True
3. At End of Loop if the linked list is linear return False
TC -> O(n), SC -> O(1)
"""