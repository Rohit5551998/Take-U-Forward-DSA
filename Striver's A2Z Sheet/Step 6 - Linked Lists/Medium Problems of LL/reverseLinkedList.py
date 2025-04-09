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
    if (head is None or head.next is None):
      return head

    curr = head
    prev = None

    while (curr is not None):
      front = curr.next
      curr.next = prev
      prev = curr
      curr = front
    return prev
  
  def reverseRecursive(self, head):
    if (head is None or head.next is None):
      return head
    
    # Recursive step:
    # Reverse the linked list starting from the second node (head.next)
    newHead = self.reverseRecursive(head.next)
     # Save a reference to the node following
    # the current 'head' node.
    front = head.next
    # Make the 'front' node point to the current
    # 'head' node in the reversed order.
    front.next = head
    # Break the link from the current 'head' node
    # to the 'front' node to avoid cycles.
    head.next = None
    # Return the 'new_head,' which is the new
    # head of the reversed linked list.
    return newHead


if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  Solution().printLinkedList(head)
  head = Solution().reverseLinkedList(head)
  Solution().printLinkedList(head)
  head = Solution().reverseRecursive(head)
  Solution().printLinkedList(head)


"""
Reverse Linked List
Brute Force
1. Create a empty stack and push all elements of list onto stack till None is reached.
2. Run another loop from head and assign the top element of stack to head and pop the element from stack
3. Continue this process until stack is empty
TC -> O(2n), SC -> O(n)

Optimal Approach (Iterative Approach)
1. Check if head or head.next is None and return head
2. Assign current = head, prev = None and run a loop till curr is None
3. First assign front = curr.next then break link of current node and reverse it with curr.next = prev
4. Afterwards assign prev = curr and curr = front
5. Once done return prev
TC -> O(n), SC -> O(1)

Optimal Apprach (Recursive Approach)
1. Establish Base Case Conditions: Check if the linked list is either empty or contains only one node. If so, the list 
is already reversed; hence, return the head as is.
2. Recursively Reverse the List: Begin the recursive step by reversing the linked list, starting from the second node. 
Utilise a recursive call to the reverse linked list function, passing the next node as an argument.
3. Preserve Access to Remaining Nodes: To maintain access to the rest of the linked list while reversing the order, store 
a reference to the node following the current 'head' node. This step ensures continuity in the link sequence during 
reversal.
4. Reverse Link Direction: Adjust the 'front' node to point to the current 'head' node in the reversed order. This action 
effectively reverses the link between the 'head' node and the 'front' node.
5. Prevent Cyclic References: Break the link from the current 'head' node to the 'front' node to prevent any cyclic 
formations. Set 'head->next' to 'NULL' to ensure the reversed segment of the list does not create a loop.
6. Return the New Head: Finally, return the 'newHead,' which signifies the new head of the reversed linked list. This 
'newHead' was initially the last node in the list before the reversal commenced.
TC -> O(n), SC -> O(1)
"""