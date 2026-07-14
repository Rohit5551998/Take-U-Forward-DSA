# mypy: disable-error-code="empty-body"
# QUESTION: Sort a stack using recursion
# Given a stack, sort it using recursion. You are NOT allowed to use any loop
# constructs (like while/for) — only recursion. Use of an extra auxiliary stack
# is also disallowed; the recursion call stack is the only extra space.
# Example 1:
# Input: stack = [11, 2, 32, 3, 41] (top is 41)
# Output: [41, 32, 11, 3, 2] (top is 2, i.e. sorted ascending from bottom to top)
# Explanation: After sorting, the smallest element is on top.
# Constraints:
# 1 <= stack size <= 100
# -100 <= element <= 100

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
    def sort_stack_brute(self, stack: List[int]) -> List[int]:
        pass

    def sort_stack_better(self, stack: List[int]) -> List[int]:
        pass

    def sort_stack_optimal(self, stack: List[int]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.sort_stack_optimal([11, 2, 32, 3, 41]))
