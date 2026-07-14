# mypy: disable-error-code="empty-body"
# QUESTION: Inorder Successor / Predecessor in BST
# Given the root of a Binary Search Tree and a key value, find its inorder
# successor and inorder predecessor. The inorder successor is the smallest value
# strictly greater than the key; the inorder predecessor is the largest value
# strictly smaller than the key. If either does not exist, return -1 for it.
#
# Example 1:
# Input: root = [8, 5, 12, 2, 7, 10, null], key = 7
# Output: predecessor = 5, successor = 8
# Explanation: Inorder is [2, 5, 7, 8, 10, 12]; around 7 the neighbours are 5 and 8.
#
# Example 2:
# Input: root = [8, 5, 12, 2, 7, 10, null], key = 12
# Output: predecessor = 10, successor = -1
# Explanation: 12 is the maximum, so there is no successor.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
# root is a valid binary search tree; key exists in the BST.


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

from typing import Optional, Tuple


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
    def inorderSuccPred_brute(self, root: Optional[TreeNode], key: int) -> Tuple[int, int]:
        pass

    def inorderSuccPred_better(self, root: Optional[TreeNode], key: int) -> Tuple[int, int]:
        pass

    def inorderSuccPred_optimal(self, root: Optional[TreeNode], key: int) -> Tuple[int, int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(8, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(12, TreeNode(10)))
#     print(sol.inorderSuccPred_optimal(root, 7))
