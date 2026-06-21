# QUESTION: Fractional Knapsack
# Given the weight of N items and their corresponding values, put these
# items in a knapsack of total capacity W such that the total value
# obtained is maximized.
# Note: Unlike 0/1 Knapsack, we CAN break an item — i.e., take a
# fraction of an item (any fraction in [0, 1] of any item's weight, with
# proportional value).
# Greedy approach: sort items by value/weight ratio in descending order,
# then fill the knapsack greedily — take whole items while they fit, and
# take a fraction of the next item to fill the remaining capacity.
#
# Examples:
# Example 1:
# Input: N = 3, W = 50, val[] = [60, 100, 120], wt[] = [10, 20, 30]
# Output: 240.0
# Explanation: Take items 1 (val=60) and 2 (val=100) whole (40 weight,
# 160 value), then take 2/3 of item 3 (remaining 10/30 weight, value
# 120 * 10/30 = 40). Wait — recompute: 2/3 of item 3 weighs 20, value
# 120 * 20/30 = 80. Total weight = 10 + 20 + 20 = 50, value = 60 + 100 + 80 = 240.
#
# Example 2:
# Input: N = 2, W = 50, val = [60, 100], wt = [20, 50]
# Output: 160.0
# Explanation: Take all of item 1 (val=60, wt=20), then 30/50 of item 2
# (value 100 * 30/50 = 60). Total = 60 + 60 = 120 (sample answer; check).
#
# Constraints:
# 1 <= N <= 10^5
# 1 <= W <= 10^5
# 1 <= wt[i], val[i] <= 10^4


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


def fractional_knapsack_brute() -> None:
    pass


def fractional_knapsack_better() -> None:
    pass


def fractional_knapsack_optimal() -> None:
    pass
