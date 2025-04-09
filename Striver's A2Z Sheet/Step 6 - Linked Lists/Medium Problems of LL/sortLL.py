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

  def middleElement(self, head):
    if (head is None or head.next is None): return head

    slow, fast = head, head.next

    while (fast.next is not None and fast.next.next is not None):
      slow = slow.next
      fast = fast.next.next

    return slow

  def mergeLL(self, left, right):
    dummyNode = Node(-1)
    temp = dummyNode

    while(left is not None and right is not None):
      if (left.data <= right.data):
        temp.next = left
        left = left.next
      else:
        temp.next = right
        right = right.next

      temp = temp.next

    if (left is None):
      temp.next = right
    else:
      temp.next = left

    return dummyNode.next


  def sortLL(self, head):
    if (head is None or head.next is None):
      return head

    middleElement = self.middleElement(head)
    leftHead = head
    rightHead = middleElement.next
    middleElement.next = None

    leftHead = self.sortLL(leftHead)
    rightHead = self.sortLL(rightHead)

    head = self.mergeLL(leftHead, rightHead)
    return head

if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().sortLL(head)
  Solution().printLinkedList(head)

"""
Sort Linked List
Brute Force
1. Traverse the linked list and append all elements to an array.
2. Sort the array and replace all elements in linked list
3. Continue this process until stack is empty
TC -> O(N) + O(N log N) + O(N), SC -> O(N)

Optimal Approach
1. Check if head or head.next is None and return head as LL is already sorted
2. Find the first middle element and split the linked list in half recursively
3. Once done apply merging algorithm on left and right halves to get sorted LL and update head of new linked list
4. Return the updated head
TC -> O((N + N/2) * log N), SC -> O(1)
"""