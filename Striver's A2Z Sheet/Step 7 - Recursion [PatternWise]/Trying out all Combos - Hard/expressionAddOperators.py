# mypy: disable-error-code="empty-body"
# QUESTION: Expression Add Operators
# Given a string num that contains only digits and an integer target, return all
# possible expressions that can be formed by inserting the binary operators '+',
# '-', and/or '*' between the digits of num so that the resulting expression
# evaluates to target. Operands must not have leading zeros.
# Example 1:
# Input: num = "123", target = 6
# Output: ["1*2*3", "1+2+3"]
# Example 2:
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
# Constraints:
# 1 <= num.length <= 10
# num consists of only digits.
# -2^31 <= target <= 2^31 - 1

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
    def add_operators_brute(self, num: str, target: int) -> List[str]:
        pass

    def add_operators_better(self, num: str, target: int) -> List[str]:
        pass

    def add_operators_optimal(self, num: str, target: int) -> List[str]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.add_operators_optimal("123", 6))
