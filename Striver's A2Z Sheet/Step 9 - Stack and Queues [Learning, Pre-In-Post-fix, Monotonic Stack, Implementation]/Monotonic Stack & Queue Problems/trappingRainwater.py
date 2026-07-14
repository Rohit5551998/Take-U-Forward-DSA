# mypy: disable-error-code="empty-body"
# QUESTION: Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of
# each bar is 1, compute how much water it can trap after raining.
# Example 1:
# Input: arr = [4, 2, 0, 3, 2, 5]
# Output: 9
# Explanation: Water is trapped in the dips between taller bars, totalling 9.
# Constraints:
# 1 <= n <= 2 * 10^4
# 0 <= arr[i] <= 10^5

"""
#Brute Force:
1. For each index i compute leftMax (max height to its left including i) and
   rightMax (max to its right including i) by scanning both directions.
2. Water at i is min(leftMax, rightMax) - arr[i]; sum over all i.
TC -> O(N^2), SC -> O(1)

#Better Approach:
1. Precompute prefix leftMax[] and suffix rightMax[] arrays in two passes.
2. Water at i is min(leftMax[i], rightMax[i]) - arr[i]; sum over all i.
TC -> O(N), SC -> O(N)

#Optimal Approach:
1. Two pointers left=0, right=n-1 with running leftMax and rightMax.
2. Move the pointer on the smaller side inward: that side's max is the binding
   constraint, so if the current bar is below the running max, add the
   difference as trapped water; otherwise update the running max.
TC -> O(N), SC -> O(1)

#KEY INSIGHT:
- Water above a bar depends on min(leftMax, rightMax). Advancing the smaller
  side guarantees that side's max is final, so trapped water can be counted in
  one pass with O(1) memory.
"""


class Solution:
    def findSolution1(self, arr: list[int]) -> int:
        n = len(arr)
        totalTrapped = 0
        for i in range(n):
            leftMax = 0
            rightMax = 0
            j = i
            while j >= 0:
                leftMax = max(leftMax, arr[j])
                j -= 1
            j = i
            while j < n:
                rightMax = max(rightMax, arr[j])
                j += 1
            totalTrapped += min(leftMax, rightMax) - arr[i]
        return totalTrapped

    def findSolution2(self, arr: list[int]) -> int:
        n = len(arr)
        totalTrapped = 0
        leftMax = [0 for _ in range(n)]
        rightMax = [0 for _ in range(n)]
        leftMax[0], rightMax[n - 1] = arr[0], arr[n - 1]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], arr[i])
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], arr[i])
        for i in range(n):
            totalTrapped += min(leftMax[i], rightMax[i]) - arr[i]
        return totalTrapped

    def findSolution(self, arr: list[int]) -> int:
        leftMax = 0
        rightMax = 0
        totalTrapped = 0
        left = 0
        right = len(arr) - 1
        while left < right:
            if arr[left] <= arr[right]:
                if arr[left] < leftMax:
                    totalTrapped += leftMax - arr[left]
                else:
                    leftMax = arr[left]
                left += 1
            else:
                if arr[right] < rightMax:
                    totalTrapped += rightMax - arr[right]
                else:
                    rightMax = arr[right]
                right -= 1
        return totalTrapped


if __name__ == "__main__":
    print(Solution().findSolution([4, 2, 0, 3, 2, 5]))
