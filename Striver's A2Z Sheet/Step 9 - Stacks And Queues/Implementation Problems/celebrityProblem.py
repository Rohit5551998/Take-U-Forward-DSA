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
  def findSolution1(self, matrix):
    row = [0] * len(matrix)
    col = [0] * len(matrix[0])
    ans = -1

    for i in range(len(matrix)):
      for j in range(len(matrix[0])):
        if matrix[i][j] == 1:
          row[i] += 1
          col[j] += 1
    
    for i in range(len(matrix)):
      if (row[i] == 1 and col[i] == len(matrix)):
        ans = i
        break

    return ans
  
  def findSolution(self, matrix):
    top = 0
    down  = len(matrix) - 1

    while top < down:
      if (matrix[top][down] == 1):
        top += 1
      elif (matrix[down][top] == 1):
        down -= 1
      else:
        top += 1
        down -= 1

    ans = top
    for i in range(len(matrix)):
      if (i == ans): continue

      if (matrix[ans][i] != 0 or matrix[i][ans] != 1):
        ans = -1
        break
    return ans

if __name__ == "__main__":
  matrix = [[1, 1, 0],
            [0, 1, 0],
            [0, 1, 1]]
  print(Solution().findSolution(matrix))

"""
Celebrity Problem
Better Approach
1. Initialize row, col arrays, ans to -1 and run two loops on array & increment row and col arrays if 1 is found respectively
2. Now loop through rows and check if row[i] is 1 and col[i] is n, if it is then return i as celebrity else return -1.
TC -> O(N**2) + O(N), SC -> O(2N)

Optimal Approach
1. Assign top = 0, down = n-1 and run while loop till top < down with condition if mat[top][down] == 1(top knows down) top += 1
2. Else if mat[down][top] == 1(down knows top), down -= 1 else top += 1, down -= 1
3. At end of loop top is probable ans run another loop to check this scenario and continue if ans == i
4. Inside loop if at any point mat[ans][i] != 0 or mat[i][ans] != 1 then assign ans = 1 and break out of loop to return ans
TC -> O(2N), SC -> O(1)
"""