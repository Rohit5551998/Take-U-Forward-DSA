# mypy: disable-error-code="empty-body"
# QUESTION: Check if Two Trees are Identical
# Given the roots of two binary trees p and q, return true if they are the same:
# structurally identical AND every corresponding node has the same value.
#
# Example 1:
# Input: p = [1, 2, 3], q = [1, 2, 3]
# Output: true
# Explanation: Both trees have identical structure and node values.
#
# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4


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

from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkIdenticalTrees_brute(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass

    def checkIdenticalTrees_better(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass

    def checkIdenticalTrees_optimal(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     p = TreeNode(1, TreeNode(2), TreeNode(3))
#     q = TreeNode(1, TreeNode(2), TreeNode(3))
#     print(sol.checkIdenticalTrees_optimal(p, q))
