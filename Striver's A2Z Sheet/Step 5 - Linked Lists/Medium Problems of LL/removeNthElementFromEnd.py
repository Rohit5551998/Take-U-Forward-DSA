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

  def removeNthEnd(self, head, k):
    cnt = 0
    fast, slow = head, head
    while (cnt < k):
      cnt += 1
      fast = fast.next
    if (fast is None):
      return head.next
    
    while (fast.next is not None):
      slow = slow.next
      fast = fast.next

    slow.next = slow.next.next

    return head


if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().removeNthEnd(head, 5)
  Solution().printLinkedList(head)


"""
Remove Nth Element From End
Brute Force
1. Run a loop to count the number for elements in linked list.
2. If k == cnt return head.next
3. Run another loop with temp to go until cnt - k with temp = temp.next
4. Once done assign temp.next = temp.next.next and return old head
TC -> O(l)+O(l-n), SC -> O(1)

Optimal Approach
1. Run a loop till k and fast pointer and assign fast = fast -> next
2. If fast is None return head.next
3. Assign Slow and run loop till fast.next is not None move both pointers to next element
4. Afterwards assign slow.next = slow.next.next
5. Once done return head
TC -> O(n), SC -> O(1)
"""