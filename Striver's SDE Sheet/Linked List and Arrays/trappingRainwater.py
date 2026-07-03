# QUESTION: Trapping Rainwater
# Given an array height of n non-negative integers representing an elevation map, where the
# width of each bar is 1, compute how much water can be trapped between the bars after raining.
#
# Examples:
# Example 1:
# Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
# Explanation: The elevation map traps water in the dips between the taller bars: 1 unit above
# index 2 (between walls of height 1 and 2), 4 units above indices 4-6 (between walls of
# height 2 and 3), and 1 unit above index 9 (between walls of height 2 and 2) — 6 units total.
#
# Example 2:
# Input: height = [4, 2, 0, 3, 2, 5]
# Output: 9
# Explanation: Water above each index i is min(max height to its left, max height to its right)
# minus height[i]: index 1 holds 2, index 2 holds 4, index 3 holds 1, index 4 holds 2,
# for a total of 2 + 4 + 1 + 2 = 9 units.
#
# Constraints:
# - n == height.length
# - 1 <= n <= 2 * 10^4
# - 0 <= height[i] <= 10^5


"""
#Brute Force:
1. Water above a bar i is min(tallest wall to its left, tallest wall to its right) - height[i],
   and only when that is positive (a bar taller than one of its walls holds nothing). Compute
   those two walls directly for every index.
2. Sweep i left to right carrying maxLeft = tallest bar strictly left of i (height[0..i-1]).
   Update it incrementally each step: maxLeft = max(maxLeft, height[i-1]). For i = 0 it stays 0.
3. For maxRight, rescan the suffix strictly right of i every iteration: max(height[i+1:]).
   This inner O(n) rescan per index is what makes the whole thing O(n^2). For the last index
   it stays 0.
4. Guard with `height[i] < maxLeft and height[i] < maxRight` before adding min(maxLeft, maxRight)
   - height[i]. This both skips the taller-than-a-wall case and the boundary bars (where a wall
   is 0), so no negative water is ever added.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Water trapped above any index i is decided by the shortest of the two tallest
   walls around it: min(tallest wall to the left, tallest wall to the right) - height[i].
   The brute force recomputes those two maxes by scanning outward for every i (O(n^2));
   here we precompute them once so each lookup is O(1).
2. Build prefixMax[i] = tallest bar in height[0..i]. Walk left to right carrying the
   running max: prefixMax[i] = max(prefixMax[i-1], height[i]). This is the tallest wall
   on the left of (and including) i.
3. Build suffixMax[i] = tallest bar in height[i..n-1] the same way but walking right to
   left: suffixMax[i] = max(suffixMax[i+1], height[i]). This is the tallest wall on the right.
4. For each i, the water it holds is min(prefixMax[i], suffixMax[i]) - height[i]. We only
   add it when height[i] is strictly below BOTH maxes (otherwise the bar itself is a wall
   and traps nothing), then sum these contributions.
5. Two precompute passes + one summing pass, all O(n); the two extra arrays cost O(n) space.
TC -> O(n), SC -> O(n)

#Optimal Approach:
1. Same core idea (water at i = min(leftMax, rightMax) - height[i]), but we avoid the two
   arrays by realizing we only ever need min(leftMax, rightMax). Whichever side is currently
   shorter is the true bottleneck, so we can commit to that side's answer immediately.
2. Put pointers left=0, right=n-1 and running leftMax=rightMax=0. Move the pointer that
   sits on the shorter (or equal) bar inward, since that shorter bar is what limits the water.
3. If height[left] <= height[right]: the left bar is the bottleneck side. If height[left]
   is below leftMax, the gap leftMax - height[left] is trapped water (a taller wall on the
   right is guaranteed to exist, so leftMax alone bounds it); otherwise height[left] becomes
   the new leftMax. Then advance left.
4. Else the right side is the bottleneck: mirror the logic with rightMax and step right inward.
5. Continue until the pointers meet. Each bar is visited once and no auxiliary arrays are
   needed, so we drop the space to O(1) while keeping O(n) time.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Water above a bar depends only on min(tallest-left, tallest-right). Because the shorter
  of the two boundaries is what actually caps the water, the two-pointer method can always
  process the side with the smaller wall right away — its answer can't change later — which
  removes the need to store the full prefix/suffix max arrays.
"""

from typing import List


class Solution:
    def trapping_rainwater_brute(self, height: List[int]) -> int:
        maxLeft = 0
        total = 0

        for i in range(0, len(height)):
            if i > 0:
                maxLeft = max(maxLeft, height[i - 1])

            maxRight = 0
            if i < len(height) - 1:
                maxRight = max(height[i + 1 :])

            if height[i] < maxLeft and height[i] < maxRight:
                total += min(maxLeft, maxRight) - height[i]

        return total

    def trapping_rainwater_better(self, height: List[int]) -> int:
        prefixSum = [0 for _ in range(len(height))]
        suffixSum = [0 for _ in range(len(height))]
        cnt = 0

        prefixSum[0] = height[0]
        suffixSum[len(height) - 1] = height[len(height) - 1]

        for i in range(1, len(height)):
            prefixSum[i] = max(prefixSum[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):
            suffixSum[i] = max(suffixSum[i + 1], height[i])

        for i in range(0, len(height)):
            if height[i] < prefixSum[i] and height[i] < suffixSum[i]:
                cnt += min(prefixSum[i], suffixSum[i]) - height[i]

        return cnt

    def trapping_rainwater_optimal(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        total = 0
        leftMax = 0
        rightMax = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] < leftMax:
                    total += min(leftMax, height[right]) - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    total += min(rightMax, height[left]) - height[right]
                else:
                    rightMax = height[right]
                right -= 1

        return total


if __name__ == "__main__":
    sol = Solution()
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(sol.trapping_rainwater_brute(height))
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(sol.trapping_rainwater_better(height))
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(sol.trapping_rainwater_optimal(height))
