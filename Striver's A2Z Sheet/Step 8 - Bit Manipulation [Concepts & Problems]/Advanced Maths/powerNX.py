# mypy: disable-error-code="empty-body"
# QUESTION: Power(n, x)
# Implement pow(x, n), which computes x raised to the power n (i.e. x^n),
# using fast/binary exponentiation. Handle negative exponents by returning 1 / x^|n|.
# Example 1:
# Input: x = 2.0, n = 10
# Output: 1024.0
# Explanation: 2^10 = 1024.
# Example 2:
# Input: x = 2.0, n = -2
# Output: 0.25
# Explanation: 2^-2 = 1 / 2^2 = 1/4 = 0.25.
# Constraints:
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31 - 1

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
    def power_brute(self, x: float, n: int) -> float:
        pass

    def power_better(self, x: float, n: int) -> float:
        pass

    def power_optimal(self, x: float, n: int) -> float:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.power_optimal(2.0, 10))
