# mypy: disable-error-code="empty-body"
# QUESTION: Book Allocation Problem
# Given arr where arr[i] is the number of pages in book i, and m students, allocate
# all books to students such that: each student gets a contiguous block, every
# student gets at least one book, and every book is allocated. Minimize the maximum
# number of pages assigned to any student. Return -1 if m > number of books.
# Example 1:
# Input: arr = [25,46,28,49,24], m = 4
# Output: 71
# Explanation: The optimal split gives a maximum load of 71 pages.
# Constraints:
# 1 <= len(arr) <= 10^5
# 1 <= arr[i] <= 10^6

"""
#Brute Force:
1. If m > n return -1. The answer lies in [max(arr), sum(arr)].
2. For each candidate max-pages from max to sum, greedily count students needed
   (start a new student when the running load would exceed the candidate).
3. Return the first candidate needing exactly m (>= m) students.
TC -> O((sum - max + 1) * N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search on the max-pages is the improvement.

#Optimal Approach:
1. If m > n return -1.
2. Students-needed is monotone non-increasing as the allowed max-pages grows, so
   "students(x) <= m" is monotone. Binary search x in [max(arr), sum(arr)].
3. If students(mid) <= m, mid is feasible; record it and try smaller (high = mid-1).
4. Else mid too small -> low = mid + 1.
TC -> O(N * log(sum - max)), SC -> O(1)

#KEY INSIGHT:
- Raising the per-student page limit can only reduce the number of students
  required, giving a monotone predicate we binary search to minimize the maximum.
"""

from typing import List


class Solution:
    def _students(self, arr: List[int], max_pages: int) -> int:
        students = 1
        load = 0
        for pages in arr:
            if load + pages <= max_pages:
                load += pages
            else:
                students += 1
                load = pages
        return students

    def book_allocation_brute(self, arr: List[int], m: int) -> int:
        if m > len(arr):
            return -1
        for x in range(max(arr), sum(arr) + 1):
            if self._students(arr, x) <= m:
                return x
        return -1

    def book_allocation_better(self, arr: List[int], m: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def book_allocation_optimal(self, arr: List[int], m: int) -> int:
        if m > len(arr):
            return -1
        low, high = max(arr), sum(arr)
        ans = high
        while low <= high:
            mid = low + (high - low) // 2
            if self._students(arr, mid) <= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.book_allocation_optimal([25, 46, 28, 49, 24], 4))
