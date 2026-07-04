# mypy: disable-error-code="empty-body"
# QUESTION: Celebrity Problem
# A celebrity is a person who is known by everyone else at the party but does not know anyone
# in return. Given a square matrix M of size N x N where M[i][j] is 1 if person i knows person
# j, and 0 otherwise, determine if there is a celebrity at the party. Return the index of the
# celebrity or -1 if no such person exists.
# Note that M[i][i] is always 0.
#
# Examples:
# Example 1:
# Input: M = [[0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]]
# Output: 1
# Explanation: Person 1 does not know anyone and is known by persons 0, 2, and 3. Therefore,
# person 1 is the celebrity.
#
# Example 2:
# Input: M = [[0, 1], [1, 0]]
# Output: -1
# Explanation: Both persons know each other, so there is no celebrity.
#
# Constraints:
# 1 <= N <= 3000
# 0 <= M[][] <= 1


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
    def celebrity_problem_brute(self, m: List[List[int]]) -> int:
        pass

    def celebrity_problem_better(self, m: List[List[int]]) -> int:
        pass

    def celebrity_problem_optimal(self, m: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    m = [[0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]]
    print(sol.celebrity_problem_optimal(m))
