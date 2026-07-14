# mypy: disable-error-code="empty-body"
# QUESTION: Sum of Subarray Ranges
# The range of a subarray is (max element - min element). Return the sum of all
# subarray ranges of the given array.
# Example 1:
# Input: arr = [4, -2, -3, 4, 1]
# Output: 59
# Explanation: Sum over every contiguous subarray of (max - min) equals 59.
# Constraints:
# 1 <= n <= 1000
# -10^9 <= arr[i] <= 10^9

"""
#Brute Force:
1. Enumerate all subarrays, track running max and min, and add (max - min) for
   each subarray to the total.
TC -> O(N^2), SC -> O(1)

#Optimal Approach:
1. Sum of ranges = (sum of subarray maximums) - (sum of subarray minimums).
2. Sum of minimums: each arr[i] is the min of (i - PSEE) * (NSE - i) subarrays.
3. Sum of maximums: each arr[i] is the max of (i - PGEE) * (NGE - i) subarrays,
   found with the same monotonic-stack pattern but reversed comparisons.
4. Answer is maxSum - minSum.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- Decomposing range into max-contribution minus min-contribution lets the
  subarray-minimums monotonic-stack trick be reused twice, turning O(N^2) into
  O(N).
"""


class Solution:
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

    def findNGE(self, arr: list[int]) -> list[int]:
        stack: list[int] = []
        nge = [0 for _ in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] >= arr[stack[-1]]:
                stack.pop()
            nge[i] = stack[-1] if stack else len(arr)
            stack.append(i)
        return nge

    def findPGEE(self, arr: list[int]) -> list[int]:
        stack: list[int] = []
        pgee = [0 for _ in range(len(arr))]
        for i in range(len(arr)):
            while stack and arr[i] > arr[stack[-1]]:
                stack.pop()
            pgee[i] = stack[-1] if stack else -1
            stack.append(i)
        return pgee

    def findSolution(self, arr: list[int]) -> int:
        minSum, maxSum = 0, 0
        mod = int(1e9 + 7)
        nse = self.findNSE(arr)
        psee = self.findPSEE(arr)
        nge = self.findNGE(arr)
        pgee = self.findPGEE(arr)
        for i in range(len(arr)):
            left1 = i - psee[i]
            right1 = nse[i] - i
            left2 = i - pgee[i]
            right2 = nge[i] - i
            minSum += (((right1 * left1) % mod) * arr[i]) % mod
            maxSum += (((right2 * left2) % mod) * arr[i]) % mod
        return int(maxSum - minSum)


if __name__ == "__main__":
    print(Solution().findSolution([4, -2, -3, 4, 1]))
