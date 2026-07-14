# mypy: disable-error-code="empty-body"
# QUESTION: Construct Binary Tree from Postorder and Inorder Traversal
# Given two integer arrays inorder and postorder representing the inorder and postorder
# traversal of a binary tree, construct and return the binary tree.
#
# Example 1:
# Input: inorder = [9, 3, 15, 20, 7], postorder = [9, 15, 7, 20, 3]
# Output: [3, 9, 20, null, null, 15, 7]
# Explanation: Last of postorder is root; inorder splits left/right subtrees.
#
# Constraints:
# 1 <= inorder.length <= 3000; postorder.length == inorder.length.
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
    def constructTreeFromPostorderInorder_brute(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def constructTreeFromPostorderInorder_better(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def constructTreeFromPostorderInorder_optimal(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.constructTreeFromPostorderInorder_optimal([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
