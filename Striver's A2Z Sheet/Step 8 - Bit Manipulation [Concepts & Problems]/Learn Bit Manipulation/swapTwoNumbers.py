# mypy: disable-error-code="empty-body"
# QUESTION: Swap two numbers
# Given two integers a and b, swap their values without using a temporary variable
# (using the XOR trick). Return the swapped pair.
# Example 1:
# Input: a = 3, b = 5
# Output: a = 5, b = 3
# Explanation: After swapping, a holds b's original value and vice versa.
# Constraints:
# 0 <= a, b <= 10^9

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
    def swap_brute(self, a: int, b: int) -> Tuple[int, int]:
        pass

    def swap_better(self, a: int, b: int) -> Tuple[int, int]:
        pass

    def swap_optimal(self, a: int, b: int) -> Tuple[int, int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.swap_optimal(3, 5))
