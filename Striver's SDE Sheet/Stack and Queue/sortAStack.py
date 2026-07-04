# mypy: disable-error-code="empty-body"
# QUESTION: Sort a Stack
# You are given a stack of integers. Your task is to sort the stack in descending order using
# recursion, such that the top of the stack contains the greatest element and the bottom contains
# the smallest. You are not allowed to use any explicit loop constructs or any additional data
# structure — only the standard stack operations (push, pop, top, isEmpty) and recursion (the
# implicit call stack) may be used.
#
# Examples:
# Example 1:
# Input: stack (bottom -> top) = [4, 1, 3, 2]
# Output: stack (bottom -> top) = [1, 2, 3, 4]
# Explanation: After sorting, the greatest element (4) is at the top of the stack, and the
# smallest (1) is at the bottom.
#
# Example 2:
# Input: stack (bottom -> top) = [1]
# Output: stack (bottom -> top) = [1]
# Explanation: A single-element stack is already sorted.


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
    def sort_a_stack_brute(self, stack: List[int]) -> List[int]:
        pass

    def sort_a_stack_better(self, stack: List[int]) -> List[int]:
        pass

    def sort_a_stack_optimal(self, stack: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    stack = [4, 1, 3, 2]
    print(sol.sort_a_stack_optimal(stack))
