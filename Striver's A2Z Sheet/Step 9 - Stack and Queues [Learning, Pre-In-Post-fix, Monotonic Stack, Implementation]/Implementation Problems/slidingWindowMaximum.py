# mypy: disable-error-code="empty-body"
# QUESTION: Sliding Window Maximum
# Given an array and a window size k, return the maximum of each contiguous
# window of size k as the window slides from left to right.
# Example 1:
# Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Output: [3, 3, 5, 5, 6, 7]
# Explanation: The max of each successive length-3 window.
# Constraints:
# 1 <= k <= n <= 10^5
# -10^4 <= arr[i] <= 10^4

"""
#Brute Force:
1. For each window start compute the max by scanning its k elements.
TC -> O(N*K), SC -> O(1)

#Optimal Approach:
1. Maintain a deque of indices whose values are in decreasing order (a monotonic
   deque); the front always holds the index of the current window's maximum.
2. Before processing i, pop the front if it has slid out of the window
   (front < i - k + 1).
3. Pop from the back while arr[back] <= arr[i] (those can never be a future max),
   then append i.
4. Once i >= k-1, append arr[front] (the window maximum) to the answer.
TC -> O(N), SC -> O(K)

#KEY INSIGHT:
- A decreasing monotonic deque keeps only elements that could still be the
  maximum of some future window, so each index enters and leaves once, giving
  O(N) instead of O(N*K).
"""

from collections import deque


class Solution:
    def findSolution(self, arr: list[int], k: int) -> list[int]:
        dq: deque[int] = deque()
        ans: list[int] = []
        for i in range(len(arr)):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                ans.append(arr[dq[0]])
        return ans


if __name__ == "__main__":
    print(Solution().findSolution([1, 3, -1, -3, 5, 3, 6, 7], 3))
