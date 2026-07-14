# mypy: disable-error-code="empty-body"
# QUESTION: The Celebrity Problem
# In a party of n people, a celebrity is someone known by everyone but who knows
# nobody. Given an n x n matrix M where M[i][j] == 1 means person i knows person
# j, return the index of the celebrity, or -1 if there is none.
# Example 1:
# Input: matrix = [[1, 1, 0],
#                  [0, 1, 0],
#                  [0, 1, 1]]
# Output: 1
# Explanation: Person 1 is known by 0 and 2 but knows nobody else.
# Constraints:
# 2 <= n <= 3000
# M[i][j] is 0 or 1; M[i][i] may be 1 (self-known) and is ignored.

"""
#Better Approach:
1. Count knowsCount[i] (row sum) and knownByCount[j] (column sum) for every person.
2. A celebrity is someone with knownByCount == n (excluding self) and knowsCount
   consistent with knowing nobody; scan for the matching index.
TC -> O(N^2), SC -> O(N)

#Optimal Approach:
1. Two pointers top=0, down=n-1. If M[top][down] == 1, top knows down so top
   can't be the celebrity -> top++. Else down knows top... actually if
   M[down][top] == 1 then down knows top so down-- ; if neither, both are
   eliminated (top++, down--).
2. When top == down, that is the only celebrity candidate.
3. Verify the candidate: it must know nobody (row all 0 except self) and be known
   by everybody (column all 1 except self); otherwise return -1.
TC -> O(N) to find + O(N) to verify, SC -> O(1)

#KEY INSIGHT:
- Each comparison eliminates at least one non-celebrity, so a single linear scan
  narrows n candidates to one, which is then verified in another linear pass.
"""


class Solution:
    def findSolution1(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        row = [0] * n
        col = [0] * len(matrix[0])
        ans = -1
        for i in range(n):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        for i in range(n):
            if row[i] == 1 and col[i] == n:
                ans = i
                break
        return ans

    def findSolution(self, matrix: list[list[int]]) -> int:
        top = 0
        down = len(matrix) - 1
        while top < down:
            if matrix[top][down] == 1:
                top += 1
            elif matrix[down][top] == 1:
                down -= 1
            else:
                top += 1
                down -= 1
        ans = top
        for i in range(len(matrix)):
            if i == ans:
                continue
            if matrix[ans][i] != 0 or matrix[i][ans] != 1:
                ans = -1
                break
        return ans


if __name__ == "__main__":
    matrix = [[1, 1, 0], [0, 1, 0], [0, 1, 1]]
    print(Solution().findSolution(matrix))
