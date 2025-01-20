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
        reversedNumber = 0;
        negative = False

        if (n < 0):
            negative = True
            n = -n

        while (n > 0):
            lastDigit = n%10
            reversedNumber = reversedNumber*(10) + lastDigit;
            n = int(n/10)

        if (negative):
            reversedNumber = -reversedNumber

        if reversedNumber < -2**31 or reversedNumber > 2**31 - 1:
          reversedNumber = 0

        return reversedNumber 


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  print(Solution().findSolution(n))


"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""