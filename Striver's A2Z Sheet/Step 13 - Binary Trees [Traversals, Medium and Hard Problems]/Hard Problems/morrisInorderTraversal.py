# mypy: disable-error-code="empty-body"
# QUESTION: Morris Inorder Traversal of Binary Tree
# Given the root of a binary tree, return its inorder traversal using Morris
# traversal in O(1) extra space by threading the tree.
#
# Example 1:
# Input: root = [1, null, 2, 3]
# Output: [1, 3, 2]
# Explanation: Temporary threads to the inorder predecessor avoid a stack.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
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
    def morrisInorderTraversal_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def morrisInorderTraversal_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def morrisInorderTraversal_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
#     print(sol.morrisInorderTraversal_optimal(root))
