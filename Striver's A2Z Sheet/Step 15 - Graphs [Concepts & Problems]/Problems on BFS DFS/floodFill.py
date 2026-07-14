# mypy: disable-error-code="empty-body"
# QUESTION: Flood Fill
# You are given an image represented as an m x n integer grid, where image[i][j]
# is the pixel value (colour) at position (i, j). You are also given a starting
# pixel (sr, sc) and a new colour newColor.
# Perform a flood fill: starting from the pixel (sr, sc), change the colour of
# that pixel and of every pixel that is connected to it 4-directionally (up,
# down, left, right) and shares the same original colour, to newColor. Continue
# this process for all such connected pixels.
# Return the modified image.
#
# Example 1:
# Input: image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr = 1, sc = 1, newColor = 2
# Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
# Explanation: Starting from the centre pixel (value 1), all 4-directionally
# connected pixels of value 1 are recoloured to 2. The bottom-right 1 is not
# connected to the region and stays unchanged.
#
# Constraints:
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], newColor < 2^16
# 0 <= sr < m
# 0 <= sc < n

"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""

from typing import List


class Solution:
    def floodFill_brute(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        pass

    def floodFill_better(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        pass

    def floodFill_optimal(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.floodFill_optimal([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
