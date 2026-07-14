# mypy: disable-error-code="empty-body"
# QUESTION: Maximal Rectangle
# Given a binary matrix (of '0'/'1' characters), find the largest rectangle
# containing only 1s and return its area.
# Example 1:
# Input: matrix = [["1","0","1","0","0"],
#                  ["1","0","1","1","1"],
#                  ["1","1","1","1","1"],
#                  ["1","0","0","1","0"]]
# Output: 6
# Explanation: The bottom-middle block of 1s forms a rectangle of area 6.
# Constraints:
# 1 <= rows, cols <= 200
# matrix[i][j] is '0' or '1'.

"""
#Optimal Approach:
1. Build a running "histogram" per row: for each column keep a prefix sum of
   consecutive 1s from the top, resetting to 0 whenever a 0 is hit. Row i's
   pseudo-array is the histogram of column heights ending at that row.
2. For every row, run Largest Rectangle in Histogram on its pseudo-array.
3. The answer is the maximum histogram area across all rows.
TC -> O(N*M) to build + O(N*M) for the row histograms = O(N*M), SC -> O(N*M)

#KEY INSIGHT:
- A rectangle of 1s ending at row i is exactly a bar in the column-height
  histogram of that row, so the 2D problem reduces to N applications of the 1D
  largest-rectangle-in-histogram solution.
"""


class Solution:
    def largestRectangleInHistogram(self, arr: list[int]) -> int:
        st: list[int] = []
        maxi = 0
        for index in range(len(arr)):
            while st and arr[index] <= arr[st[-1]]:
                element = arr[st.pop()]
                pse = -1 if not st else st[-1]
                nse = index
                maxi = max(maxi, (nse - pse - 1) * element)
            st.append(index)
        while st:
            element = arr[st.pop()]
            pse = -1 if not st else st[-1]
            nse = len(arr)
            maxi = max(maxi, (nse - pse - 1) * element)
        return maxi

    def findSolution(self, matrix: list[list[str]]) -> int:
        maxi = 0
        n = len(matrix)
        m = len(matrix[0])
        pseudoArray = [[0 for _ in range(m)] for _ in range(n)]
        for j in range(m):
            total = 0
            for i in range(n):
                total += int(matrix[i][j])
                if int(matrix[i][j]) == 0:
                    total = 0
                pseudoArray[i][j] = total
        for i in range(n):
            maxi = max(maxi, self.largestRectangleInHistogram(pseudoArray[i]))
        return maxi


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(Solution().findSolution(matrix))
