# QUESTION: Z function
# Given a pattern P and a text T, find all occurrences of P inside T
# using the Z-function (Z-algorithm) for string matching in O(|T| + |P|)
# time.
#
# Z-function background:
#   For a string s of length n, the Z-array z[] is defined as:
#     z[0] = 0 (by convention; some sources set z[0] = n)
#     z[i] = the length of the longest substring starting at index i
#            that matches a prefix of s.
#   Example: s = "aabaabab"
#            z = [0, 1, 0, 4, 1, 0, 2, 0]
#
# Algorithm to find occurrences of pattern P in text T:
#   1. Construct a combined string S = P + '$' + T, where '$' is a
#      sentinel character not in P or T.
#   2. Compute the Z-array of S in O(|S|) using the two-pointer
#      [l, r] window technique.
#   3. Any index i where z[i] == |P| means an occurrence of P starts at
#      position (i - |P| - 1) in T.
#
# Examples:
# Example 1:
# Input: text = "aabaacaadaabaaba", pattern = "aaba"
# Output: [0, 9, 12]
# Explanation: Pattern occurs starting at indices 0, 9, and 12 in text.
#
# Example 2:
# Input: text = "abcdef", pattern = "xyz"
# Output: []
#
# Constraints:
# 1 <= |P| <= |T| <= 10^5
# P and T consist of printable ASCII characters.


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


def z_function_brute() -> None:
    pass


def z_function_better() -> None:
    pass


def z_function_optimal() -> None:
    pass
