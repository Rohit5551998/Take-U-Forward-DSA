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

  def reverseLinkedList(self, head):
    if (head is None or head.next is None):
      return head
    
    prev = None
    curr = head

    while (curr is not None):
      front = curr.next
      curr.next = prev
      prev = curr
      curr = front
    return prev

  def palindromeLinkedList(self, head):
    if (head is None or head.next is None):
      return True
    
    slow, fast, resp = head, head, True

    while (fast.next is not None and fast.next.next is not None):
      slow = slow.next
      fast = fast.next.next

    newHead = self.reverseLinkedList(slow.next)
    first, second = head, newHead

    while (second is not None):

      if (first.data != second.data):
        resp = False
        break

      first = first.next
      second = second.next

    self.reverseLinkedList(newHead)

    return resp
      
if __name__ == "__main__":
  arr = [1, 2, 3, 2, 1]
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  print(Solution().palindromeLinkedList(head))
  Solution().printLinkedList(head)


"""
Palindrome Linked List
Brute Force
1. Create empty stack and traverse through list and add each data element to stack.
2. Run another loop and check if list data element matches popped stack element.
3. If at any point it does not match return False.
4. At end of loop return True.
TC -> O(2n), SC -> O(n)

Optimal Approach
1. If linked list is empty or contains one element return True.
2. Initialize pointers slow and fast to head, resp = True and run loop till fast.next.next or fast.next is not None.
3. Inside loop move slow by 1 node and fast by 2 nodes. At end of loop slow will point to middle of list.
4. Reverse linked list from slow.next and assign first and second as the head of both list.
5. If at any point elements do not match assign resp = False and break
6. At end of loop reverse the reversed linked list
TC -> O(2n), SC -> O(1)
"""