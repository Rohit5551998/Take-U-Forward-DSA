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

  def rotateLL(self, head, k):
    if (head is None or head.next is None):
      return head

    cnt = 1
    temp = head

    while (temp.next is not None):
      cnt += 1
      temp = temp.next

    k = k % cnt

    if (k == 0): return head

    temp.next = head

    end = cnt - k
    while (end):
      end -= 1
      temp = temp.next

    head = temp.next
    temp.next = None

    return head

if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  k = 13
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().rotateLL(head, k)
  Solution().printLinkedList(head)

"""
Rotate Linked List
Optimal Approach
1. Calculate the length of the list.
2. Connect the last node to the first node, converting it to a circular linked list.
3. Iterate to cut the link of the last node and start a node of k%length of the list rotated list.
TC -> O(length of list) + O(length of list - (length of list%k)), SC -> O(1)
"""