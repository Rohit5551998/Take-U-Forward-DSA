# mypy: disable-error-code="empty-body"
# QUESTION: LRU Page Faults (Least Recently Used Page Replacement)
# Given a sequence of page references pages and a memory capacity of C frames, simulate
# the Least Recently Used (LRU) page replacement policy. Count and return the total
# number of page faults. A page fault occurs whenever a referenced page is not currently
# in memory; if memory is full, evict the least recently used page to make room.
#
# Example 1:
# Input: pages = [5, 0, 1, 3, 2, 4, 1, 0, 5], C = 4
# Output: 8
# Explanation: Simulating LRU with 4 frames results in 8 page faults.
#
# Constraints:
# 1 <= len(pages) <= 10^4
# 1 <= C <= 10^4
# 0 <= pages[i] <= 10^4

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
    def lru_page_fault_brute(self, pages: List[int], capacity: int) -> int:
        pass

    def lru_page_fault_better(self, pages: List[int], capacity: int) -> int:
        pass

    def lru_page_fault_optimal(self, pages: List[int], capacity: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.lru_page_fault_optimal([5, 0, 1, 3, 2, 4, 1, 0, 5], 4))
