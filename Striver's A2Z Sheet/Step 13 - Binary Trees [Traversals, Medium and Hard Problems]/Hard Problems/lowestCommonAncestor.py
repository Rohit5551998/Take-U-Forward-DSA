# mypy: disable-error-code="empty-body"
# QUESTION: Lowest Common Ancestor in Binary Tree
# Given the root of a binary tree and two nodes p and q, return their lowest common
# ancestor (LCA): the deepest node that has both p and q as descendants.
#
# Example 1:
# Input: root = [3, 5, 1, 6, 2, 0, 8], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is node 3.
#
# Constraints:
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9; p and q exist in the tree and are distinct.


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
    def lowestCommonAncestor_brute(self, root: Optional[TreeNode], p: int, q: int) -> Optional[int]:
        pass

    def lowestCommonAncestor_better(
        self, root: Optional[TreeNode], p: int, q: int
    ) -> Optional[int]:
        pass

    def lowestCommonAncestor_optimal(
        self, root: Optional[TreeNode], p: int, q: int
    ) -> Optional[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     left = TreeNode(5, TreeNode(6), TreeNode(2))
#     root = TreeNode(3, left, TreeNode(1, TreeNode(0), TreeNode(8)))
#     print(sol.lowestCommonAncestor_optimal(root, 5, 1))
