# QUESTION: Rotate matrix by 90 degrees
# Given an N * N 2D integer matrix, rotate the matrix by 90 degrees clockwise. The rotation must be done in place, meaning the input 2D matrix must be modified directly.
#
# Examples:
# Input :matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# Output :matrix = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
#
# Explanation :First, we transpose the matrix: rows become columns. Then, we reverse each row to simulate 90° clockwise rotation. So element at (0,0) goes to (0,2), (0,1) goes to (1,2), and so on, achieving the rotated layout.
#
# Input :matrix = [[0, 1, 1, 2], [2, 0, 3, 1], [4, 5, 0, 5], [5, 6, 7, 0]]
#
# Output :matrix = [[5, 4, 2, 0], [6, 5, 0, 1], [7, 0, 3, 1], [0, 5, 1, 2]]
#
# Explanation :First, the matrix is transposed: rows become columns. Then, each row is reversed. This moves the last column to the first row, the second last column to the second row, and so on. The original position of each element is rotated 90° clockwise into its new location.


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


class Solution:
    def rotate_matrix_by_ninezero_degrees_brute(self) -> None:
        pass

    def rotate_matrix_by_ninezero_degrees_better(self) -> None:
        pass

    def rotate_matrix_by_ninezero_degrees_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
