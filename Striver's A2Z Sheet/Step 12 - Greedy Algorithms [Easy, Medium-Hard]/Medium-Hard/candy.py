# mypy: disable-error-code="empty-body"
# QUESTION: Candy
# There are n children standing in a line, each with a rating value given in the array
# ratings. You are giving candies to these children subject to:
#   - Each child must have at least one candy.
#   - Children with a higher rating than an immediate neighbor get more candies than
#     that neighbor.
# Return the minimum number of candies you need to distribute.
#
# Example 1:
# Input: ratings = [1, 0, 2]
# Output: 5
# Explanation: Distribute [2, 1, 2] candies for a total of 5.
#
# Constraints:
# 1 <= ratings.length <= 2 * 10^4
# 0 <= ratings[i] <= 2 * 10^4

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
    def candy_brute(self, ratings: List[int]) -> int:
        pass

    def candy_better(self, ratings: List[int]) -> int:
        pass

    def candy_optimal(self, ratings: List[int]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.candy_optimal([1, 0, 2]))
