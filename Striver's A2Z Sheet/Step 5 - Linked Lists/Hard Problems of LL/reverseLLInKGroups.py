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
    if (head is None or head.next is None): return head

    prev = None
    curr = head

    while (curr is not None):
      front = curr.next
      curr.next = prev
      prev = curr
      curr = front

    return prev

  def getKthNode(self, temp, k):
    # Current Node
    k -= 1

    while (temp is not None and k > 0):
      k -= 1
      temp = temp.next

    return temp

  def reverseK(self, head, k):
    if (head is None or head.next is None): return head

    temp = head
    prevNode = None

    while (temp is not None):
      kthNode = self.getKthNode(temp, k)

      if (kthNode is None):
        #Unfinished Iteration So No Reversal Required
        if (prevNode): 
          prevNode.next = temp
          break

      nextNode = kthNode.next
      kthNode.next = None

      self.reverseLinkedList(temp)

      if (temp == head):
        head = kthNode
      else:
        # If PrevNode is not None then need to attach it to reversed kth node
        prevNode.next = kthNode

      prevNode = temp
      temp = nextNode
    return head

if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0, 10, 9, 3]
  k = 3
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().reverseK(head, k)
  Solution().printLinkedList(head)

"""
Reverse Linked List In Groups of Size K
Optimal Approach
1. Initialise a pointer `temp` to the head of the linked list. Using `temp`, traverse to the Kth Node iteratively.
2. On reaching the Kth Node, preserve the Kth Node’s next node as `nextNode` and set the Kth Node’s next pointer to `null`.
This effectively breaks the linked list in a smaller list of size K that can be reversed and attached back.
3. Treat this segment from `temp` to Kth Node as an individual linked list and reverse it. This can be done via the help 
of a helper function `reverseLinkedList` 
4. The reversed linked list segment returns a modified list with `temp` now at its tail  and the `KthNode` pointing to its
head. Update the `temp`s `next` pointer to `nextNode`. If we are at the first segment of K nodes, update the head to `Kth Node`.
5. Continue this reversal for further groups. If a segment has fewer than K Nodes, leave them unmodified and return the 
new head. Use the prevLast pointer to maintain the link between the end of the previous reversed segment and the current 
segment.
TC -> O(2n), SC -> O(1)
"""