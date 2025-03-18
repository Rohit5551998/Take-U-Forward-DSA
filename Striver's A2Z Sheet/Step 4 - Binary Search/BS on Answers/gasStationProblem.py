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
  def findSolution1(self, arr: List[int], k:int):
    n = len(arr)
    howMany = [0 for _ in range(n-1)]

    for gasStations in range(1, k+1):
      maxSection, maxIndex = -1, -1
      for i in range(0, n-1):
        difference = arr[i+1] - arr[i]
        sectionLength = difference / ( howMany[i] + 1 )
        if (sectionLength > maxSection):
          maxSection = sectionLength
          maxIndex = i
      howMany[maxIndex] += 1

    maxAns = -1
    for i in range(0, n - 1):
      difference = arr[i+1] - arr[i]
      sectionLength = difference / (howMany[i] + 1)
      maxAns = max(maxAns, sectionLength)
    return maxAns
  
  def findSolution2(self, arr: List[int], k: int):
    n = len(arr)
    howMany = [0 for _ in range(n-1)]
    pq = []

    for i in range(0, n-1):
      heapq.heappush(pq, ((-1) * (arr[i+1]-arr[i]), i))    

    for gasStations in range(1, k+1):
      top = heapq.heappop(pq)
      secInd = top[1]

      howMany[secInd] += 1
      iniDiff = arr[secInd + 1] - arr[secInd]
      newDist = iniDiff / (howMany[secInd] + 1)
      heapq.heappush(pq, ((-1) * newDist, secInd))

    return pq[0][0]*(-1)
  

  def noOfGasStationsRequired(self, arr:List[int], dist):
    n = len(arr)
    cnt = 0
    for i in range(1, n):
      numberInBetween = ((arr[i] - arr[i - 1]) / dist)
      if (arr[i] - arr[i-1]) == (dist * numberInBetween):
        numberInBetween -= 1
      cnt += numberInBetween
    return cnt

  def findSolution(self, arr: List[int], k: int):
    n = len(arr)
    low, high = 0, 0
    for i in range(0, n-1):
      high = max(high, arr[i+1] - arr[i])

    while (high - low > 1e-6):
      mid = (low + high) / 2.0
      cnt = self.noOfGasStationsRequired(arr, mid)
      print(cnt, mid, high)
      if (cnt > k):
        low = mid
      else:
        high = mid

    return high
    


if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  k = 1
  # arr = [1, 2, 3, 4, 5]
  # k = 4
  resp = Solution().findSolution(arr, k)
  print(resp)


"""
Gas Station Problem
Brute Force
1. First, we will declare an array howMany[] of size n-1, to keep track of the number of placed gas stations.
2. Next, using a loop we will pick k gas stations one at a time.
3. Then, using another loop, we will find the index 'i' where the distance (arr[i+1] - arr[i]) is the maximum 
and insert the current gas station between arr[i] and arr[i+1] (i.e. howMany[i]++).
4. Finally, after placing all the new stations, we will find the distance between two consecutive gas stations. 
For a particular section,
distance = section_length / (number_of_stations_ inserted+1)
    = (arr[i+1]-arr[i]) / (howMany[i]+1)
5. Among all the distances, the maximum one will be the answer.
TC -> O(k*n) + O(n), SC -> O(n - 1)

Better Approach
1. First, we will declare an array howMany[] of size n-1, to keep track of the number of placed gas stations 
and a priority queue that uses max heap.
2. We will insert the first n-1 indices with the respective distance value, arrr[i+1]-arr[i] for every index.
3. Next, using a loop we will pick k gas stations one at a time. Then we will pick the first element of the priority queue
as this is the element with the maximum distance. Lets call the index secInd.
4. Now we will place the current gas station at secInd(howMany[secInd]++) and calculate the new section length,
new_section_length = initial_section_length / (number_of_stations_ inserted+1)
            = (arr[secInd+1] - arr[secInd]) / (howMany[i] + 1)
5. After that, we will again insert the pair <new_section_length, secInd> into the priority queue 
for further consideration.
6. After performing all the steps for k gas stations, the distance at the top of the priority queue 
will be the answer as we want the maximum distance.
TC -> O(nlogn + klogn), SC -> O(n-1) + O(n-1)

Optimal Approach
1. Initialize two pointers low = 0, high = max(dist)
2. In loop calculate mid = low + high / 2.0
3. while(low <= high): The condition 'while(low <= high)' inside the 'while' loop won't work for decimal answers, 
and using it might lead to a TLE error. To avoid this, we can modify the condition to 'while(high - low > 10^(-6))'. 
This means we will only check numbers up to the 6th decimal place. Any differences beyond this decimal precision won't 
be considered, as the question explicitly accepts answers within 10^-6 of the actual answer.
4. low = mid+1: We have used this operation to eliminate the left half. But if we apply the same here, we might ignore 
several decimal numbers and possibly our actual answer. So, we will use this: low = mid.
5. high = mid-1: Similarly, We have used this operation to eliminate the right half. But if we apply the same here, 
we might ignore several decimal numbers and possibly the actual answer. So, we will use this: high = mid.

numberOfGasStationsRequired(dist, arr[]): 
6. We will use a loop(say i) that will run from 1 to n. For each section between i and i-1, we will do the following:
No. of stations = (arr[i]-arr[i-1]) / dist
7. Let's keep in mind a crucial edge case: if the section_length (arr[i] - arr[i-1]) is completely divisible by 'dist', 
the actual number of stations required will be one less than what we calculate.
if (arr[i]-arr[i-1] == (No. of stations*dist): No. of stations -= 1.
8. Now, we will add the no. of stations regarding all the sections and the total will be the answer.
TC -> O(n*log(Len)) + O(n), SC -> O(1)
"""