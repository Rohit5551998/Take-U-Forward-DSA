# mypy: disable-error-code="empty-body"
# QUESTION: Set/Unset the rightmost unset bit
# Given a non-negative integer N, set (turn to 1) the rightmost unset (0) bit
# in its binary representation and return the resulting number.
# If all bits are already set (as in a number of the form 2^k - 1), return N unchanged.
# Example 1:
# Input: N = 10   (10 = 1010 in binary)
# Output: 11      (11 = 1011 in binary)
# Explanation: The rightmost 0 bit is at position 0; setting it gives 1011 = 11.
# Example 2:
# Input: N = 7    (7 = 111 in binary)
# Output: 7
# Explanation: All bits are set, so N is returned unchanged.
# Constraints:
# 0 <= N <= 10^9

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
    def setRightmostUnsetBit_brute(self, N: int) -> int:
        pass

    def setRightmostUnsetBit_better(self, N: int) -> int:
        pass

    def setRightmostUnsetBit_optimal(self, N: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.setRightmostUnsetBit_optimal(10))
