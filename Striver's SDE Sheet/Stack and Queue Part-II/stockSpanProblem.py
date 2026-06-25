# QUESTION: Stock span problem
# Given an array arr of size n, where each element arr[i] represents the
# stock price on day i, calculate the SPAN of stock prices for each day.
# The span S_i for a specific day i is defined as the maximum number of
# consecutive days (ending at day i, going back) for which the price on
# those days was LESS THAN OR EQUAL TO the price on day i.
#
# Examples:
# Example 1:
# Input: arr = [100, 80, 60, 70, 60, 75, 85]
# Output: [1, 1, 1, 2, 1, 4, 6]
# Explanation:
#   Day 0 (100): only itself -> 1
#   Day 1 (80): 100 is greater -> 1
#   Day 2 (60): -> 1
#   Day 3 (70): includes 60 -> 2
#   Day 4 (60): -> 1
#   Day 5 (75): 60, 70, 60 are ≤ 75 -> 4
#   Day 6 (85): all prior are ≤ 85 -> 6
#
# Example 2:
# Input: arr = [10, 4, 5, 90, 120, 80]
# Output: [1, 1, 2, 4, 5, 1]
#
# Constraints:
# 1 <= n <= 10^5
# 1 <= arr[i] <= 10^5
#
# Optimal approach: monotonic decreasing stack of (price, span) pairs.


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
    def stock_span_problem_brute(self) -> None:
        pass

    def stock_span_problem_better(self) -> None:
        pass

    def stock_span_problem_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
