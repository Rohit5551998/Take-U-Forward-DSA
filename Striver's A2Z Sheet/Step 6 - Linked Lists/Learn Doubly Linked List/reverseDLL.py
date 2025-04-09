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
  def __init__(self, data, next1 = None, prev1 = None): # data -> value stored in node
    self.data = data
    self.next = next1
    self.prev = prev1

class Solution:
  def convertArr2LL(self, arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
      temp.next = Node(arr[i], None, temp)
      temp = temp.next
    return head

  def printLinkedList(self, head):
    temp = head
    while temp is not None:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")  

  def reverseDLL(self, head):

    if (head is None or head.next is None):
      return head

    temp = head
    last = None
    while (temp is not None):
      last = temp.prev
      temp.prev = temp.next
      temp.next = last
      temp = temp.prev
    
    # The final node in the original list
    # becomes the new head after reversal
    return last.prev


if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().reverseDLL(head)
  Solution().printLinkedList(head)


"""
Reverse DLL
Brute Force
1. Initialization a temp pointer to the head of the doubly linked list and a stack data structure to store the 
values from the list.
2. Traverse the doubly linked list with the temp pointer and while traversing push the value at the current node temp 
onto the stack. Move the temp to the next node continuing until temp reaches null indicating the end of the list.
3. Reset the temp pointer back to the head of the list and in thissecond iteration pop the element from the stack, 
replace the data at the current node with the popped value from the top of the stack and move temp to the next node. 
4. Repeat this step until temp reaches null or the stack becomes empty.
TC -> O(2n), SC -> O(n)

Optimal Approach
1. If head or head.next is None then no changes required simply return head
2. Initialize temp as head and last as None and run loop until temp is not None
3. Assign temp.prev to last then assign temp.prev = temp.next and finally assign temp.next = last
4. Move to the next element using temp = temp.prev
5. At end of loop the head will be modified to last.prev
TC -> O(n), SC -> O(1)
"""