# mypy: disable-error-code="empty-body"
# QUESTION: Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the
# recursive formula:
#   countAndSay(1) = "1"
#   countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding compresses a string by replacing each group of consecutive
# identical characters with the count followed by the character. For example, the
# string "3322251" is encoded as "23" (two 3's), "32" (three 2's), "15" (one 5)
# and "11" (one 1), giving "23321511". Given a positive integer n, return the
# n-th element of the count-and-say sequence.
# Example 1:
# Input: n = 4
# Output: "1211"
# Explanation: countAndSay(1)="1", countAndSay(2)="11", countAndSay(3)="21",
# countAndSay(4)="1211".
# Example 2:
# Input: n = 1
# Output: "1"
# Constraints:
# 1 <= n <= 30

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
    def count_and_say_brute(self, n: int) -> str:
        pass

    def count_and_say_better(self, n: int) -> str:
        pass

    def count_and_say_optimal(self, n: int) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    # print(sol.count_and_say_optimal(4))
