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
  def __init__(self, data): # data -> value stored in node
    self.data = data
    self.next = None

class Solution:
  def convertArr2LL(self, arr):
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
      temp.next = Node(arr[i])
      temp = temp.next
    return head
        

if __name__ == "__main__":
  arr = [2, 4, 6, 7, 5, 1, 0]
  resp = Solution().convertArr2LL(arr)
  print(resp)