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
    if (n <= 1):
      return 1
    else:
      return n * self.findSolution(n-1)

if __name__ == "__main__":
  n = int(input("Please enter a number: \n"))
  print(Solution().findSolution(n))

  def factorialtillN(self, n, i, response):
    if (response[-1]*i <= n):
      response.append(response[-1]*i)
      self.factorial(n, i+1, response)
    else:
      return
    
  def factorial(self, n):
    if (n <= 1):
      return 1
    else:
      return n * self.factorial(n-1)
  
  def factorialNumbers(self, n):
    #code here 
    response = [1]
    self.factorial(n, 2, response)
    return response


"""
1. Given a number ‘N’, find out the factorial till N 
2. A number n is called a factorial number if it is the factorial of a positive integer. For example, the first few factorial numbers are 1, 2, 6, 24, 120,
Given a number n, the task is to return the list/vector of the factorial numbers smaller than or equal to n.
"""