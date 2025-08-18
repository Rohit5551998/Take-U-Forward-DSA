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
    self.child = None # random pointer

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

  def convertArrToLL(self, ans):
    newHead = Node(-1)
    temp = newHead

    for i in range(0, len(ans)):
      temp.child = Node(ans[i])
      temp = temp.child
    return newHead.child

  def flattenLinkedList1(self, head):
    if (head is None): return None

    ans = []

    temp1 = head
    while (temp1 is not None):
      temp2 = temp1
      while (temp2 is not None):
        ans.append(temp2.data)
        temp2 = temp2.child
      temp1 = temp1.next
    
    ans.sort()
    return self.convertArrToLL(ans)
  
  def merge(self, head1, head2):
    newHead = Node(-1)
    temp = newHead

    while (head1 is not None and head2 is not None):
      if head1.data < head2.data:
        temp.child = head1
        temp = temp.child
        head1 = head1.child
      else:
        temp.child = head2
        temp = temp.child
        head2 = head2.child

      temp.next = None

    if (head1 is not None):
      temp.child = head1
    else:
      temp.child = head2

    if (newHead.child is not None): newHead.child.next = None

    return newHead.child

  def flattenLinkedList(self, head):
    if (head is None or head.next is None):
      return head
    
    mergedListHead = self.flattenLinkedList(head.next)

    head = self.merge(head, mergedListHead)
    return head

if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  head = Solution().convertArr2LL(arr)
  head = Solution().flattenLinkedList(head)
  Solution().printLinkedList(head)

"""
Flatten Linked List
Brute Force
1. Initialize empty array to store all linked list elements
2. Traverse the linked list and if child exists traverse downwards and add all elements to an array.
3. Sort the entire array and create new linked list from this sorted array
Time Complexity: O(N*M) + O(N*M log(N*M)) + O(N*M), Space Complexity: O(N*M) + O(N*M)

Optimal Approach
1. Establish Base Case Conditions Check if the base case conditions are met, return the head if it is null or has no 
next pointer to head as there’s no further flattening or merging required.
2. Recursively Merge the List: Initiate the recursive flattening process by calling `flattenLinkedList` on the next node 
(`head -> next`).
3. The result of this recursive call is the head of the flattened and merged linked list.
4. Merge Operations: Inside the recursive call, call the merge function which takes care of the merging of these two lists
based on their data values.
5. Initialise two pointers, t1 and t2 to the heads of the input linked lists. Create a dummyNode with value -1 that will 
serve as the starting point of the merged list. Use a temp pointer to traverse and build the combined merged list.
6. While t1 and t2 are not null: Compare the values of t1 and t2, connect the node with smaller value to the temp pointer 
of the merged combined list. Move the temp pointer and the respective t1 and t2 pointer to their next nodes.
7. Attach the remaining nodes of the non-empty list directly to the temp pointer as they are already sorted.
8. Return the next of the dummyNode as the head of the merge sorted linked list.
9. The merged list is updated in the head, which is then returned as the result of the flattening process.
Time Complexity: O(3N), Space Complexity: O(N)
"""