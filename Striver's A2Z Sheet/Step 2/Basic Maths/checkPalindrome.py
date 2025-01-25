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


class Solution:
  def findSolution(self, n:int):
        duplicate = n;
        reversedNumber = 0

        response = False
        if (n >= 0):
          while (n > 0):
            lastDigit = n%10
            reversedNumber = reversedNumber*(10) + lastDigit;
            n = int(n/10)

          if (reversedNumber == duplicate): response = True

        return response



if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  print(Solution().findSolution(n))


"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""