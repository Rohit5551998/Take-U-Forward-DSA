# mypy: disable-error-code="empty-body"
# QUESTION: Hands of Straights
# Alice has some number of cards and she wants to rearrange the cards into groups
# so that each group is of size groupSize, and consists of groupSize consecutive
# cards. Given an integer array hand where hand[i] is the value on the ith card
# and an integer groupSize, return true if she can rearrange the cards, or false
# otherwise.
#
# Example 1:
# Input: hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3
# Output: True
# Explanation: The hand can be split into [1,2,3], [2,3,4], [6,7,8].
#
# Example 2:
# Input: hand = [1, 2, 3, 4, 5], groupSize = 4
# Output: False
# Explanation: The hand cannot be rearranged into groups of 4 consecutive cards.
#
# Constraints:
# 1 <= hand.length <= 10^4
# 0 <= hand[i] <= 10^9
# 1 <= groupSize <= hand.length


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
    def isNStraightHand_brute(self, hand: List[int], groupSize: int) -> bool:
        pass

    def isNStraightHand_better(self, hand: List[int], groupSize: int) -> bool:
        pass

    def isNStraightHand_optimal(self, hand: List[int], groupSize: int) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.isNStraightHand_optimal([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
