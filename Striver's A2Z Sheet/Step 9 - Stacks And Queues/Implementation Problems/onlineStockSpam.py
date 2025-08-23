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

from queue import PriorityQueue, Queue, LifoQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
    def __init__(self):
      self.stockLessList = []
      self.stack = []
      self.index = -1

    def next(self, price: int) -> int:
      self.index += 1
      self.stockLessList.append(price)
      while (self.stack and price >= self.stockLessList[self.stack[-1]]):
        self.stack.pop()
      pge = -1 if not self.stack else self.stack[-1]
      self.stack.append(self.index)
      return self.index - pge

if __name__ == "__main__":

  prices = [100, 80, 60, 70, 60, 75, 85]

  spanner = Solution()
  for price in prices:
    print(spanner.next(price))

  print([1, 1, 1, 2, 1, 4, 6])
  # print(spanner.stockLessList)
  # print(spanner.findSolution(prices))
"""
Online Stock Spam
Optimal Approach
1. Initialize a stack and a list to store the stock less list along with index
2. Iterate through the prices and append the price to the stock less list and increment the index
3. While the stack is not empty and the current price is greater than the price at the index of the stack, pop the stack
4. If the stack is empty, append -1 to the stock less list else append the index of the stack to the stock less list
5. Return the index of the stack - the index of the previous greater element
TC -> O(2N), SC -> O(N)
"""