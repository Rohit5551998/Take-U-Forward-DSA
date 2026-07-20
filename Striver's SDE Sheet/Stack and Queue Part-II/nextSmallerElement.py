# mypy: disable-error-code="empty-body"
# QUESTION: Next Smaller Element
# Given an array of integers arr, find the Next Smaller Element (NSE) for every element in the
# array. The Next Smaller Element of an element x is the first element to the right of x in the
# array that is strictly smaller than x. If no such element exists, the answer for x is -1.
# Return an array where the i-th value is the NSE of arr[i].
#
# Examples:
# Example 1:
# Input: arr = [4, 8, 5, 2, 25]
# Output: [2, 5, 2, -1, -1]
# Explanation:
# - For 4, the first smaller element to its right is 2.
# - For 8, the first smaller element to its right is 5.
# - For 5, the first smaller element to its right is 2.
# - For 2, no smaller element exists to its right -> -1.
# - For 25, there is no element to its right -> -1.
#
# Example 2:
# Input: arr = [10, 9, 8, 7]
# Output: [9, 8, 7, -1]
# Explanation: The array is strictly decreasing, so each element's immediate right neighbour is
# its next smaller element; the last element has nothing to its right -> -1.


"""
#Brute Force:
1. For each index i, the answer is the FIRST element to its right that is smaller.
   So scan rightward from i+1 and take the first arr[j] < arr[i].
2. Initialize the whole answer array to -1 (the default for "no smaller element
   exists"), so if the inner scan finds nothing we already have the right value.
3. On the first j with arr[j] < arr[i], record it and break — we want the NEAREST
   smaller, not the smallest. Worst case (strictly increasing array) every inner
   scan runs to the end -> quadratic.
TC -> O(n^2), SC -> O(n) for the output

#Better Approach:
SKIPPED — no meaningful middle tier. The problem jumps from the O(n^2) rightward
scan straight to the O(n) monotonic-stack solution; there is no sensible
in-between (e.g. sorting destroys the positional "nearest on the right" info).

#Optimal Approach:
1. Process the array RIGHT to LEFT, maintaining a stack of "candidates" — the
   elements to the right of i that could still be someone's next-smaller. The
   stack is kept INCREASING from bottom to top (mirror of the NGE decreasing
   stack).
2. For index i, pop everything >= arr[i] (condition arr[i] <= top). Those popped
   elements can never be the NSE of i or of anything further left, because arr[i]
   sits between them and the left and is <= them — arr[i] "blocks" them. Each
   element is pushed once and popped at most once, keeping total work linear.
3. After popping, if the stack is non-empty its top is the nearest element to the
   right that is strictly smaller than arr[i] -> that's nse[i]. If the stack is
   empty, nothing to the right is smaller, so nse[i] stays -1.
4. Push arr[i] itself: it is now a candidate NSE for elements still to its left.
5. Note on the <= comparison: popping EQUAL values (not just larger) is essential
   because the NSE must be STRICTLY smaller, so an equal element is not a valid
   answer and must be discarded — using < here (leaving equals) is the classic
   bug that mis-reports an equal element as the NSE.
TC -> O(n) (each element pushed/popped once), SC -> O(n) stack + O(n) output

#KEY INSIGHT:
- Scan right-to-left with a monotonic (increasing) stack: pop everything the
  current element dominates from below (>= it, so blocked and useless as future
  answers), and whatever survives on top is exactly the nearest strictly-smaller
  element. Amortized O(1) per element since each is pushed and popped at most once.
"""

from queue import LifoQueue
from typing import List


class Solution:
    def next_smaller_element_brute(self, arr: List[int]) -> List[int]:
        nse = [-1] * len(arr)

        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    nse[i] = arr[j]
                    break
        return nse

    def next_smaller_element_better(self, arr: List[int]) -> List[int]:
        # SKIP: no meaningful middle tier — the problem goes straight from the
        # O(n^2) rightward scan to the O(n) monotonic stack, with nothing sensible
        # in between.
        pass

    def next_smaller_element_optimal(self, arr: List[int]) -> List[int]:
        nse = [-1] * len(arr)
        st: LifoQueue[int] = LifoQueue()

        for i in range(len(arr) - 1, -1, -1):
            while not st.empty() and arr[i] <= st.queue[-1]:
                st.get()

            if not st.empty():
                nse[i] = st.queue[-1]

            st.put(arr[i])
        return nse


if __name__ == "__main__":
    sol = Solution()
    arr = [4, 8, 5, 2, 25]
    print(sol.next_smaller_element_brute(arr))
    arr = [4, 8, 5, 2, 25]
    print(sol.next_smaller_element_optimal(arr))
