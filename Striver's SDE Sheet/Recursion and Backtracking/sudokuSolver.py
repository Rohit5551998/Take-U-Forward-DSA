# mypy: disable-error-code="empty-body"
# QUESTION: Sudoku Solver
# Create a program that fills in the blank cells in a Sudoku puzzle to solve it.
# Every sudoku solution needs to follow these guidelines:
# 1) In every row, the numbers 1 through 9 must appear exactly once.
# 2) In every column, the numbers 1 through 9 must appear exactly once.
# 3) In each of the grid's nine 3x3 sub-boxes, the numbers 1 through 9 must appear exactly once.
# Empty cells are indicated by the '.' character. Fill the board in-place.
#
# Examples:
# Example 1:
# Input: board =
# [["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]]
# Output:
# [["5","3","4","6","7","8","9","1","2"],
#  ["6","7","2","1","9","5","3","4","8"],
#  ["1","9","8","3","4","2","5","6","7"],
#  ["8","5","9","7","6","1","4","2","3"],
#  ["4","2","6","8","5","3","7","9","1"],
#  ["7","1","3","9","2","4","8","5","6"],
#  ["9","6","1","5","3","7","2","8","4"],
#  ["2","8","7","4","1","9","6","3","5"],
#  ["3","4","5","2","8","6","1","7","9"]]
# Explanation: All empty cells are filled so that every row, every column and every 3x3 sub-box
# contains each of the digits 1 through 9 exactly once. This is the only valid solution for the
# given board.
#
# Constraints:
# - board.length = 9
# - board[i].length = 9
# - board[i][j] is a digit or '.'
# - It is guaranteed that input board has only one solution.


"""
#Brute Force (is_valid_brute + sudoku_solver_brute):
1. Scan the grid for the FIRST empty cell ('.'). Everything before it is already
   consistently filled, so we only ever decide one undecided cell at a time.
2. For that cell try each digit num in 1..9 as a candidate.
3. Before writing, is_valid_brute checks all three Sudoku constraints for num at
   (row, col) in a single 0..8 SCAN:
   - row clash:  board[row][i] == num for any column i.
   - col clash:  board[i][col] == num for any row i.
   - box clash:  board[3*(row//3) + i//3][3*(col//3) + i%3] == num. The
     3*(row//3) / 3*(col//3) snaps to the top-left corner of this cell's 3x3
     box, and i//3, i%3 walk the 9 cells inside it.
4. If num is valid, place it and RECURSE to solve the rest of the board. If that
   recursive call returns True, a full solution was found — propagate True up
   immediately (the puzzle is guaranteed to have exactly one solution).
5. If the recursion fails, undo the write (reset to '.') and try the next digit —
   this is the backtrack that lets a wrong early guess be retracted.
6. If NO digit 1..9 works for this cell, return False so the caller backtracks.
7. If the scan finds no empty cell at all, every cell is filled consistently, so
   return True — this is the base case that ends the recursion.
8. Why this is the BRUTE tier: every validity test re-SCANS the row, column and
   box in O(9). That repeated linear scan on each candidate is exactly the cost
   the optimal tier eliminates with O(1) lookups.
TC -> O(9^(n*n)), SC -> O(n*n) recursion depth (n = 9; board is edited in place)
   (each empty cell branches up to 9 ways; ~n*n empty cells in the worst case)

#Better Approach:
SKIPPED — no middle tier. Sudoku goes from the O(9)-scan validity check (brute)
straight to O(1) hash-set / bitmask validity checks (optimal); nothing sensible
sits between them.

#Optimal Approach (sudoku_solver_optimal + solve_sudoku):
1. Same cell-by-cell backtracking as brute, but replace the O(9) per-candidate
   SCAN with O(1) membership tests. Keep three lists of SETS: rowList[r],
   colList[c] and gridList[g] — each set holds the digits already used in that
   row / column / 3x3 box.
2. CRITICAL SEED STEP: before recursing, walk the initial board once and add
   every pre-filled clue to all three sets. Without this the solver is blind to
   the givens and places digits that collide with them (rows/cols/boxes go wrong
   even though the clue cells themselves are untouched).
3. Box id from a cell: g = 3*(row//3) + (col//3), mapping (row,col) to 0..8.
4. Recurse to the first empty cell. A digit num is placeable iff
   num not in rowList[row] and num not in colList[col] and num not in gridList[g]
   — one O(1) test, no scanning.
5. On placing num: write it to the board and add it to all three sets, then
   recurse; if the recursive call returns True, propagate True up immediately.
6. Backtrack: reset the cell to '.' and remove num from all three sets so sibling
   branches see a clean state.
7. If no digit fits the cell, return False; if no empty cell remains, the grid is
   complete — return True.
TC -> O(9^(n*n)), SC -> O(n*n) for the three sets + O(n*n) recursion
   (same exponential search tree as brute; the win is O(1) validity vs O(9) scan)

#KEY INSIGHT:
- Trade a little space (row/col/box "used-digit" sets) for time: each safety
  check becomes an O(1) `num not in set` test instead of re-scanning 27 cells.
  The make-or-break detail is SEEDING those sets from the board's clues first —
  otherwise the fast check silently ignores the givens and yields an invalid grid.
- NOTE: this only cuts the per-node COST, not the node COUNT. The cell order is
  still top-left-first, so adversarial puzzles can still blow up; an MRV heuristic
  (branch on the empty cell with the fewest candidates) would fix that.
"""

