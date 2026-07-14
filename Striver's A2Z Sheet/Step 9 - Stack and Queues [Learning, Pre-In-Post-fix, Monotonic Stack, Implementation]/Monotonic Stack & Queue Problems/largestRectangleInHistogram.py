# mypy: disable-error-code="empty-body"
# QUESTION: Largest Rectangle in Histogram
# Given an array of bar heights (each of width 1), find the area of the largest
# rectangle that fits entirely within the histogram.
# Example 1:
# Input: arr = [2, 1, 5, 6, 2, 3]
# Output: 10
# Explanation: Bars of heights 5 and 6 form a 2x5 rectangle of area 10.
# Constraints:
# 1 <= n <= 10^5
# 0 <= arr[i] <= 10^4

"""
#Brute Force:
1. For each bar treat it as the minimum height and expand left/right while bars
   are >= it, tracking the widest span; area = span * height.
TC -> O(N^2), SC -> O(1)

#Better Approach:
1. Precompute the Next Smaller Element (right boundary) and Previous Smaller
   Element (left boundary) index for each bar with two monotonic-stack passes.
2. Width for bar i is (nse[i] - psee[i] - 1); area = width * arr[i]. Take the max.
TC -> O(N), SC -> O(N)

#Optimal Approach:
1. Single pass with an increasing monotonic stack of indices. When the current
   bar is <= the top, pop it: the popped bar's height, with right boundary = i
   and left boundary = new stack top (or -1), gives a candidate area.
2. After the scan, drain the stack using right boundary = n for the remaining bars.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- When a bar is popped, we know both its nearest smaller neighbours (i on the
  right, the new top on the left), so its maximal rectangle is finalized on the
  spot — a single pass computes every candidate area.
"""


class Solution:
    def findNSE(self, arr: list[int]) -> list[int]:
        st: list[int] = []
        ans = [0 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            while st and arr[i] <= arr[st[-1]]:
                st.pop()
            ans[i] = len(arr) if not st else st[-1]
            st.append(i)
        return ans

    def findPSEE(self, arr: list[int]) -> list[int]:
        st: list[int] = []
        ans = [0 for _ in range(len(arr))]
        for i in range(len(arr)):
            while st and arr[i] < arr[st[-1]]:
                st.pop()
            ans[i] = -1 if not st else st[-1]
            st.append(i)
        return ans

    def findSolution1(self, arr: list[int]) -> int:
        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)
        maxi = 0
        for i in range(len(arr)):
            maxi = max(maxi, (nse[i] - psee[i] - 1) * arr[i])
        return maxi

    def findSolution(self, arr: list[int]) -> int:
        st: list[int] = []
        maxi = 0
        for i in range(len(arr)):
            while st and arr[i] <= arr[st[-1]]:
                # The popped element's rectangle is bounded by i (next smaller)
                # on the right and the new stack top (previous smaller) on the left.
                element = arr[st.pop()]
                pse = -1 if not st else st[-1]
                nse = i
                maxi = max(maxi, (nse - pse - 1) * element)
            st.append(i)
        while st:
            element = arr[st.pop()]
            pse = -1 if not st else st[-1]
            nse = len(arr)
            maxi = max(maxi, (nse - pse - 1) * element)
        return maxi


if __name__ == "__main__":
    print(Solution().findSolution([2, 1, 5, 6, 2, 3]))
