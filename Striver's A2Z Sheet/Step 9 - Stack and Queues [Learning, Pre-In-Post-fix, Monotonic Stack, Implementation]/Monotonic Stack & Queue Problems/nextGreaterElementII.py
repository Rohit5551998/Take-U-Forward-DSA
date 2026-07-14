# mypy: disable-error-code="empty-body"
# QUESTION: Next Greater Element II
# Given a circular array, find the next greater element for every index. The
# search wraps around to the start of the array. If none exists, answer is -1.
# Example 1:
# Input: arr = [1, 2, 1]
# Output: [2, -1, 2]
# Explanation: For the last 1 the search wraps to the front and finds 2.
# Constraints:
# 1 <= n <= 10^4
# -10^9 <= arr[i] <= 10^9

"""
#Brute Force:
1. For each index i, scan the next n-1 positions (using i % n) for a strictly
   greater element; record it, else -1.
TC -> O(N^2), SC -> O(N)

#Optimal Approach:
1. Simulate the circular array by iterating i from 2n-1 down to 0 and indexing
   with arr[i % n], maintaining a decreasing monotonic stack.
2. Pop all stack values <= current; the top (if any) is the next greater element.
3. Only record the answer when i < n (the real, first pass over each index).
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- Doubling the traversal with modulo indexing lets a single monotonic-stack pass
  handle the wrap-around without physically duplicating the array.
"""


class Solution:
    def findSolution(self, arr: list[int]) -> list[int]:
        n = len(arr)
        stack: list[int] = []
        ans = [0 for _ in range(n)]
        for i in range(2 * n - 1, -1, -1):
            while stack and arr[i % n] >= stack[-1]:
                stack.pop()
            if i < n:
                ans[i] = -1 if not stack else stack[-1]
            stack.append(arr[i % n])
        return ans


if __name__ == "__main__":
    print(Solution().findSolution([1, 2, 1]))
