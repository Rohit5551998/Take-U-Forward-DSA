# QUESTION: Merge K Sorted Arrays
# You are given k sorted arrays, each of size k. Merge all the arrays
# into one sorted array and return it.
# You should use an efficient algorithm. The expected time complexity is
# O(k^2 log k) — equivalently O(N log k) where N is the total number of
# elements across all arrays.
#
# Examples:
# Example 1:
# Input: k = 3, arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Example 2:
# Input: k = 2, arrays = [[1, 4, 7], [2, 5, 8]]
# Output: [1, 2, 4, 5, 7, 8]
#
# Constraints:
# 1 <= k <= 100
# Each array has size k.
# -10^9 <= array[i][j] <= 10^9
#
# Optimal approach: use a min-heap of size k. Push the first element of
# each array into the heap (with array index + position). Pop the min,
# append to result, push the next element from the same array. Repeat
# until the heap is empty.


"""
(N = total elements across all arrays = k * k = k^2 for this problem.)

#Brute Force:
1. Ignore the fact that the arrays are already sorted — just collect everything
   into one flat list by walking every array and appending every element.
2. Sort that combined list once at the end. Correctness is trivial (a global
   sort can't be wrong), but it throws away the free ordering the inputs already
   have, so it does more comparisons than necessary.
TC -> O(N log N), SC -> O(N)

#Better Approach:
1. Use the sortedness: merge the arrays two at a time with the classic
   two-pointer merge (merge_two_sorted_arrays), which walks both inputs once and
   emits the smaller head each step — O(len(a) + len(b)) per merge.
2. Fold left across the arrays: start the accumulator as arrays[0], then merge
   in arrays[1], arrays[2], ... one by one, each producing a new larger sorted
   list.
3. Why it's only "better", not optimal: the accumulator keeps growing, and every
   merge re-copies all elements seen so far. Merging in the i-th array touches
   ~i*k elements, so the total is k + 2k + 3k + ... + k*k = O(k * N) = O(k^3).
   The early elements get copied k times over.
TC -> O(N * k) = O(k^3), SC -> O(N)

#Optimal Approach:
1. The wasteful part of "better" is re-copying already-merged elements. Avoid it
   by never materializing intermediate merges — instead, at every step know the
   single global minimum among the *current fronts* of all k arrays, and emit it.
2. A MIN-HEAP gives that global minimum in O(log k). Seed it with the FIRST
   element of each non-empty array, stored as a tuple (value, array_no, index)
   so that after popping a value you know exactly which array it came from and
   where you were in it.
3. Repeatedly pop the smallest tuple: append its value to the output (it is the
   next element in the fully-merged order, since every array is sorted and the
   heap holds the frontier of unconsumed heads).
4. After popping from array `array_no` at position `index`, push that array's
   NEXT element (index + 1) if it exists. This keeps the heap holding at most one
   "front" per array — size <= k at all times.
5. Stop when the heap empties: every element of every array has been popped
   exactly once. Tuples compare by value first, so ties are broken by array_no
   deterministically without extra work.
6. Cost: N total pops/pushes, each an O(log k) heap op (heap never exceeds k
   entries). So O(N log k) time and O(k) heap space (plus O(N) for the output),
   beating better's O(N*k).
TC -> O(N log k), SC -> O(k) heap (+ O(N) output)

#KEY INSIGHT:
- Don't merge pairwise and recopy — keep a min-heap of just the k current array
  heads (value, array_no, index). Popping the min gives the next merged element
  in O(log k), and pushing that array's successor keeps the heap at size <= k, so
  the whole merge is O(N log k) instead of O(N*k).
"""

import heapq
from typing import List


class Solution:
    def merge_k_sorted_arrays_brute(self, arrays: List[List[int]]) -> List[int]:
        output: List[int] = []
        if arrays:
            output = []
            for array in arrays:
                for element in array:
                    output.append(element)
            output.sort()
        return output

    def merge_two_sorted_arrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                output.append(nums1[i])
                i += 1
            else:
                output.append(nums2[j])
                j += 1

        while i < len(nums1):
            output.append(nums1[i])
            i += 1

        while j < len(nums2):
            output.append(nums2[j])
            j += 1

        return output

    def merge_k_sorted_arrays_better(self, arrays: List[List[int]]) -> List[int]:
        output = []
        if arrays:
            output = arrays[0]
            for i in range(1, len(arrays)):
                output = self.merge_two_sorted_arrays(output, arrays[i])
        return output

    def merge_k_sorted_arrays_optimal(self, arrays: List[List[int]]) -> List[int]:
        output: List[int] = []
        heap: List[tuple[int, int, int]] = []

        for i in range(0, len(arrays)):
            array = arrays[i]
            if len(array) > 0:
                heapq.heappush(heap, (array[0], i, 0))

        while heap:
            val, array_no, index = heapq.heappop(heap)
            output.append(val)
            if index + 1 < len(arrays[array_no]):
                heapq.heappush(heap, (arrays[array_no][index + 1], array_no, index + 1))

        return output


if __name__ == "__main__":
    sol = Solution()
    arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.merge_k_sorted_arrays_brute(arrays))
    arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.merge_k_sorted_arrays_better(arrays))
    arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sol.merge_k_sorted_arrays_optimal(arrays))
