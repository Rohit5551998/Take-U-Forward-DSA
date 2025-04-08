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

  def oddEvenList(self, head):
    oddHead, evenHead = Node(-1), Node(-1)
    oddTail = oddHead
    evenTail = evenHead
    curr = head
    cnt = 0
    temp = None
    while (curr is not None):
      cnt += 1

      temp = curr
      curr = curr.next
      temp.next = None

      if (cnt % 2 == 1):
        oddTail.next = temp
        oddTail = oddTail.next
      else:
        evenTail.next = temp
        evenTail = evenTail.next

    oddTail.next = evenHead.next
    return oddHead.next



if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().oddEvenList(head)
  Solution().printLinkedList(head)


"""
Segregate Even And Odd Nodes in LL
Brute Force
1. Initialize two empty arrays of size n/2 and traverse through all linked list elements and add elements at even and odd
indexed in respective arrays.
2. Loop through the linked list and assign values from odd array to linked first then from even array.
TC -> O(2n), SC -> O(n)

Optimal Approach
1. Create two separate linked list with odd and even index elements and assign them dummy node of -1 and initilaize
oddTail = oddHead and evenTail = evenHead.
2. Loop through linked list and add elements to respective linked lists to element exists.
3. Assign Current Element to Temp, Move to Next Element and then remove next of temp.
4. Afterwards check count and assign to respective linked list.
5. At end of loop, assign evenHead.next to oddTail.next and return oddHead.next.
TC -> O(n), SC -> O(1)
"""