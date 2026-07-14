# mypy: disable-error-code="empty-body"
# QUESTION: Next Greater Element
# For each element of an array, find the first element to its right that is
# strictly greater. If none exists the answer is -1.
# Example 1:
# Input: arr = [1, 2, 3, 4, 5, 6, 7]
# Output: {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: -1}
# Explanation: Each element's next greater is its right neighbour; 7 has none.
# Constraints:
# 1 <= n <= 10^5
# -10^9 <= arr[i] <= 10^9 (values assumed distinct for the dict mapping)

"""
#Brute Force:
1. For each index i, scan to the right until a strictly greater element is found;
   record it, else record -1.
TC -> O(N^2), SC -> O(N)

#Optimal Approach:
1. Traverse the array from right to left keeping a monotonic (decreasing) stack
   of candidate "greater" values.
2. For each element pop all stack values <= it (they can never be the answer for
   anything to their left once a bigger element appears).
3. The stack top (if any) is the next greater element, else -1; then push the
   current value.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- A decreasing monotonic stack keeps only useful candidates: each element is
  pushed and popped at most once, giving linear time.
"""


class Solution:
    def findSolution1(self, arr: list[int]) -> list[int]:
        stack: list[int] = []
        ans = [0 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            ans[i] = -1 if not stack else stack[-1]
            stack.append(arr[i])
        return ans

    def findSolution(self, arr: list[int]) -> dict[int, int]:
        stack: list[int] = []
        ans: dict[int, int] = {}
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] >= stack[-1]:
                stack.pop()
            ans[arr[i]] = -1 if not stack else stack[-1]
            stack.append(arr[i])
        return ans


if __name__ == "__main__":
    print(Solution().findSolution([1, 2, 3, 4, 5, 6, 7]))
