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

from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

class Solution:
  def findSolution1(self, string):
      maxAns = 0
      if (len(string) != 0):
        for i in range(0, len(string)):
          found = set()
          for j in range(i, len(string)):
            if string[j] in found: 
              break
            else:
              found.add(string[j])
          maxAns = max(maxAns, len(found))
      return maxAns

  def findSolution(self, string):
    maxAns = 0
    l = 0
    r = 0
    found = {}
    if (len(string) != 0):
      while(r < len(string)):
        if (string[r] in found):
          l = max(l, found[string[r]] + 1)
        found[string[r]] = r
        maxAns = max(maxAns, r - l + 1)
        r += 1
    return maxAns

if __name__ == "__main__":
  arr = "abcabcbb"
  # arr = "bbbbb"
  # arr = "pwwkew"
  # arr = "aab"
  print(Solution().findSolution(arr))

"""
Longest Substring Without Repeating Characters
Better Approach
1. If length of string is 0, return 0
2. Run a loop till length of the string and initialize a set to store the characters in the current window
3. Run a nested loop to check if the character is already in the set, if it is then break the inner loop
4. If the character is not in the set, add it to the set
5. At end of inner loop, update the maxAns
6. Return the maxAns
TC -> O(N*N), SC -> O(N)

Optimal Approach
1. If length of string is 0, return 0 and initialize two pointers l and r to 0, maxAns to 0 and found to empty object
2. Run a loop till r is less than length of string
3. If the character is already in dictionary, update left to max of left and found[string[r]] + 1 (to handle case where l is already ahead 
of current duplicate eg: acca ==> at index 3, l should point to 2 not 1)
4. Update found[string[r]] to r, maxAns to max of maxAns and r - l + 1, increment r by 1
5. Return maxAns
TC -> O(N), SC -> O(N)
"""