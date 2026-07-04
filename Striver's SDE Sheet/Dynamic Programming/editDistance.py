# mypy: disable-error-code="empty-body"
# QUESTION: Edit distance
# Given two strings S1 and S2, we need to convert S1 to S2. The following
# three operations are allowed:
#   1. Deletion of a character.
#   2. Replacement of a character with another character.
#   3. Insertion of a character.
# Find the minimum number of operations required to convert S1 to S2.
#
# Examples:
# Example 1:
# Input: start = "planet", target = "plan"
# Output: 2
# Explanation:
# To transform "planet" into "plan", the following operations are required:
# 1. Delete the character 'e': "planet" -> "plan"
# 2. Delete the character 't': "plan" -> "plan"
# Thus, a total of 2 operations are needed.
#
# Example 2:
# Input: start = "abcdefg", target = "azced"
# Output: 4
# Explanation:
# To transform "abcdefg" into "azced", the following operations are required:
# 1. Replace 'b' with 'z': "abcdefg" -> "azcdefg"
# 2. Delete 'd': "azcdefg" -> "azcefg"
# 3. Delete 'f': "azcefg" -> "azceg"
# 4. Replace 'g' with 'd': "azceg" -> "azced"
# Thus, a total of 4 operations are needed.


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
    def edit_distance_brute(self, start: str, target: str) -> int:
        pass

    def edit_distance_better(self, start: str, target: str) -> int:
        pass

    def edit_distance_optimal(self, start: str, target: str) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    start = "planet"
    target = "plan"
    print(sol.edit_distance_optimal(start, target))
