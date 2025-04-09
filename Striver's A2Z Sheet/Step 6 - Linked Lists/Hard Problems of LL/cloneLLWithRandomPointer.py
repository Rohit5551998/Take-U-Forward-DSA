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
    self.random = None # random pointer

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

  def cloneLinkedList1(self, head):
    hashMap = {}
    newHead = Node(-1)
    curr = head
    while curr is not None:
      hashMap[curr] = Node(curr.data)
      curr = curr.next

    curr = head
    res = newHead
    while curr is not None:
      res.next = hashMap[curr]
      res.next.random = hashMap[curr.random] if curr.random is not None else None
      curr = curr.next
      res = res.next
    return newHead.next

  def cloneLinkedList(self, head):
    if head is None: return None

    curr = head
    while curr is not None:
      newNode = Node(curr.data)
      newNode.next = curr.next
      curr.next = newNode
      curr = curr.next.next

    curr = head
    while curr is not None:
      curr.next.random = curr.random.next if curr.random is not None else None
      curr = curr.next.next

    curr = head
    newHead = Node(-1)
    res = newHead

    while curr is not None:
      res.next = curr.next
      curr.next = curr.next.next
      res = res.next
      curr = curr.next

    return newHead.next

if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  head = Solution().cloneLinkedList(head)
  Solution().printLinkedList(head)

"""
Clone LL With Random Pointer
Brute Force
1. Initialize a hash map to store the mapping of original nodes to their clones.
2. Traverse the original linked list and create a new node for each original node and store mapping in hashmap.
3. Traverse the original linked list again and set the next and random pointers of the cloned nodes using the hash map.
4. Return the head of the cloned linked list.
Time Complexity: O(2N), Space Complexity: O(N) + O(N)

Optimal Approach
1. Traverse the list create a new node for each original node and insert it right after the original node.
2. Traverse the list again and set the random pointers of the cloned nodes to point to the corresponding cloned nodes.
3. Assign Dummy Node as Head of New Linked List and Traverse the original list to separate the original and cloned nodes.
4. Return the head of the cloned linked list.
Time Complexity: O(3N), Space Complexity: O(N)
"""