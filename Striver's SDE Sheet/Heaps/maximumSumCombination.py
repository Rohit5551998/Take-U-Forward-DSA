# QUESTION: Maximum Sum Combination
# Given two integer arrays nums1 and nums2 (of equal length n) and an
# integer k, return the maximum k valid sum combinations from all
# possible sum combinations, where each sum is formed by picking one
# element from nums1 and one element from nums2 (one of each per pair).
# A sum combination is the sum nums1[i] + nums2[j] for any valid pair of
# indices (i, j). Return the top k such sums in non-increasing order.
#
# Optimal approach: use a max-heap (priority queue). Sort both arrays in
# descending order, then push the top combination (nums1[0]+nums2[0])
# and explore neighbors greedily, using a visited set to avoid
# duplicates.
#
# Examples:
# Input : nums1 = [7, 3], nums2 = [1, 6], k = 2
#  Output : [13, 9]
# Explanation: The 2 maximum combinations are nums1[0] + nums2[1] = 13 and
# nums1[1] + nums2[1] = 9.
#
#  Input : nums1 = [3, 4, 5], nums2 = [2, 6, 3], k = 2
# Output : [11, 10]
# Explanation: The 2 maximum combinations are nums1[2] + nums2[1] = 11 and
# nums1[1] + nums2[1] = 10.


"""
#Brute Force:
1. There are exactly n*n possible pair-sums (one element from nums1 paired with one from
   nums2). The most direct idea is to just materialize every one of them, then pick the top k.
2. Double loop over i in nums1 and j in nums2, appending nums1[i] + nums2[j] to `ans`. After
   both loops `ans` holds all n^2 sums with no structure yet.
3. Sort `ans` in DESCENDING order so the largest sums come first.
4. Slice ans[0:k] — the first k entries are the k maximum sum combinations in non-increasing
   order, exactly what's asked.
5. Wasteful because we build and sort all n^2 sums even though we only keep k; the heap-based
   tiers avoid generating the vast majority of them.
TC -> O(n^2 log n), SC -> O(n^2)   (n^2 sums built, then sorted)

#Better Approach:
1. Same n^2 sums exist, but we don't need to store all of them — only the k largest ever
   matter. So keep a bounded container of size k instead of the whole list.
2. Use a MIN-heap capped at size k. The invariant: the heap always holds the k biggest sums
   seen so far, and its root is the SMALLEST of those k (the weakest survivor / eviction
   candidate).
3. Double loop over every pair, push nums1[i] + nums2[j] onto the heap.
4. After each push, if the heap grew past k, pop the root. That evicts the current smallest,
   so anything smaller than our existing top-k can never linger — memory stays O(k).
5. After all pairs, the heap holds exactly the k largest sums but in heap order. Sort it
   reverse=True to return them non-increasing, as required.
6. Beats brute on space (O(k) vs O(n^2)); still visits all n^2 pairs, so time is only a log
   factor better. The optimal tier avoids visiting most pairs entirely.
TC -> O(n^2 log k), SC -> O(k)

#Optimal Approach:
1. Don't generate all n^2 sums. Sort BOTH arrays descending so index (0,0) — the pairing of
   the two largest elements — is guaranteed the single biggest sum. That's our starting point.
2. Key structural fact: after sorting desc, from any pair (i,j) the only candidates that can
   be "next largest" are its neighbours (i+1, j) and (i, j+1). Moving either index right can
   only shrink the sum, so the next best sum is always adjacent to one already taken.
3. Use a MAX-heap (Python's heapq is a min-heap, so store the NEGATED sum). Each heap entry is
   (-sum, i, j). Seed it with (0,0) and mark (0,0) in a `visited` set.
4. Repeat k times: pop the largest sum, append it (negated back) to result. This is the next
   answer in non-increasing order — the heap always exposes the current best unexplored pair.
5. After popping (i,j), push its two neighbours (i+1,j) and (i,j+1) if in-bounds and not
   already visited. The `visited` set is essential: both (i-1,j) and (i,j-1) would otherwise
   try to add the same pair, so it prevents the same (i,j) entering the heap twice.
6. We only ever expand ~2 pairs per pop, so the heap holds O(k) entries and we do O(k) pops,
   each O(log k). Plus the two sorts. Total O(n log n + k log k) — independent of n^2.
TC -> O(n log n + k log k), SC -> O(k)

#KEY INSIGHT:
- Sort both arrays descending and the pair-sums form a grid where every sum is >= both of its
  right/down neighbours. The k largest can therefore be peeled off greedily with a max-heap
  starting at the top-left (0,0), only ever expanding the frontier of a taken cell — a
  visited set stops the same cell being queued from two directions. No need to build the
  n^2 grid at all.
"""

import heapq
from typing import List, Tuple


class Solution:
    def maximum_sum_combination_brute(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[int]:
        ans = []
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                ans.append(nums1[i] + nums2[j])

        ans.sort(reverse=True)

        return ans[0:k]

    def maximum_sum_combination_better(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[int]:
        ans: List[int] = []
        heapq.heapify(ans)
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                heapq.heappush(ans, nums1[i] + nums2[j])
                if len(ans) > k:
                    heapq.heappop(ans)
        ans.sort(reverse=True)
        return ans

    def maximum_sum_combination_optimal(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[int]:
        visited = set()
        heap: List[Tuple[int, int, int]] = []
        result = []

        nums1.sort(reverse=True)
        nums2.sort(reverse=True)

        heapq.heappush(heap, (-(nums1[0] + nums2[0]), 0, 0))
        visited.add((0, 0))

        for _ in range(0, k):
            total, i, j = heapq.heappop(heap)
            result.append(-total)
            if i + 1 < len(nums1) and (i + 1, j) not in visited:
                heapq.heappush(heap, (-(nums1[i + 1] + nums2[j]), i + 1, j))
                visited.add((i + 1, j))
            if j + 1 < len(nums2) and (i, j + 1) not in visited:
                heapq.heappush(heap, (-(nums1[i] + nums2[j + 1]), i, j + 1))
                visited.add((i, j + 1))
        return result


if __name__ == "__main__":
    sol = Solution()
    nums1 = [7, 3]
    nums2 = [1, 6]
    k = 2
    print(sol.maximum_sum_combination_brute(nums1, nums2, k))
    nums1 = [7, 3]
    nums2 = [1, 6]
    k = 2
    print(sol.maximum_sum_combination_better(nums1, nums2, k))
    nums1 = [7, 3]
    nums2 = [1, 6]
    k = 2
    print(sol.maximum_sum_combination_optimal(nums1, nums2, k))
