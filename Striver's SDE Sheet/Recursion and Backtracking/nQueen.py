# mypy: disable-error-code="empty-body"
# QUESTION: N Queen
# The n-queens puzzle is the problem of placing n queens on an n × n
# chessboard such that no two queens attack each other (no two queens
# share the same row, column, or diagonal).
# Given an integer n, return all distinct solutions to the n-queens
# puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space,
# respectively.
#
# Examples:
# Example 1:
# Input: n = 4
# Output: [[".Q..", "...Q", "Q...", "..Q."],
#          ["..Q.", "Q...", "...Q", ".Q.."]]
# Explanation: There are exactly two distinct solutions to the 4-queens
# puzzle.
#
# Example 2:
# Input: n = 1
# Output: [["Q"]]
#
# Constraints:
# 1 <= n <= 9
#
# Approach: backtracking. Place a queen in a row, then recurse to the
# next row. Track conflicting columns and both diagonals (via column
# index and (row+col) / (row-col+n) markers) to prune.
#
# Examples:
# Input: N = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown below
#
# Input : N = 1
# Output: [["Q"]]
# Explanation : There is only one way to place 1 queen on 1x1 chessboard.


"""
#Brute Force (is_valid_brute + place_queens_brute + n_queen_brute):
1. Fill the board COLUMN BY COLUMN, left to right. Placing exactly one queen per
   column automatically guarantees no two queens share a column, so that whole
   class of conflicts is handled for free by the loop structure.
2. At column `col`, try every row 0..n-1 as a candidate square for this column's
   queen, and only commit if is_valid_brute says the square is safe so far.
3. Safety only needs to look LEFT: since columns to the right are still empty,
   the sole threats come from queens already placed in columns < col. So the
   check scans three directions to the left — same row, upper-left diagonal,
   lower-left diagonal — and returns False the moment it hits a 'Q'.
4. Each of those three scans walks up to O(n) cells, so one validity check costs
   O(n). This O(n)-per-check scan is exactly what marks this as the BRUTE tier
   (the optimal tier replaces it with O(1) hash-set lookups).
5. If safe, place 'Q' at board[row][col], recurse to col+1 to solve the rest,
   then backtrack by resetting the cell to '.' so the next row can be tried.
6. Base case: when col == n every column has a safe queen, so the board is one
   complete solution — snapshot it by joining each row into a string and append
   a copy to ans (a copy, since board keeps mutating as recursion unwinds).
TC -> O(n! * n), SC -> O(n^2) board + O(n) recursion depth
   (~n! pruned placements, each doing an O(n) validity scan; the n^2 is the grid)

#Better Approach:
SKIPPED — no middle tier. N-Queens goes from the O(n)-scan validity check
(brute) straight to O(1) hash-set validity checks (optimal); there is no sensible
intermediate between them.

#Optimal Approach (place_queens_optimal + n_queen_optimal):
1. Same column-by-column backtracking as brute, but replace the O(n) safety SCAN
   with O(1) lookups. Idea: instead of walking the board to check a square, keep
   three marker arrays that remember which rows/diagonals are already taken.
2. left[row] marks that `row` already holds a queen (we fill columns left→right,
   so a taken row is the "same row to the left" conflict, now a single lookup).
3. Both diagonals become array indices via a constant-along-the-diagonal formula:
   - lower-left diagonal (i+=1, j-=1): row+col stays constant → lower[row+col].
   - upper-left diagonal (i-=1, j-=1): row-col stays constant → upper[(n-1)+(row-col)].
     The +(n-1) offset shifts row-col (which ranges -(n-1)..n-1) into 0..2n-2 so
     it's a valid non-negative index; both diag arrays have size 2n-1.
4. A square (row, col) is safe iff left[row], lower[row+col] and
   upper[(n-1)+(row-col)] are ALL 0 — one O(1) test, no scanning.
5. On placing a queen: set the cell to 'Q' and flip all three markers to 1, then
   recurse to col+1.
6. Backtrack: reset the cell to '.' and flip the same three markers back to 0 so
   sibling branches see a clean state.
7. Base case (col == n): every column is safely filled — join rows into strings
   and append the finished board to ans.
TC -> O(n! * n), SC -> O(n^2) board + O(n) markers + O(n) recursion depth
   (~n! pruned placements; the *n is now only the O(n) row loop / board copy,
    since each validity test itself is O(1) instead of O(n))

#KEY INSIGHT:
- A cell's two diagonals have INVARIANTS: row+col is constant down the ↙ diagonal
  and row-col is constant up the ↖ diagonal. Encoding those (with a +(n-1) shift
  to stay non-negative) turns each safety check into an O(1) array lookup, so the
  expensive per-placement scan of the brute tier disappears entirely.
"""

from typing import List


class Solution:
    def is_valid_brute(self, row: int, col: int, board: List[List[str]], n: int) -> bool:
        # only need to look LEFT: columns >= col are still empty

        # same row, cells to the left
        for i in range(0, col):
            if board[row][i] == "Q":
                return False

        # upper-left diagonal (step up-left: row-col stays constant)
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # lower-left diagonal (step down-left: row+col stays constant)
        i, j = row, col
        while i < n and j >= 0:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1

        return True

    def place_queens_brute(
        self, board: List[List[str]], ans: List[List[str]], n: int, col: int
    ) -> None:
        if col == n:
            temp = ["".join(row) for row in board]
            ans.append(list(temp))
        else:
            # try this column's queen in every row
            for row in range(0, n):
                if self.is_valid_brute(row, col, board, n):
                    board[row][col] = "Q"
                    self.place_queens_brute(board, ans, n, col + 1)
                    board[row][col] = "."

        return

    def n_queen_brute(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        ans = []
        self.place_queens_brute(board, ans, n, 0)
        return ans

    def n_queen_better(self, n: int) -> List[List[str]]:
        # SKIP: no middle tier — N-Queens goes from the O(n)-scan validity check
        # (brute) straight to O(1) hash-set validity checks (optimal).
        pass

    def place_queens_optimal(
        self,
        board: List[List[str]],
        ans: List[List[str]],
        n: int,
        col: int,
        left: List[int],
        upper: List[int],
        lower: List[int],
    ) -> None:
        if col == n:
            temp = ["".join(row) for row in board]
            ans.append(temp)
        else:
            # O(1) safety via markers: row+col keys the lower(↙) diagonal, and
            # (n-1)+(row-col) keys the upper(↖) diagonal (shift keeps it >= 0)
            for row in range(n):
                if left[row] == 0 and lower[row + col] == 0 and upper[(n - 1) + (row - col)] == 0:
                    # place queen + mark its row and both diagonals as occupied
                    board[row][col] = "Q"
                    left[row] = 1
                    lower[row + col] = 1
                    upper[(n - 1) + (row - col)] = 1
                    self.place_queens_optimal(board, ans, n, col + 1, left, upper, lower)
                    # backtrack: unmark so sibling branches start clean
                    board[row][col] = "."
                    left[row] = 0
                    lower[row + col] = 0
                    upper[(n - 1) + (row - col)] = 0
        return

    def n_queen_optimal(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        left = [0 for _ in range(n)]
        upper = [0 for _ in range(2 * n - 1)]
        lower = [0 for _ in range(2 * n - 1)]
        ans = []
        self.place_queens_optimal(board, ans, n, 0, left, upper, lower)
        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 4
    print(sol.n_queen_brute(n))
    n = 4
    print(sol.n_queen_optimal(n))
