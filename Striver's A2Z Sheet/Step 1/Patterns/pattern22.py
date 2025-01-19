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
    for i in range(0, 2*n-1):
      for j in range(0, 2*n-1):
        # print(min(i,j, 2*n-1-(i+1), 2*n-1-(j+1)), " ", end=" ")
        print(n-min(i,j, 2*n-1-(i+1), 2*n-1-(j+1)), " ", end=" ")
      print("")


if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  Solution().findSolution(n)


"""
Initial: (Minimum Distance From Each Side)
0   0   0   0   0   0   0   
0   1   1   1   1   1   0
0   1   2   2   2   1   0
0   1   2   3   2   1   0
0   1   2   2   2   1   0
0   1   1   1   1   1   0
0   0   0   0   0   0   0

Final:
4   4   4   4   4   4   4   
4   3   3   3   3   3   4
4   3   2   2   2   3   4
4   3   2   1   2   3   4
4   3   2   2   2   3   4
4   3   3   3   3   3   4
4   4   4   4   4   4   4
"""