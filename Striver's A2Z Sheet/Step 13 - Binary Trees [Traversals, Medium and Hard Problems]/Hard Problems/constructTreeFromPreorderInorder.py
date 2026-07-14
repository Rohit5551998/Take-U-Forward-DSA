# mypy: disable-error-code="empty-body"
# QUESTION: Construct Binary Tree from Preorder and Inorder Traversal
# Given two integer arrays preorder and inorder representing the preorder and inorder
# traversal of a binary tree, construct and return the binary tree.
#
# Example 1:
# Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
# Output: [3, 9, 20, null, null, 15, 7]
# Explanation: Preorder gives roots; inorder splits left/right subtrees.
#
# Constraints:
# 1 <= preorder.length <= 3000; inorder.length == preorder.length.
# -3000 <= values <= 3000; values are unique.


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

from typing import List, Optional


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
    def constructTreeFromPreorderInorder_brute(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def constructTreeFromPreorderInorder_better(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def constructTreeFromPreorderInorder_optimal(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.constructTreeFromPreorderInorder_optimal([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
