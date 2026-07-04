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
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""

from typing import List


class Solution:
    def allocate_minimum_number_of_pages_brute(self, books: List[int], m: int) -> int:
        pass

    def allocate_minimum_number_of_pages_better(self, books: List[int], m: int) -> int:
        pass

    def allocate_minimum_number_of_pages_optimal(self, books: List[int], m: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    books = [12, 34, 67, 90]
    m = 2
    print(sol.allocate_minimum_number_of_pages_optimal(books, m))
