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

  def findSolution1(self, arr:List[int]):
    resp = set()
    for i in range(len(arr)):
      for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
          if (arr[i] + arr[j] + arr[k] == 0):
            resp.add(tuple(sorted([arr[i], arr[j], arr[k]])))
    ans = [list(item) for item in resp]
    return ans

  def findSolution2(self, arr:List[int]):
    resp = set()

    for i in range(len(arr)):
      temp = set()
      for j in range(i+1, len(arr)):
        remove = -(arr[i] + arr[j])
        if (remove in temp):
          resp.add(tuple(sorted([arr[i], arr[j], remove])))
        temp.add(arr[j])
      
    ans = [list(item) for item in resp]
    return ans

  def findSolution(self, arr:List[int]):
    resp = []
    arr.sort()

    for i in range(0, len(arr)):
      if (i > 0 and arr[i] == arr[i-1]): continue
      j, k = i+1, len(arr) - 1
      while (j < k):
        sum = arr[i] + arr[j] + arr[k]
        if (sum < 0): j += 1
        elif (sum > 0): k -= 1
        else:
          resp.append([arr[i], arr[j], arr[k]])
          j += 1
          k -= 1
          while (j < k and arr[j] == arr[j-1]): j += 1
          while (j < k and arr[k] == arr[k+1]): k -= 1
    return resp

if __name__ == "__main__":
  arr = [-1,0,1,2,-1,-4]
  resp = Solution().findSolution(arr)
  print(resp)


"""
3 Sum

Brute Force:
1. First, we will declare a set data structure as we want unique triplets.
2. Then we will use the first loop(say i) that will run from 0 to n-1.
3. Inside it, there will be the second loop(say j) that will run from i+1 to n-1.
4. Then there will be the third loop(say k) that runs from j+1 to n-1.
5. Now, inside these 3 nested loops, we will check the sum i.e. arr[i]+arr[j]+arr[k], 
and if it is equal to the target i.e. 0 we will sort this triplet and insert it in the set data structure.
6. Finally, we will return the list of triplets stored in the set data structure.
TC -> O(N**3 * log(no. of unique triplets)), SC -> O(2 * no. of the unique triplets)

Better:
1. First, we will declare a set data structure as we want unique triplets.
2. Then we will use the first loop(say i) that will run from 0 to n-1.
3. Inside it, there will be the second loop(say j) that will run from i+1 to n-1.
4. Before the second loop, we will declare another HashSet to store the array elements 
as we intend to search for the third element using this HashSet.
5. Inside the second loop, we will calculate the value of the third element i.e. -(arr[i]+arr[j]).
6. If the third element exists in the HashSet, we will sort these 3 values i.e. arr[i], arr[j], and the third element, 
and insert it in the set data structure declared in step 1.
7. After that, we will insert the j-th element i.e. arr[j] in the HashSet as we only want to insert those array elements
that are in between indices i and j.
8. Finally, we will return a list of triplets stored in the set data structure.
TC -> O(N**2 * log(no. of unique triplets)), SC -> O(2 * no. of the unique triplets) + O(N)

Optimal (Three Pointer Approach):
1. Sort The Array
2. Take Three Pointers i will run from 0 to n-1, j will start from i+1 and k will be n - 1
3. First Check if current i value is same as last one if yes continue
4. Run a loop while j < k
5. Calculate Sum by adding all elements
6. If Sum is Less Than K increment j Pointer 
7. If Sum is Greater Than K decrement k Pointer
8. If Sum is Equal to K append to answer and increment j and decrement k pointer
9. Run two loops and increment j and decrement k till same elements are encountered
TC -> O(NlogN)+O(N**2), SC -> O(no. of triplets)
"""