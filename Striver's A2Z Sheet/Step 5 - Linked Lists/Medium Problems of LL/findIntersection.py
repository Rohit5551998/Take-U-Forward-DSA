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

  def getDifference(self, head1, head2):
    len1, len2 = 0, 0
    temp1, temp2 = head1, head2
    while (temp1 is not None or temp2 is not None):
      if (temp1 is not None):
        len1 += 1
        temp1 = temp1.next
      if (temp2 is not None):
        len2 += 1
        temp2 = temp2.next
    return len1-len2

  def findIntersection1(self, head1, head2):
    diff = self.getDifference(head1, head2)

    if (diff < 0):
      while (diff != 0):
        head2 = head2.next
        diff += 1

    else:
      while (diff != 0):
        head1 = head1.next
        diff -= 1

    while (head1 is not None):
      if (head1 == head2):
        return head1
      head1 = head1.next
      head2 = head2.next

    return head1
  
  def findIntersection(self, head1, head2):
    temp1, temp2 = head1, head2
    while (temp2 != temp1):
      temp1 = head2 if temp1 is None else temp1.next
      temp2 = head1 if temp2 is None else temp2.next

    return temp1
      
if __name__ == "__main__":
  arr = [1, 2, 3, 2, 1]
  head = Solution().convertArr2LL(arr)
  arr1 = [4, 5, 6]
  head1 = Solution().convertArr2LL(arr1)
  # head1.next = head.next.next
  print(Solution().findIntersection(head, head1))

"""
Find Intersection
Brute Force
1. Initialize HashMap and Iterate through List 1 and Store it's Nodes in HashMap with Value 1.
2. Run another loop and check if List 2 node is present in HashMap if present return the first matched element.
3. If No Match Return None.
TC -> O(n+m), SC -> O(n)

Better Approach
1. Count the number of elements in both lists and run a loop till diff in longer list.
2. Once done both lists will have equal number of elements simply run loop and return first matched element.
TC -> O(2max(length of list1,length of list2))+O(abs(length of list1-length of list2))+O(min(length of list1,length of list2)), SC -> O(1)

Optimal Approach
1. Initialize temp1 = head1, temp2 = head2 and Run a loop till node 1 != node 2.
2. If temp1 is None assign it to head2 and if temp2 is None assign it to head1.
3. Return the first matched element
TC -> O(2*max(length of list1,length of list2)), O(1)
"""