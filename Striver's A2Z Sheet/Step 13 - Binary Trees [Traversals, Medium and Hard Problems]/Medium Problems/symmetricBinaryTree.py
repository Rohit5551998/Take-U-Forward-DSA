# mypy: disable-error-code="empty-body"
# QUESTION: Check for Symmetrical Binary Tree
# Given the root of a binary tree, check whether it is a mirror of itself (symmetric
# around its center).
#
# Example 1:
# Input: root = [1, 2, 2, 3, 4, 4, 3]
# Output: true
# Explanation: The left subtree is a mirror reflection of the right subtree.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100


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
    def symmetricBinaryTree_brute(self, root: Optional[TreeNode]) -> bool:
        pass

    def symmetricBinaryTree_better(self, root: Optional[TreeNode]) -> bool:
        pass

    def symmetricBinaryTree_optimal(self, root: Optional[TreeNode]) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     left = TreeNode(2, TreeNode(3), TreeNode(4))
#     root = TreeNode(1, left, TreeNode(2, TreeNode(4), TreeNode(3)))
#     print(sol.symmetricBinaryTree_optimal(root))
