# QUESTION: Flood-fill Algorithm
# An image is represented by an m x n integer grid `image` where each
# integer represents the pixel value of the image. You are also given
# three integers sr, sc, and color. You should perform a "flood fill" on
# the image starting from the pixel image[sr][sc].
# To perform a flood fill:
#   1. Begin with the starting pixel and change its color to `color`.
#   2. Perform the same process for each pixel that is directly
#      4-connected (up/down/left/right) to the starting pixel and shares
#      the SAME original color as the starting pixel.
#   3. Repeat the process by changing the color of those pixels and
#      then their connected neighbors with the same original color, and so on.
#   4. Return the modified image after performing the flood fill.
#
# Examples:
# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center, all 4-connected pixels with the original
# color (1) are recolored to 2.
#
# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already color 0; no change.
#
# Constraints:
# m == image.length, n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m, 0 <= sc < n


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


def flood_fill_algorithm_brute() -> None:
    pass


def flood_fill_algorithm_better() -> None:
    pass


def flood_fill_algorithm_optimal() -> None:
    pass
