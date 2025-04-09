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

  def mergeKSorted1(self, lists):
    if (not lists): return None

    head = lists[0]

    for i in range(1, len(lists)):
      head = self.mergeTwoSorted(head, lists[i])

    return head
  
  def mergeKSorted(self, lists):
    if (not lists): return None

    pq = queue.PriorityQueue()
    newHead = Node(-1)
    temp = newHead

    for i in range(0, len(lists)):
      node = lists[i]
      if (node is not None): pq.put((node.data, i, node))

    while (not pq.empty()):
      _, index, curr = pq.get()

      if (curr.next is not None): pq.put((curr.next.data, index, curr.next))

      temp.next = curr
      temp = temp.next

    return newHead.next

if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  head = Solution().mergeKSorted(head)
  Solution().printLinkedList(head)

"""
Merge K Sorted Linked Lists
Brute Force
1. Initialize Empty Array to Store Elements From All Linked Lists
2. Once done sort the array and create new linked list from this array
Time Complexity: O(K*N) + O((N*K) * log(N*K)) + O(N*K), Space Complexity: O(N*K) + O(N*K)


Better Approach (Merging Two Lists At a Time)
1. Use the first list as first list for merging.
2. Loop through the remaining lists and perfom merging of LL by returning new head after each merge.
3. Return the final head after all merge operations are completed
Time Complexity: O( N*k(k+1)/2) ~ O(N*k^2), Space Complexity: O(1)

Optimal Approach
1. Initialise a Priority Queue that stores pair of element data and node and store head of linked lists in it.
2. Create a dummy node and run a loop till priority queue is not empty
3. Inside loop pop the topmost element and add to new linked list created.
4. If next of the popped element exists add it to queue.
5. Return next of the dummy node created
Time Complexity: O(K log K) + O(N*K*(3*log K)), Space Complexity: O(K)
"""