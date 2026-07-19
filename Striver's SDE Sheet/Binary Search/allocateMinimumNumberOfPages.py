# mypy: disable-error-code="empty-body"
# QUESTION: Allocate Minimum Number of Pages
# Given an array 'arr' of integer numbers, arr[i] represents the number of
# pages in the i-th book. There are 'm' number of students. The task is to
# allocate books to students such that:
#   1. Each student gets at least one book.
#   2. Each book is allocated to only one student.
#   3. Book allocation is contiguous (a student gets a consecutive set of
#      books).
# Allocate books in such a way that the maximum number of pages assigned
# to a student is minimum. Return that minimum value. If allocation is not
# possible (e.g., books < students), return -1.
#
# Examples:
# Example 1:
# Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
# Result: 113
# Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the
# first 3 books and the other will get the last one.
#
# Example 2:
# Input Format: n = 5, m = 4, arr[] = {25, 46, 28, 49, 24}
# Result: 71
# Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.


"""
#Brute Force:
1. Reframe: the answer is a page-limit value — the maximum pages any single
   student is allowed. allocation_possible(limit) greedily hands contiguous
   books to a student until adding the next book would exceed limit, then
   starts a new student; the allocation fits if the students needed <= m.
2. The smallest limit worth trying is max(books) — no student can take fewer
   pages than the single largest book (each book must go somewhere, whole).
   The largest is sum(books) — one student takes everything.
3. Linearly try every limit from max(books) up to sum(books). The FIRST limit
   that is feasible is the minimum possible maximum — so record it and break.
   (Guard m <= n: can't give every student a book otherwise -> -1.)
TC -> O((sum-max) * N), SC -> O(1)

#Better Approach:
SKIPPED — no meaningful middle tier. Brute linearly scans every candidate
page-limit; optimal binary-searches it. Nothing sensible sits between the two.

#Optimal Approach:
1. Same reframing and same allocation_possible greedy as brute — the answer is
   a page-limit, and feasibility is monotonic: if a limit works, every larger
   limit also works (more slack per student). So feasible limits form a suffix
   [ans .. sum(books)], which binary search can pinpoint.
2. Set the search space to the limit's range: low = max(books) (no limit can be
   below the largest single book) and high = sum(books) (everything to one
   student). The answer lies in [low, high].
3. Binary search: for each candidate mid limit, run allocation_possible(mid).
4. If mid is feasible, it might be too generous — record it (ans = mid) and try
   to tighten (high = mid - 1). If infeasible, mid is too small, so raise the
   floor (low = mid + 1). The smallest feasible mid is the answer.
5. Guard m <= n as in brute; return -1 when there are fewer books than students.
TC -> O(N * log(sum-max)), SC -> O(1)

#KEY INSIGHT:
- Feasibility is monotonic in the page-limit: a bigger allowance is only ever
  easier to satisfy. So binary search the smallest limit for which a greedy
  contiguous allocation still fits within m students.
"""

from typing import List


class Solution:
    def allocate_minimum_number_of_pages_brute(self, books: List[int], m: int) -> int:
        ans = -1
        if m <= len(books):
            for i in range(max(books), sum(books) + 1):
                if self.allocation_possible(books, m, i):
                    ans = i
                    break
        return ans

    def allocate_minimum_number_of_pages_better(self, books: List[int], m: int) -> int:
        # SKIP: no meaningful middle tier — the brute force linearly scans every
        # candidate page-limit and the optimal binary-searches it; nothing
        # sensible sits between the two.
        pass

    def allocation_possible(self, books: List[int], m: int, maxPages: int) -> bool:
        cnt = 1
        pages = 0
        ans = False

        for i in range(0, len(books)):
            if pages + books[i] <= maxPages:
                pages += books[i]
            else:
                pages = books[i]
                cnt += 1

        if cnt <= m:
            ans = True

        return ans

    def allocate_minimum_number_of_pages_optimal(self, books: List[int], m: int) -> int:
        ans = -1
        if m <= len(books):
            low, high = max(books), sum(books)

            while low <= high:
                mid = low + (high - low) // 2

                if self.allocation_possible(books, m, mid):
                    ans = mid
                    high = mid - 1

                else:
                    low = mid + 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    books = [25, 46, 28, 49, 24]
    m = 4
    print(sol.allocate_minimum_number_of_pages_brute(books, m))
    books = [12, 34, 67, 90]
    m = 2
    print(sol.allocate_minimum_number_of_pages_optimal(books, m))
    books = [25, 46, 28, 49, 24]
    m = 4
    print(sol.allocate_minimum_number_of_pages_optimal(books, m))
