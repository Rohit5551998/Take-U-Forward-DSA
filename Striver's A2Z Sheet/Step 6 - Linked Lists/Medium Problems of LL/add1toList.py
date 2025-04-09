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

  def calculateCarry(self, head):
    if (head is None):
      return 1
    
    carry = self.calculateCarry(head.next)
    head.data += carry

    if head.data == 10:
      head.data = 0
      return 1
    return 0
  
  def add1toList(self, head):
    carry = self.calculateCarry(head)
    if carry == 1:
      newHead = Node(1)
      newHead.next = head
      head = newHead
    return head

if __name__ == "__main__":
  arr = [9, 9, 9, 9]
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().add1toList(head)
  Solution().printLinkedList(head)


"""
Add 1 to Linked List Elements
Brute Force
1. Reverse the linked list
2. Add 1 to the first element
3. Traverse the linked list and if the element is 10, change it to 0 and add 1 to the next element
4. Reverse the linked list
TC -> O(2n), SC -> O(1)

Optimal Approach
1. Call calculateCarry function recursively to calculate the carry
2. Inside calculateCarry function, if head is None, return 1
3. Else recursively call calculateCarry function for next element and add the carry to the current element
4. If element is 10, change it to 0 and return 1
5. Else return 0
6. Outside calculateCarry function, check if carry is 1, then add 1 to the head and change head to newHead
7. Return head
TC -> O(n), SC -> O(1)
"""