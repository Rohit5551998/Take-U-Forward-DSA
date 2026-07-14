# mypy: disable-error-code="empty-body"
# QUESTION: Introduction to Binary Search Tree
# A Binary Search Tree (BST) is a binary tree in which, for every node, all
# values in its left subtree are smaller than the node's value and all values in
# its right subtree are greater. (Typically duplicates are not allowed, or handled
# with a defined convention.) This ordering makes search, insert, and delete run
# in O(height) time, which is O(log N) for a balanced BST.
# The task is to understand BST properties and verify/identify a valid BST.
#
# Example 1:
# Input: root = [8, 3, 10, 1, 6, null, 14]
# Output: True
# Explanation: Every node satisfies left < node < right, so it is a valid BST.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^5].
# -10^9 <= Node.val <= 10^9


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
    def isBST_brute(self, root: Optional[TreeNode]) -> bool:
        pass

    def isBST_better(self, root: Optional[TreeNode]) -> bool:
        pass

    def isBST_optimal(self, root: Optional[TreeNode]) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10, None, TreeNode(14)))
#     print(sol.isBST_optimal(root))
