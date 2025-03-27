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

  def addTwoNumber(self, head1, head2):
    sumList = Node(-1)
    sumListHead = sumList
    carry = 0
    curr1, curr2 = head1, head2
    while (curr1 is not None or curr2 is not None):
      el1 = curr1.data if curr1 is not None else 0
      el2 = curr2.data if curr2 is not None else 0
      addition = el1 + el2 + carry
      data = addition % 10
      carry = addition // 10

      sumList.next = Node(data)
      sumList = sumList.next

      if (curr1 is not None): curr1 = curr1.next
      if (curr2 is not None): curr2 = curr2.next

    if (carry > 0): sumList.next = Node(carry)

    return sumListHead.next

if __name__ == "__main__":
  arr1 = [2, 4, 6, 7, 5, 9, 9]
  arr2 = [4, 7, 2, 3, 5]
  head1 = Solution().convertArr2LL(arr1)
  head2 = Solution().convertArr2LL(arr2)
  Solution().printLinkedList(head1)
  Solution().printLinkedList(head2)
  head = Solution().addTwoNumber(head1, head2)
  Solution().printLinkedList(head)


"""
Segregate Even And Odd Nodes in LL
Optimal Approach
1. Create New Sum Linked List with Dummy Element and assign SumListHead equal to this node.
2. Assign Carry to 0 and Traverse through both linked lists until either exists.
3. If either of the linked lists exists, assign the node's data to el1 and el2 else assign 0 to them.
4. Take addition = e1 + e2 + carry, data = addition % 10 and carry = addition // 10.
5. Create New Node with data and assign it to the next of the sum list and then set sumList = sumList.next.
6. If curr1 exists, assign curr1 to curr1.next else assign None to curr1.
7. If curr2 exists, assign curr2 to curr2.next else assign None to curr2.
8. At end of loop if carry > 0, assign new Node with carry to the next of the sum list.
9. Return the next of the sumListHead.
TC -> O(max(m,n)), SC -> O(max(m,n))
"""