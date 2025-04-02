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
      return None

    cnt = 1
    temp = head

    while (temp.next is not None):
      temp = temp.next
      cnt += 1

    mid = cnt // 2

    temp = head
    cnt = 1
    while (cnt != mid):
      cnt += 1
      temp = temp.next

    temp.next = temp.next.next

    return head
  
  def middleElement(self, head):
    if head is None or head.next is None:
      return None

    slow, fast = head, head.next

    while (fast.next is not None and fast.next.next is not None):
      slow = slow.next
      fast = fast.next.next

    slow.next = slow.next.next

    return head 
      
if __name__ == "__main__":
  arr = [1, 2, 3, 4, 2, 1]
  head = Solution().convertArr2LL(arr)
  head = Solution().middleElement(head)
  Solution().printLinkedList(head)

"""
Delete Middle of Linked List
Brute Force
1. Loop through linked list and maintain count of elements
2. Calculate mid = n//2 element and run another loop to find the element at this position.
3. Change pointer of this location with temp.next = temp.next.next
TC -> O(n + n/2), SC -> O(1)

Optimal Approach
1. Initialize slow = head, fast = head.next and Run a loop till fast is not None or fast.next is not None.
2. At end of loop slow will point to prev of middle element.
3. Assign slow.next = slow.next.next
TC -> O(n/2), SC -> O(1)
"""