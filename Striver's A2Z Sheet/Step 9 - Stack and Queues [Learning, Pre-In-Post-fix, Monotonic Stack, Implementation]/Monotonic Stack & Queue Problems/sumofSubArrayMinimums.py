# mypy: disable-error-code="empty-body"
# QUESTION: Sum of Subarray Minimums
# Given an array of integers, return the sum of min(b) for every contiguous
# subarray b. Since the answer can be large, return it modulo 10^9 + 7.
# Example 1:
# Input: arr = [11, 81, 94, 43, 3]
# Output: 444
# Explanation: Sum of the minimums of all contiguous subarrays modulo 1e9+7.
# Constraints:
# 1 <= n <= 3 * 10^4
# 1 <= arr[i] <= 3 * 10^4

"""
#Brute Force:
1. Enumerate all subarrays with two nested loops, tracking the running minimum,
   and add each subarray's minimum to the total.
TC -> O(N^2), SC -> O(1)

#Optimal Approach:
1. Every element arr[i] is the minimum of exactly (left * right) subarrays, where
   left = distance to the Previous Smaller-or-Equal Element and right = distance
   to the Next Smaller Element.
2. Compute PSEE indices (strict smaller on the left, using < so ties are counted
   once) and NSE indices (smaller-or-equal on the right, using <=) with two
   monotonic-stack passes.
3. Contribution of arr[i] is left * right * arr[i]; sum all contributions mod 1e9+7.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- Counting how many subarrays each element dominates as the minimum (via nearest
  smaller boundaries) replaces the O(N^2) enumeration; the strict/non-strict
  boundary choice avoids double counting equal elements.
"""


class Solution:
    def findSolution1(self, arr: list[int]) -> int:
        import math

        total = 0.0
        for i in range(len(arr)):
            mini = math.inf
            for j in range(i, len(arr)):
                mini = min(mini, arr[j])
                total += mini % (1e10 + 7)
        return int(total)

    def findNSE(self, arr: list[int]) -> list[int]:
        stack: list[int] = []
        nse = [0 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            nse[i] = stack[-1] if stack else len(arr)
            stack.append(i)
        return nse

    def findPSEE(self, arr: list[int]) -> list[int]:
        stack: list[int] = []
        psee = [0 for _ in range(len(arr))]
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            psee[i] = stack[-1] if stack else -1
            stack.append(i)
        return psee

    def findSolution(self, arr: list[int]) -> int:
        mod = int(1e9 + 7)
        total = 0
        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)
        for i in range(len(arr)):
            left = i - psee[i]
            right = nse[i] - i
            total += (((right * left) % mod) * arr[i]) % mod
            total %= mod
        return total


if __name__ == "__main__":
    print(Solution().findSolution([11, 81, 94, 43, 3]))
