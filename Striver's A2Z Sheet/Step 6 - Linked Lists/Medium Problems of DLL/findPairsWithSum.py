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

  def findPairs1(self, head, target):
    if (head is None or head.next is None): return []

    temp1 = head
    ans = []
    while (temp1.next is not None):
      temp2 = temp1.next
      while (temp2 is not None and temp1.data + temp2.data <= target):
        if (temp1.data + temp2.data == target): ans.append((temp1.data, temp2.data))
        temp2 = temp2.next
      temp1 = temp1.next
        
    return ans
  
  def findPairs(self, head, target):
    ans = []
    if (head is None or head.next is None): return ans

    left, right = head, head
    while (right.next is not None):
      right = right.next


    while (right is not None and right.data > left.data):
      sum = left.data + right.data
      if (sum > target): right = right.prev
      elif (sum < target): left = left.next
      else: 
        ans.append((left.data, right.data))
        left = left.next
        right = right.prev

    return ans

if __name__ == "__main__":
  arr = [3, 4, 5, 6, 7, 9, 12, 15, 16, 18, 19, 20, 21, 22, 24, 25, 28, 31, 32, 33, 34, 38, 41, 42, 44, 47, 48, 49]
  head = Solution().convertArr2LL(arr)
  print(Solution().findPairs(head, 50))


"""
Find Pairs With Sum In DLL
Brute Force
1. Assign temp1 = head, ans = [] and run a loop till temp1.next is not None
2. Assign temp2 = temp1.next and run another loop till temp2 is not None and temp1.data and temp2.data <= sum
3. If sum == k append tuple to final ans
4. Return final ans array.
TC -> O(n**2), SC -> O(1)

Optimal Approach
1. Initialize ans = [], left = head, right = tail(run loop) and Run till right is not None and right.data > left.data
2. Calculate sum = left.data + right.data
3. If sum < k left = left.next
4. If sum > k right = right.prev
4. If sum == k append tuple to ans array
5. Return final ans array
TC -> O(n), SC -> O(1)
"""