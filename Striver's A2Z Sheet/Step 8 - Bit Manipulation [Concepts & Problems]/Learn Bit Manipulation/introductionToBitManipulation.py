# mypy: disable-error-code="empty-body"
# QUESTION: Introduction to Bit Manipulation
# Given a number N and a bit position i (0-indexed from the right), perform three
# fundamental bit operations and return their results:
#   1. Get the i-th bit of N.
#   2. Set the i-th bit of N (make it 1).
#   3. Clear the i-th bit of N (make it 0).
# Example 1:
# Input: N = 13, i = 2   (13 = 1101 in binary)
# Output: getBit = 1, setBit = 13, clearBit = 9
# Explanation:
#   - The 2nd bit of 1101 is 1, so getBit = 1.
#   - Setting the already-set 2nd bit leaves 1101 = 13.
#   - Clearing the 2nd bit gives 1001 = 9.
# Constraints:
# 0 <= N <= 10^9
# 0 <= i <= 31

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

from typing import Tuple


class Solution:
    def bitOps_brute(self, N: int, i: int) -> Tuple[int, int, int]:
        pass

    def bitOps_better(self, N: int, i: int) -> Tuple[int, int, int]:
        pass

    def bitOps_optimal(self, N: int, i: int) -> Tuple[int, int, int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.bitOps_optimal(13, 2))
