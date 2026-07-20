# QUESTION: Top K Frequent Elements
# Given an integer array `nums` and an integer k, return the k most
# frequent elements. You may return the answer in any order.
#
# Examples:
# Example 1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
# Follow up: Your algorithm's time complexity must be better than
# O(n log n), where n is the array's size.
#
# Approaches:
#   - O(n + u log u): count frequencies with a hashmap, then sort
#     entries by count.
#   - O(n + u log k): count frequencies, then keep a min-heap of size k
#     keyed by frequency.
#   - O(n): count frequencies, then use bucket sort indexed by
#     frequency (buckets of size up to n).


"""
#Brute Force:
1. First count how often each value appears: walk nums once, building hashMap[value] = count.
   This collapses the array into u unique (value, count) entries.
2. To find the most frequent, just fully sort those entries by count in DESCENDING order
   (sorted(..., key=count, reverse=True)). The biggest counts come first.
3. Take the value from each of the first k entries (x[0]) and return them.
4. Correct but wasteful: sorting ALL u uniques costs u log u even though we only need the top
   k — the better/optimal tiers avoid the full sort.
TC -> O(n + u log u), SC -> O(u)   (u = number of unique elements)

#Better Approach:
1. Count frequencies first: walk nums once, building hashMap[value] = count. This is the
   O(n) part every tier shares — after it we only care about the u unique (value, count)
   entries, not the raw array.
2. We only need the k highest counts, so keep a bounded MIN-heap of size k keyed by frequency.
   Storing tuples (count, value) makes heapq order by count automatically (it compares the
   first tuple field), and the min-heap root is the SMALLEST count currently kept — the
   eviction candidate.
3. For each (value, count) push (count, value); whenever the heap exceeds k, pop the root.
   Popping the smallest count guarantees only the k largest-frequency entries survive.
4. After all uniques are processed, the heap holds exactly the k most frequent entries. Strip
   the value out of each tuple (item[1]) and return them; order doesn't matter per the prompt.
5. Why "better", not optimal: each of the u uniques does an O(log k) heap op, so it's
   O(n + u log k) — beats the brute's O(n + u log u) full sort, but bucket sort can reach O(n).
TC -> O(n + u log k), SC -> O(u + k)   (u = number of unique elements)

#Optimal Approach:
1. Count frequencies into hashMap as before — the shared O(n) step.
2. Bucket sort by frequency instead of comparison-sorting. A count can only be between 1 and
   n, so make buckets = a list of n+1 empty lists where the INDEX is a frequency. (Size n+1,
   not n, so that buckets[n] exists for the case where one value fills the whole array.)
3. For each (value, count), append value to buckets[count]. Now all values sharing a frequency
   sit together, positioned by that frequency — no comparisons were ever made.
4. Collect from the HIGH end: walk index from len(buckets)-1 down to 1. Higher index = higher
   frequency, so scanning downward yields values in most-frequent-first order for free.
5. Pop values out of each non-empty bucket into ans, incrementing a counter; the moment cnt
   hits k, return immediately — we've found the k most frequent.
6. Every step is linear (build buckets O(n), scan buckets O(n)), so no log factor at all.
TC -> O(n), SC -> O(n)

#KEY INSIGHT:
- Frequencies are bounded by n, so they can be used directly as array indices — bucket each
  value under its own count and read the buckets from the top down. This replaces the
  sort/heap (log factor) with plain O(n) indexing, because we're ordering by a small bounded
  integer key rather than comparing arbitrary values.
"""

import heapq
from typing import List, Tuple


class Solution:
    def top_k_frequent_elements_brute(self, nums: List[int], k: int) -> List[int]:
        ans = []
        hashMap = {}

        for i in range(0, len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1

        ans = [x[0] for x in sorted(hashMap.items(), reverse=True, key=lambda item: item[1])]
        return ans[0:k]

    def top_k_frequent_elements_better(self, nums: List[int], k: int) -> List[int]:
        ans: List[Tuple[int, int]] = []
        hashMap = {}
        heapq.heapify(ans)

        for i in range(0, len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1

        for key, value in hashMap.items():
            heapq.heappush(ans, (value, key))
            if len(ans) > k:
                heapq.heappop(ans)

        return [item[1] for item in ans]

    def top_k_frequent_elements_optimal(self, nums: List[int], k: int) -> List[int]:
        buckets: List[List[int]] = [[] for _ in range(0, len(nums) + 1)]
        hashMap = {}
        ans = []

        for i in range(0, len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1

        for key, value in hashMap.items():
            buckets[value].append(key)

        cnt = 0

        for index in range(len(buckets) - 1, 0, -1):
            while len(buckets[index]) != 0:
                cnt += 1
                ans.append(buckets[index].pop())
                if cnt == k:
                    return ans
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(sol.top_k_frequent_elements_brute(nums, k))
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(sol.top_k_frequent_elements_better(nums, k))
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(sol.top_k_frequent_elements_optimal(nums, k))
