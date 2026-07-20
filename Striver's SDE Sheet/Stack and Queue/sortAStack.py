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
1. The most intuitive idea: if we could pull everything out into a plain list, sorting
   becomes trivial. So pop every element off the stack one by one and collect them in a
   temporary list `temp` until the stack is empty.
2. Sort `temp` in ascending order using the language's built-in sort (O(n log n)).
3. Push the sorted values back onto the stack left-to-right. Since the smallest is pushed
   first and the largest last, the stack ends up with the greatest element on top — exactly
   the required descending order (bottom -> top ascending).
4. NOTE: this technically breaks the problem's rules (it uses an extra data structure and
   explicit loops), so it's only a baseline for correctness, not an allowed solution. It IS
   faster in raw time than the recursive answer though.
TC -> O(n log n), SC -> O(n)

#Better Approach:
SKIPPED — there is no meaningful middle tier. The sort-into-a-list baseline and the
recursion-only solution are the two natural approaches; nothing distinct sits between them.

#Optimal Approach:
1. Constraint-driven "optimal": we may only use stack ops + the recursion call stack (no
   loops, no extra container). The trick is to let the call stack hold the popped elements.
2. sort(stack): if the stack is empty, it's trivially sorted -> return (base case).
3. Otherwise pop the top into `element` and recursively sort the SMALLER remaining stack
   first. On the way back up the recursion, the stack below is already sorted.
4. Now `element` must be dropped back into its correct place in that sorted stack — this is
   the sub-problem that `insert_into_stack` solves.
5. insert(stack, element): base case — if the stack is empty, or `element` is >= the current
   top (so it belongs on top for descending order), just push it and stop.
6. Otherwise the top is bigger than `element`, so `element` belongs deeper. Pop the top into
   `val`, recursively insert `element` into the now-smaller stack, then push `val` back on
   top of it. This restores the elements we temporarily held on the call stack.
7. Each insert is O(n) in the worst case, and we insert n times -> T(n) = T(n-1) + O(n),
   giving O(n^2). The recursion depth of n gives the O(n) space.
TC -> O(n^2), SC -> O(n)

#KEY INSIGHT:
- The recursion call stack itself is the "extra storage": pop everything down to empty, then
  on the unwind reinsert each held element into its sorted position via insert_into_stack. No
  explicit loop or container is ever used — the two mutually-supporting recursions (sort +
  insert) do all the work.
"""

from typing import List


class Solution:
    def sort_a_stack_brute(self, stack: List[int]) -> None:
        temp = []

        while len(stack) != 0:
            temp.append(stack.pop())

        temp.sort()

        for i in range(0, len(temp)):
            stack.append(temp[i])

    def sort_a_stack_better(self, stack: List[int]) -> None:
        # SKIP: no meaningful middle tier between the sort-into-a-list baseline and the
        # recursion-only solution.
        pass

    def insert_into_stack(self, stack: List[int], element: int) -> None:
        # Base Case: Push into stack if element is greater or stack is empty
        if len(stack) == 0 or element >= stack[-1]:
            stack.append(element)

        # Else since stack top is greater pop the element till top is smaller and at end reinsert it
        else:
            val = stack.pop()
            self.insert_into_stack(stack, element)
            stack.append(val)

    def sort_a_stack_optimal(self, stack: List[int]) -> None:
        if len(stack) == 0:
            return

        element = stack.pop()
        self.sort_a_stack_optimal(stack)
        self.insert_into_stack(stack, element)


if __name__ == "__main__":
    sol = Solution()
    stack = [4, 1, 3, 2]
    sol.sort_a_stack_brute(stack)
    print(stack)
    stack = [4, 1, 3, 2]
    sol.sort_a_stack_optimal(stack)
    print(stack)
