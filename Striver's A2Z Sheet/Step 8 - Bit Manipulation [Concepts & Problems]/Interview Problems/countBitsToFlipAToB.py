# mypy: disable-error-code="empty-body"
# QUESTION: Count number of bits to be flipped to convert A to B
# Given two integers A and B, count the number of bit positions that must be flipped
# in the binary representation of A to convert it into B.
# Example 1:
# Input: A = 10, B = 20   (A = 01010, B = 10100 in binary)
# Output: 4
# Explanation: A XOR B = 11110, which has 4 set bits, so 4 flips are needed.
# Example 2:
# Input: A = 7, B = 10    (A = 0111, B = 1010 in binary)
# Output: 3
# Explanation: A XOR B = 1101, which has 3 set bits.
# Constraints:
# 0 <= A, B <= 10^9

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
    def countBitsToFlip_brute(self, A: int, B: int) -> int:
        pass

    def countBitsToFlip_better(self, A: int, B: int) -> int:
        pass

    def countBitsToFlip_optimal(self, A: int, B: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.countBitsToFlip_optimal(10, 20))
