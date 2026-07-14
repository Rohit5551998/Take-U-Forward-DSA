# mypy: disable-error-code="empty-body"
# QUESTION: Flatten Binary Tree to Linked List
# Given the root of a binary tree, flatten it in-place into a 'linked list' where
# each node's right pointer points to the next node in preorder and the left pointer
# is always null.
#
# Example 1:
# Input: root = [1, 2, 5, 3, 4, null, 6]
# Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6]
# Explanation: The tree is flattened into a right-skewed list in preorder.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
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
    def flattenBinaryTreeToLinkedList_brute(self, root: Optional[TreeNode]) -> None:
        pass

    def flattenBinaryTreeToLinkedList_better(self, root: Optional[TreeNode]) -> None:
        pass

    def flattenBinaryTreeToLinkedList_optimal(self, root: Optional[TreeNode]) -> None:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
#     sol.flattenBinaryTreeToLinkedList_optimal(root)
