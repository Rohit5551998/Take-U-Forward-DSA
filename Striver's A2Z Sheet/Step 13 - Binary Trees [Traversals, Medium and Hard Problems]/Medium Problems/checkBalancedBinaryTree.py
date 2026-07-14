# mypy: disable-error-code="empty-body"
# QUESTION: Check if the Binary Tree is Balanced
# Given a binary tree, determine if it is height-balanced: for every node the
# heights of the left and right subtrees differ by at most 1.
#
# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: true
# Explanation: Every node's subtrees differ in height by at most 1.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
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
    def checkBalancedBinaryTree_brute(self, root: Optional[TreeNode]) -> bool:
        pass

    def checkBalancedBinaryTree_better(self, root: Optional[TreeNode]) -> bool:
        pass

    def checkBalancedBinaryTree_optimal(self, root: Optional[TreeNode]) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#     print(sol.checkBalancedBinaryTree_optimal(root))
