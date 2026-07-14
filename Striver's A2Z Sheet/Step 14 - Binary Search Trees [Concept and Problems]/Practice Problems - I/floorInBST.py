# mypy: disable-error-code="empty-body"
# QUESTION: Floor in a Binary Search Tree
# Given the root of a Binary Search Tree and a key X, find the floor of X in the
# BST. The floor of X is the largest value in the BST that is less than or equal
# to X. If no such value exists, return -1.
#
# Example 1:
# Input: root = [8, 5, 12, 2, 7, 10, null], X = 6
# Output: 5
# Explanation: The largest value <= 6 present in the BST is 5.
#
# Example 2:
# Input: root = [8, 5, 12, 2, 7, 10, null], X = 1
# Output: -1
# Explanation: No node has a value <= 1.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
# root is a valid binary search tree.


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
    def findFloor_brute(self, root: Optional[TreeNode], key: int) -> int:
        pass

    def findFloor_better(self, root: Optional[TreeNode], key: int) -> int:
        pass

    def findFloor_optimal(self, root: Optional[TreeNode], key: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(8, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(12, TreeNode(10)))
#     print(sol.findFloor_optimal(root, 6))