from typing import List


class Solution:
    def is_valid_brute(self, board: List[List[str]], row: int, col: int, num: str) -> bool:
        ans = True
        for i in range(0, 9):
            # Check in row
            if board[row][i] == num:
                ans = False
                break

            # Check in col
            if board[i][col] == num:
                ans = False
                break

            # Check in 3x3 grid
            if board[3 * (row // 3) + (i // 3)][3 * (col // 3) + (i % 3)] == num:
                ans = False
                break
        return ans

    def sudoku_solver_brute(self, board: List[List[str]]) -> bool:
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == ".":
                    for num in range(1, 10):
                        if self.is_valid_brute(board, row, col, str(num)):
                            board[row][col] = str(num)
                            if self.sudoku_solver_brute(board) == True:
                                return True
                            board[row][col] = "."

                    return False
        return True

    def sudoku_solver_better(self, board: List[List[str]]) -> None:
        # SKIP: no middle tier — the O(9)-scan validity check (brute) goes straight
        # to O(1) hash-set / bitmask validity checks (optimal); nothing between.
        pass

    def solve_sudoku(
        self,
        board: List[List[str]],
        rowList: List[set],
        colList: List[set],
        gridList: List[set],
    ) -> bool:
        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == ".":
                    for num in range(1, 10):
                        gridId = (row // 3) * 3 + (col // 3)
                        if (
                            num not in rowList[row]
                            and num not in colList[col]
                            and num not in gridList[gridId]
                        ):
                            board[row][col] = str(num)
                            rowList[row].add(num)
                            colList[col].add(num)
                            gridList[gridId].add(num)
                            if self.solve_sudoku(board, rowList, colList, gridList) == True:
                                return True
                            board[row][col] = "."
                            rowList[row].remove(num)
                            colList[col].remove(num)
                            gridList[gridId].remove(num)

                    return False
        return True

    def sudoku_solver_optimal(self, board: List[List[str]]) -> None:
        rowList: List[set] = [set() for _ in range(len(board))]
        colList: List[set] = [set() for _ in range(len(board))]
        gridList: List[set] = [set() for _ in range(len(board))]

        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] != ".":
                    num = int(board[row][col])
                    gridId = 3 * (row // 3) + (col // 3)
                    rowList[row].add(num)
                    colList[col].add(num)
                    gridList[gridId].add(num)

        self.solve_sudoku(board, rowList, colList, gridList)


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol.sudoku_solver_brute(board)
    for row in board:
        print("".join(row))
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    sol.sudoku_solver_optimal(board)
    for row in board:
        print("".join(row))
