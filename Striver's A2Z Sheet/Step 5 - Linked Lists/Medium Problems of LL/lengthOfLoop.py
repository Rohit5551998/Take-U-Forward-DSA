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
  
  def lengthOfLoop1(self, head):
    hashMap = {}
    cnt = 1
    resp = 0
    temp = head
    while (temp is not None):
      if (temp in hashMap):
        resp = cnt - hashMap[temp]
        break

      hashMap[temp] = cnt
      cnt += 1
      temp = temp.next

    return resp  
  
  def lengthOfLoop(self, head):
    slow, fast = head, head
    resp = 0
    while (fast is not None and fast.next is not None):
      slow = slow.next
      fast = fast.next.next

      if (slow == fast):
        cnt = 1
        fast = fast.next

        while (slow != fast):
          fast = fast.next
          cnt += 1
          
        resp = cnt
        break

    return resp
    
if __name__ == "__main__":
  arr = [1, 2, 3, 2, 1]
  head = Solution().convertArr2LL(arr)
  head.next.next.next.next.next = head.next.next
  print(Solution().lengthOfLoop(head))

"""
Starting Point Of Loop In Linked List
Brute Force
1. Initialize HashMap and store all nodes in hashmap by looping over list and assign 0 based counter
2. Before Adding to HashMap check if Node already exists in Linked List and Return current counter - the stored nodes's index
3. At End of Loop Return 0
TC -> O(n * 2log(n)), SC -> O(n)

Optimal Approach
1. Initialize slow = head, fast = head and Run a loop till fast is not None or fast.next is not None.
2. If At Point slow == fast, reset slow to head and run a loop till slow != fast
3. Both Pointers Will Collide At Start of Loop
4. At End of Loop if the linked list is linear return -1
TC -> O(n), O(1)
"""