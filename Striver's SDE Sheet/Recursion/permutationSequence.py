# QUESTION: Permutation Sequence
# Given N and K, where N is the sequence of numbers from 1 to N (i.e.,
# [1, 2, 3, ..., N]), find the K-th permutation sequence (1-indexed) in
# the lexicographically sorted list of all N! permutations of [1..N].
# Return the permutation as a string.
#
# Examples:
# Example 1:
# Input: N = 3, K = 3
# Output: "213"
# Explanation: The 3! = 6 permutations of [1, 2, 3] in order are:
# "123", "132", "213", "231", "312", "321". The 3rd is "213".
#
# Example 2:
# Input: N = 4, K = 9
# Output: "2314"
#
# Constraints:
# 1 <= N <= 9
# 1 <= K <= N!
#
# Approach: Use factorial-base math to directly compute the K-th
# permutation without generating all of them — for each position, the
# leading digit is determined by K / (N-1)! after appropriate
# 0-indexing of K.
#
# Examples:
# Example 1:
# Input: N = 3, K = 3
# Output: “213”
# Explanation: The sequence has 3! permutations as illustrated in the figure above. K = 3 corresponds to the third sequence.
#
# Example 2:
# Input: N = 3, K = 5
# Result: “312”
# Explanation: The sequence has 3! permutations as illustrated in the figure above. K = 5 corresponds to the fifth sequence.


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


def permutation_sequence_brute() -> None:
    pass


def permutation_sequence_better() -> None:
    pass


def permutation_sequence_optimal() -> None:
    pass
