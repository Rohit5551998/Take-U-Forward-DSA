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

  def removeDuplicates(self, head):
    if (head is None): return None

    temp = head
    nextNode = temp.next

    while (temp is not None):
      while (nextNode is not None and nextNode.data == temp.data):
        nextNode = nextNode.next

      temp.next = nextNode
      if (nextNode is not None): nextNode.prev = temp

      temp = temp.next

    return head

if __name__ == "__main__":
  arr = [1, 1, 4, 6, 6, 10, 10, 10, 10]
  head = Solution().convertArr2LL(arr)
  head = Solution().removeDuplicates(head)
  Solution().printLinkedList(head)


"""
Remove Duplicates From Sorted DLL
Optimal Approach
1. Initialize temp = head and Run a loop till temp is not None
2. Assign nextNode = temp.next Run another loop till nextNode is not None and temp.data is equal to nextNode.data
3. Inside Inner Loop Assign nextNode = nextNode.next
3. Assign temp.next = nextNode and if nextNode is not None assign nextNode.prev = temp
4. Assign temp = temp.next
TC -> O(n), SC -> O(1)
"""