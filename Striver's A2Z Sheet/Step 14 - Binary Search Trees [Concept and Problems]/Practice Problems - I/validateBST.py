# mypy: disable-error-code="empty-body"
# QUESTION: Check if a Tree is a BST or Binary Tree (Validate BST)
# Given the root of a binary tree, determine whether it is a valid Binary Search
# Tree. A BST requires that for every node, all values in its left subtree are
# strictly smaller and all values in its right subtree are strictly greater than
# the node's value (the property must hold for entire subtrees, not just children).
#
# Example 1:
# Input: root = [2, 1, 3]
# Output: True
# Explanation: 1 < 2 < 3, so it is a valid BST.
#
# Example 2:
# Input: root = [5, 1, 4, null, null, 3, 6]
# Output: False
# Explanation: Node 4 is in the right subtree of 5 but 3 < 5, violating the BST rule.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1


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
    def isValidBST_brute(self, root: Optional[TreeNode]) -> bool:
        pass

    def isValidBST_better(self, root: Optional[TreeNode]) -> bool:
        pass

    def isValidBST_optimal(self, root: Optional[TreeNode]) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(2, TreeNode(1), TreeNode(3))
#     print(sol.isValidBST_optimal(root))
