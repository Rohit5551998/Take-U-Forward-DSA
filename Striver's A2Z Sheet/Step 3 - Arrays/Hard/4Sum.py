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

  def findSolution1(self, arr:List[int], n: int):
    resp = set()
    for i in range(len(arr)):
      for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
          for l in range(k+1, len(arr)):
            if (arr[i] + arr[j] + arr[k] + arr[l] == n):
              resp.add(tuple(sorted([arr[i], arr[j], arr[k], arr[l]])))
    ans = [list(item) for item in resp]
    return ans

  def findSolution2(self, arr:List[int], n: int):
    resp = set()

    for i in range(0, len(arr)):
      for j in range(i+1, len(arr)):
        temp = set()
        for k in range(j+1, len(arr)):
          remove = n - (arr[i] + arr[j] + arr[k])
          if (remove in temp):
            resp.add(tuple(sorted([arr[i], arr[j], arr[k], remove])))
          temp.add(arr[k])
      
    ans = [list(item) for item in resp]
    return ans

  def findSolution(self, arr:List[int], n: int):
    resp = []
    arr.sort()

    for i in range(0, len(arr)):
      if (i > 0 and arr[i] == arr[i-1]): continue
      else:
        for j in range(i+1, len(arr)):
          if (j > i + 1 and arr[j] == arr[j-1]): continue
          else:
            k, l = j + 1, len(arr) - 1
            while (k < l):
              sum = arr[i] + arr[j] + arr[k] + arr[l]
              if (sum < n): k += 1
              elif (sum > n): l -= 1
              else:
                resp.append([arr[i], arr[j], arr[k], arr[l]])
                k += 1
                l -= 1
                while (k < l and arr[k] == arr[k-1]): k += 1
                while (k < l and arr[l] == arr[l+1]): l -= 1
    return resp

if __name__ == "__main__":
  arr = [-1,0,1,2,-1,-4]
  resp = Solution().findSolution(arr, 0)
  print(resp)


"""
4 Sum

Brute Force:
1. First, we will declare a set data structure as we want unique quadruplets.
2. Then we will use the first loop(say i) that will run from 0 to n-1.
3. Inside it, there will be the second loop(say j) that will run from i+1 to n-1.
4. Then there will be the third loop(say k) that runs from j+1 to n-1.
5. Inside loop k, the fourth loop(say l) will run from k+1 to n-1.
6. Now, inside these four nested loops, we will check the sum i.e. arr[i]+arr[j]+arr[k]+arr[l], and if it is equal to the target we will sort this quadruplet and insert it in the set data structure.
7. Finally, we will return a list of stored quadruplets.
TC -> O(N**4), SC -> O(2 * no. of the unique quadruplets)

Better:
1. First, we will declare a set data structure as we want unique quadruplets.
2. Then we will use the first loop(say i) that will run from 0 to n-1.
3. Inside it, there will be the second loop(say j) that will run from i+1 to n-1.
4. Before the third loop, we will declare a HashSet to store the specific array elements as we intend to search the fourth element in that HashSet.
5. Then there will be the third loop(say k) that runs from j+1 to n-1.
6. Inside the third loop, we will calculate the value of the fourth element i.e. target - (nums[i]+nums[j]+nums[k]).
7. If the fourth element exists in the HashSet, we will sort these four values i.e. nums[i], nums[j], nums[k], and the fourth element, and insert it in the set data structure declared in step 1.
8. After that, we will insert the k-th element i.e. nums[k] in the HashSet as we only want to insert those array elements that are in between indices j and k.
9. Finally, we will return a list of stored quadruplets stored in the set data structure.
TC -> O(N**3 * log(no. of unique triplets)), SC -> O(2 * no. of the unique triplets) + O(N)

Optimal (Three Pointer Approach):
1. First, we will sort the entire array.
2. We will use a loop(say i) that will run from 0 to n-1. This i will represent one of the fixed pointers. In each iteration, this value will be fixed for all different values of the rest of the 3 pointers. Inside the loop, we will first check if the current and the previous element is the same and if it is we will do nothing and continue to the next value of i.
3. After checking inside the loop, we will introduce another fixed pointer j(runs from i+1 to n-1) using another loop. Inside this second loop, we will again check for duplicate elements and only perform any further operation if the elements are different.
4. Inside the second loop, there will be 2 moving pointers i.e. k(starts from j+1) and l(starts from the last index). The pointer k will move forward and the pointer l will move backward until they cross each other while the value of i and j will be fixed.
5. Now we will check the sum i.e. nums[i]+nums[j]+nums[k]+nums[l].
If the sum is greater, then we need lesser elements and so we will decrease the value of l.
If the sum is lesser than the target, we need a bigger value and so we will increase the value of k. 
If the sum is equal to the target, we will simply insert the quad i.e. nums[i], nums[j], nums[k], and nums[l] into our answer and move the pointers k and l skipping the duplicate elements(i.e. by checking the adjacent elements while moving the pointers).
6. Finally, we will have a list of unique quadruplets.
TC -> O(N**3), SC -> O(no. of quadruplets)
"""