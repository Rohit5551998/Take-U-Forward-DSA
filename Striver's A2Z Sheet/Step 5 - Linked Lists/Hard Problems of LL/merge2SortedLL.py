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

  def mergeTwoSorted(self, head1, head2):
    newHead = Node(-1)
    temp = newHead

    while (head1 is not None and head2 is not None):
      if head1.data < head2.data:
        temp.next = head1
        temp = temp.next
        head1 = head1.next
      else:
        temp.next = head2
        temp = temp.next
        head2 = head2.next

      temp.next = None

    if (head1 is not None):
      temp.next = head1
    else:
      temp.next = head2

    return newHead.next

if __name__ == "__main__":
  arr1 = [0, 1, 2, 4, 5, 6, 7]
  arr2 = [5, 6, 7, 8]
  head1 = Solution().convertArr2LL(arr1)
  head2 = Solution().convertArr2LL(arr2)
  head = Solution().mergeTwoSorted(head1, head2)
  Solution().printLinkedList(head)

"""
Merge Two Sorted Linked Lists
Brute Force
1. Initialize Empty Array to Store Elements From All Linked Lists
2. Once done sort the array and create new linked list from this array
Time Complexity: O(N1 + N2) + O(N log N) + O(N), Space Complexity: O(N) + O(N)


Better Approach (Merging Two Lists At a Time)
1. Perfom merging of LL by returning new head after each merge.
2. Return the final head after merge operation is completed
Time Complexity: O(N1+N2), Space Complexity: O(1)
"""