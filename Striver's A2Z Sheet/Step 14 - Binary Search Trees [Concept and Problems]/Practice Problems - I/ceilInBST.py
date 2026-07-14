# mypy: disable-error-code="empty-body"
# QUESTION: Ceil in a Binary Search Tree
# Given the root of a Binary Search Tree and a key X, find the ceil of X in the
# BST. The ceil of X is the smallest value in the BST that is greater than or
# equal to X. If no such value exists, return -1.
#
# Example 1:
# Input: root = [8, 5, 12, 2, 7, 10, null], X = 6
# Output: 7
# Explanation: The smallest value >= 6 present in the BST is 7.
#
# Example 2:
# Input: root = [8, 5, 12, 2, 7, 10, null], X = 13
# Output: -1
# Explanation: No node has a value >= 13.
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
    def findCeil_brute(self, root: Optional[TreeNode], key: int) -> int:
        pass

    def findCeil_better(self, root: Optional[TreeNode], key: int) -> int:
        pass

    def findCeil_optimal(self, root: Optional[TreeNode], key: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(8, TreeNode(5, TreeNode(2), TreeNode(7)), TreeNode(12, TreeNode(10)))
#     print(sol.findCeil_optimal(root, 6))
