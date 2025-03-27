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

  def sortLinkedList(self, head):
    oneHead, twoHead, zeroHead = Node(-1), Node(-1), Node(-1)
    oneTail, twoTail, zeroTail = oneHead, twoHead, zeroHead
    curr = head

    while (curr is not None):
      temp = curr
      if curr.data == 0:
        zeroTail.next = temp
        zeroTail = zeroTail.next

      elif curr.data == 1:  
        oneTail.next = temp
        oneTail = oneTail.next

      else:
        twoTail.next = temp
        twoTail = twoTail.next

      curr = curr.next
      temp.next = None

    zeroTail.next = oneHead.next if oneHead.next is not None else twoHead.next
    oneTail.next = twoHead.next
    return zeroHead.next
      
if __name__ == "__main__":
  # arr = [1, 2, 0, 0, 2, 1, 1, 2, 0, 0]
  arr = [2, 2, 0, 0, 2, 2, 2, 2, 0, 0]
  arr = [2, 2, 1, 1, 2, 2, 2, 2, 1, 1]
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().sortLinkedList(head)
  Solution().printLinkedList(head)


"""
Sort Linked List of 0, 1 and 2
Brute Force
1. Run a loop to count the number for elements in linked list for 0, 1 and 2 in cnt0, cnt1, cnt2
2. Run loops to change node element's values till each counter is exhausted
TC -> O(2n), SC -> O(1)

Optimal Approach
1. Create three separate dummy nodes for 0, 1 and 2 lists
2. Check each nodes value and assign them to respective linked list
3. Once done assign zero's tail to one's head.next if exists or two's head.next
4. If one's head.next exists assign one's tail to two's head.next
5. Return zero's head.next
TC -> O(n), SC -> O(1)
"""