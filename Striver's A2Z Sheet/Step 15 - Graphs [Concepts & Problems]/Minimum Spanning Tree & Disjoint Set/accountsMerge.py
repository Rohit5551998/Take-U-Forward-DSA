# mypy: disable-error-code="empty-body"
# QUESTION: Accounts Merge
# Given a list of accounts where each element accounts[i] is a list of strings,
# the first element accounts[i][0] is a name, and the rest of the elements are
# emails representing emails of the account.
# Two accounts definitely belong to the same person if there is some common
# email to both accounts. Note that even if two accounts have the same name,
# they may belong to different people, as people could have the same name. A
# person can have any number of accounts initially, but all of their accounts
# definitely have the same name.
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order. The accounts themselves can be returned in any order.
#
# Example 1:
# Input: accounts = [
#   ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#   ["John", "johnsmith@mail.com", "john00@mail.com"],
#   ["Mary", "mary@mail.com"],
#   ["John", "johnnybravo@mail.com"]
# ]
# Output: [
#   ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
#   ["Mary", "mary@mail.com"],
#   ["John", "johnnybravo@mail.com"]
# ]
# Explanation: The first and second John's accounts share "johnsmith@mail.com",
# so they are merged. The third account (Mary) and fourth account (John) have
# no shared emails, so they remain separate.
#
# Constraints:
# 1 <= accounts.length <= 1000
# 2 <= accounts[i].length <= 10
# 1 <= accounts[i][j].length <= 30
# accounts[i][0] consists of English letters.
# accounts[i][j] (for j > 0) is a valid email.

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
    def accounts_merge_brute(self, accounts: List[List[str]]) -> List[List[str]]:
        pass

    def accounts_merge_better(self, accounts: List[List[str]]) -> List[List[str]]:
        pass

    def accounts_merge_optimal(self, accounts: List[List[str]]) -> List[List[str]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.accounts_merge_optimal([
    #     ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    #     ["John", "johnsmith@mail.com", "john00@mail.com"],
    #     ["Mary", "mary@mail.com"],
    #     ["John", "johnnybravo@mail.com"],
    # ])
