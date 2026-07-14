# mypy: disable-error-code="empty-body"
# QUESTION: Bit PreRequisites for TRIE Problems
# This is a prerequisite set of bit-manipulation operations used before solving XOR
# based Trie problems. Given an integer num, implement helper operations:
# - getBit(num, i): return the i-th bit (0 or 1) of num.
# - setBit(num, i): set the i-th bit of num to 1 and return the result.
# - clearBit(num, i): clear the i-th bit of num to 0 and return the result.
# These are the building blocks for representing numbers as bit paths in a binary
# Trie (typically iterating from the most significant bit down to bit 0).
#
# Example 1:
# Input: num = 5 (binary 101), i = 0
# Output: getBit -> 1
# Explanation: 5 = 101, the 0-th (least significant) bit is 1.
#
# Example 2:
# Input: num = 5 (binary 101), i = 1
# Output: setBit -> 7 (binary 111)
# Explanation: Setting bit 1 of 101 gives 111 = 7.
#
# Constraints:
# - 0 <= num <= 2^31 - 1
# - 0 <= i <= 31

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
    def bitOps_brute(self, num: int, i: int) -> int:
        pass

    def bitOps_better(self, num: int, i: int) -> int:
        pass

    def bitOps_optimal(self, num: int, i: int) -> int:
        pass


if __name__ == "__main__":
    # sol = Solution()
    # print(sol.bitOps_optimal(5, 0))
    pass
