# mypy: disable-error-code="empty-body"
# QUESTION: Matrix chain multiplication
# Given a chain of n matrices A1, A2, ..., An, denoted by an array of
# size n+1 where arr[i-1] x arr[i] gives the dimensions of matrix A_i,
# find the minimum number of scalar multiplications needed to multiply
# the chain. You only need to compute the cost, not the actual
# parenthesization.
# Two matrices A (p x q) and B (q x r) can be multiplied in p*q*r
# operations to produce a (p x r) matrix.
#
# Examples:
# Input : [40, 20, 30, 10, 30]
# Output : 26000
# Explanation : Best parenthesization is ( (A1 x (A2 x A3)) x A4 ).
#
# Input : [10, 20, 30, 40, 30]
# Output : 30000
# Explanation : Optimal parenthesization minimizes cost.


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
    def matrix_chain_multiplication_brute(self, dims: List[int]) -> int:
        pass

    def matrix_chain_multiplication_better(self, dims: List[int]) -> int:
        pass

    def matrix_chain_multiplication_optimal(self, dims: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    dims = [40, 20, 30, 10, 30]
    print(sol.matrix_chain_multiplication_optimal(dims))
