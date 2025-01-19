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
    spaces = 2*n-2
    for i in range(1, 2*n):
      stars = i;
      #spaces = 2*(n-i)
      if (stars>n):
        stars = 2*n-i
      for j in range(1, stars+1):
        print("*", end=" ")

      for j in range(1, spaces+1):
        print(" ", end=" ")

      for j in range(1, stars+1):
        print("*", end=" ")

      if (i < n): spaces -= 2
      else: spaces += 2
      print("")


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  Solution().findSolution(n)


"""
*                 * 
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *

[number, space, number]
[1, 6, 1]
[2, 4, 2]
[3, 2, 3]
[4, 0, 4]
"""