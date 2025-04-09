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

  def deleteOccurences(self, head, key):
    if (head is None): return None

    temp = head
    while (temp is not None):
      if (head.data == key):
        head = head.next

      if (temp.data == key):
        prevNode, nextNode = temp.prev, temp.next
        if (prevNode is not None): prevNode.next = nextNode
        if (nextNode is not None): nextNode.prev = prevNode
        temp = nextNode
      else:
        temp = temp.next
    return head

if __name__ == "__main__":
  arr = [10, 4, 10, 10, 6, 10]
  head = Solution().convertArr2LL(arr)
  head = Solution().deleteOccurences(head, 10)
  Solution().printLinkedList(head)


"""
Delete All Occurences of Key From DLL
Optimal Approach
1. Initialize temp = head and Run a loop till temp is not None if temp.data == key shift head = head.next
2. Assign prevNode = temp.prev, nextNode = temp.next
3. If prevNode != None, assign prevNode.next = nextNode
4. If nextNode != None, assign nextNode.prev = prevNode
5. Assign temp = nextNode
6. Else temp = temp.next
TC -> O(n), SC -> O(1)
"""