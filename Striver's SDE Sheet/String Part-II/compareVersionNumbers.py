# mypy: disable-error-code="empty-body"
# QUESTION: Compare version numbers
# Given two version numbers, version1 and version2, compare them.
# A version number is a string consisting of dot-separated integers.
# Each segment (called a revision) is a non-negative integer, and
# leading zeroes should be ignored during comparison.
# To compare version numbers, compare their revisions in LEFT-TO-RIGHT
# order. Revisions at index i are compared as integers (ignoring leading
# zeros). If one version number has fewer revisions, the missing
# revisions are treated as 0.
# Return:
#   - -1  if version1 < version2
#   -  1  if version1 > version2
#   -  0  if version1 == version2
#
# Examples:
# Example 1:
# Input: version1 = "1.01", version2 = "1.001"
# Output: 0
# Explanation: Ignoring leading zeros, both are "1.1".
#
# Example 2:
# Input: version1 = "1.0", version2 = "1.0.0"
# Output: 0
# Explanation: version1 has no third revision, treated as 0.
#
# Example 3:
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
# Explanation: 0 < 1 at the first revision.
#
# Constraints:
# 1 <= version1.length, version2.length <= 500
# version1 and version2 only contain digits and '.'.
# version1 and version2 are valid version numbers.
# All the given revisions in version1 and version2 can be stored in a
# 32-bit integer.


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
    def compare_version_numbers_brute(self, version1: str, version2: str) -> int:
        pass

    def compare_version_numbers_better(self, version1: str, version2: str) -> int:
        pass

    def compare_version_numbers_optimal(self, version1: str, version2: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    version1 = "1.01"
    version2 = "1.001"
    print(sol.compare_version_numbers_optimal(version1, version2))
