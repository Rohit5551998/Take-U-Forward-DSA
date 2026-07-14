# mypy: disable-error-code="empty-body"
# QUESTION: Z-Function
# For a string s of length n, the Z-function is an array z where z[i] is the
# length of the longest substring starting at index i that is also a prefix of s.
# By convention z[0] is defined as 0 (or n). The Z-function can be computed in
# O(n) using a "Z-box" (the rightmost [l, r] segment matching a prefix) to reuse
# previously computed values. It is widely used for pattern matching by building
# the Z-function of pattern + separator + text.
# Example 1:
# Input: s = "aabxaabxcaabxaabxay"
# Output: [0, 1, 0, 0, 4, 1, 0, 0, 0, 8, 1, 0, 0, 5, 1, 0, 0, 1, 0]
# Explanation: z[4] = 4 because "aabx" (starting at index 4) matches the prefix
# "aabx" of length 4.
# Example 2:
# Input: s = "aaaaa"
# Output: [0, 4, 3, 2, 1]
# Constraints:
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.

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
    def z_function_brute(self, s: str) -> List[int]:
        pass

    def z_function_better(self, s: str) -> List[int]:
        pass

    def z_function_optimal(self, s: str) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.z_function_optimal("aabxaabxcaabxaabxay"))
