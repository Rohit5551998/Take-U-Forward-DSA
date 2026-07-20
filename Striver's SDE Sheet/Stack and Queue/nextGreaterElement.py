# mypy: disable-error-code="empty-body"
# QUESTION: Next Greater Element
# Given an array arr of size n, find the next greater element for each element in the array in
# the order of their appearance. The next greater element of an element in the array is the
# nearest element on the right that is greater than the current element. If there does not exist
# a next greater element for the current element, then the next greater element for that element
# is -1.
#
# Examples:
# Example 1:
# Input: arr = [1, 3, 2, 4]
# Output: [3, 4, 4, -1]
# Explanation: In the array, the next larger element to 1 is 3, for 3 it is 4, for 2 it is 4, and
# for 4 it is -1, since it does not exist.
#
# Example 2:
# Input: arr = [6, 8, 0, 1, 3]
# Output: [8, -1, 1, 3, -1]
# Explanation: The next larger element to 6 is 8; for 8 there is no larger element, hence -1; for
# 0 it is 1; for 1 it is 3; and for 3 there is no larger element on the right, hence -1.
#
# Constraints:
# - 1 <= n <= 10^5
# - 0 <= arr[i] <= 10^9


"""
#Brute Force:
1. For each index i, the answer is the FIRST element to its right that is bigger.
   So just scan rightward from i+1 and take the first arr[j] > arr[i].
2. Initialize the whole answer array to -1 (the default for "no greater element
   exists"), so if the inner scan finds nothing we already have the right value.
3. On the first j with arr[j] > arr[i], record it and break — we only want the
   NEAREST greater, not the largest. Worst case (strictly decreasing array) every
   inner scan runs to the end -> quadratic.
TC -> O(n^2), SC -> O(n) for the output

#Better Approach:
SKIPPED — no meaningful middle tier. The problem jumps from the O(n^2) rightward
scan straight to the O(n) monotonic-stack solution; there is no sensible
in-between (e.g. sorting destroys the positional "nearest on the right" info).

#Optimal Approach:
1. Process the array RIGHT to LEFT, maintaining a stack of "candidates" — the
   elements to the right of i that could still be someone's next-greater. The
   stack is kept DECREASING from bottom to top.
2. For index i, pop everything <= arr[i] (condition arr[i] >= top). Those popped
   elements can never be the NGE of i or of anything further left, because arr[i]
   sits between them and the left and is >= them — arr[i] "blocks" them. This is
   what keeps total work linear: each element is pushed once and popped at most
   once.
3. After popping, if the stack is non-empty its top is the nearest element to the
   right that is strictly greater than arr[i] -> that's nge[i]. If the stack is
   empty, nothing to the right is bigger, so nge[i] stays -1.
4. Push arr[i] itself: it is now a candidate NGE for elements still to its left.
5. Note on the >= comparison: popping equal values (not just smaller) is correct
   because the NGE must be STRICTLY greater, so an equal element is not a valid
   answer and should be discarded.
TC -> O(n) (each element pushed/popped once), SC -> O(n) stack + O(n) output

#KEY INSIGHT:
- Scan right-to-left with a monotonic (decreasing) stack: pop everything the
  current element dominates (they're blocked and useless as future answers), and
  whatever survives on top is exactly the nearest strictly-greater element. Amortized
  O(1) per element because each is pushed and popped at most once.
"""

from queue import LifoQueue
from typing import List


class Solution:
    def next_greater_element_brute(self, arr: List[int]) -> List[int]:
        nge = [-1] * len(arr)

        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] < arr[j]:
                    nge[i] = arr[j]
                    break

        return nge

    def next_greater_element_better(self, arr: List[int]) -> List[int]:
        # SKIP: no meaningful middle tier — the problem goes straight from the
        # O(n^2) rightward scan to the O(n) monotonic stack, with nothing sensible
        # in between.
        pass

    def next_greater_element_optimal(self, arr: List[int]) -> List[int]:
        nge = [-1] * len(arr)
        st: LifoQueue[int] = LifoQueue()

        for i in range(len(arr) - 1, -1, -1):
            while not st.empty() and arr[i] >= st.queue[-1]:
                st.get()

            if not st.empty():
                nge[i] = st.queue[-1]

            st.put(arr[i])

        return nge


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 3, 2, 4]
    print(sol.next_greater_element_brute(arr))
    arr = [1, 3, 2, 4]
    print(sol.next_greater_element_optimal(arr))
