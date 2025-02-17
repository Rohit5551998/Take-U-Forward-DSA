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
  def findSolution1(self, row: int, col: int):
    ans, n, r = 1, row-1, col-1
    for i in range(0, r+1):
      ans *= (n - i);
      ans /= (i+1);
    return (int)(ans)
  
  def findSolution2(self, n: int):
    temp = [1]
    ans = 1    
    for i in range(1, n):
      ans *= (n-i)
      ans /= (i)
      temp.append((int)(ans))
    return temp
  
  def findSolution(self, n: int):
    ans = []
    for i in range(1, n+1):
      ans.append(self.findSolution2(i))
    return ans

if __name__ == "__main__":
  resp = Solution().findSolution1(5, 3)
  print(resp)
  print(Solution().findSolution2(5))
  print(Solution().findSolution(5))


"""
Pascal Triangle:

a. Variant 1 -> Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.
Use Formula nCr with n = r-1 and r = c-1
Naive Approach: Calculate n!/(r! * (n-r)!) TC ->  O(n)+O(r)+O(n-r).
Optimal Approach: 
1. Skip (n-r)! and eliminate the same from numerator
2. Run a loop till r calculating numerator and denomiator as (n-i)/(i+1)
TC -> O(c), SC -> O(1)


b. Variant 2 -> Given the row number n. Print the n-th row of Pascal’s triangle.
Naive Approach: Use Variant 1 Optimal Approach to Generate All Elements of nth row
Optimal Approach: 
1. Start with ans = 1
2. Run a loop from 1 to n-1. 
3. Multiply by (n-i) and divide by i to get next elements of row
TC -> O(n), SC -> O(1)


c. Variant 3 -> Given the number of rows n. Print the first n rows of Pascal’s triangle.
1. Run a loop till required no of rows
2. Use Variant 2 Optimal Approach to generate all elements of the mentioned row.
TC -> O(n**2), SC -> O(1)
"""