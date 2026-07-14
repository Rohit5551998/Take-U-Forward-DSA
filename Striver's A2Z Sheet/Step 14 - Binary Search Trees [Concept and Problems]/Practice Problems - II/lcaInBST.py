# mypy: disable-error-code="empty-body"
# QUESTION: Lowest Common Ancestor in a Binary Search Tree
# Given the root of a Binary Search Tree and two nodes p and q present in it, find
# their Lowest Common Ancestor (LCA). The LCA is the deepest node that has both p
# and q as descendants (a node may be a descendant of itself). The BST ordering
# lets you decide direction: if both values are smaller go left, if both larger go
# right, otherwise the current node is the split point and hence the LCA.
#
# Example 1:
# Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8
# Output: 6
# Explanation: 2 and 8 lie on opposite sides of 6, so 6 is their LCA.
#
# Example 2:
# Input: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
# Output: 2
# Explanation: 4 is in the subtree of 2, so 2 is the LCA of 2 and 4.
#
# Constraints:
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique. p != q, and both p and q exist in the BST.


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
    def lowestCommonAncestor_brute(
        self,
        root: Optional[TreeNode],
        p: Optional[TreeNode],
        q: Optional[TreeNode],
    ) -> Optional[TreeNode]:
        pass

    def lowestCommonAncestor_better(
        self,
        root: Optional[TreeNode],
        p: Optional[TreeNode],
        q: Optional[TreeNode],
    ) -> Optional[TreeNode]:
        pass

    def lowestCommonAncestor_optimal(
        self,
        root: Optional[TreeNode],
        p: Optional[TreeNode],
        q: Optional[TreeNode],
    ) -> Optional[TreeNode]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     p = TreeNode(2)
#     q = TreeNode(8)
#     root = TreeNode(6, p, q)
#     print(sol.lowestCommonAncestor_optimal(root, p, q))
