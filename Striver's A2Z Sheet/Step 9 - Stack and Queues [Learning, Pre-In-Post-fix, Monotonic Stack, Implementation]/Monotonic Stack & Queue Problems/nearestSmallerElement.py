# mypy: disable-error-code="empty-body"
# QUESTION: Next Smaller Element
# For each element of an array, find the first element to its right that is
# strictly smaller. If none exists the answer is -1.
# Example 1:
# Input: arr = [39, 27, 11, 4, 24, 32, 32, 1]
# Output: [27, 11, 4, 1, 1, 1, 1, -1]
# Explanation: For index 0 (39) the next smaller to the right is 27, and so on.
# Constraints:
# 1 <= n <= 10^5
# -10^9 <= arr[i] <= 10^9

"""
#Brute Force:
1. For each index i, scan to the right until a strictly smaller element is found;
   record it, else -1.
TC -> O(N^2), SC -> O(N)

#Optimal Approach:
1. Traverse left to right keeping an increasing monotonic stack of candidate
   "smaller" values.
2. For each element pop all stack values >= it, then the stack top (if any) is
   the nearest smaller element; else -1. Push the current value.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- An increasing monotonic stack retains only the values that could still be a
  nearest-smaller answer, so each element is pushed/popped once (linear time).
"""


class Solution:
    def findSolution(self, arr: list[int]) -> list[int]:
        stack: list[int] = []
        ans = [0 for _ in range(len(arr))]
        for i in range(len(arr)):
            while stack and arr[i] <= stack[-1]:
                stack.pop()
            ans[i] = -1 if not stack else stack[-1]
            stack.append(arr[i])
        return ans


if __name__ == "__main__":
    print(Solution().findSolution([39, 27, 11, 4, 24, 32, 32, 1]))
