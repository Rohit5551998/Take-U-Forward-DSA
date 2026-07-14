# mypy: disable-error-code="empty-body"
# QUESTION: Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter: the number
# of edges on the longest path between any two nodes (may not pass through the root).
#
# Example 1:
# Input: root = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: Longest path 4 -> 2 -> 1 -> 3 (or 5 -> 2 -> 1 -> 3) has 3 edges.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
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
    def diameterOfBinaryTree_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def diameterOfBinaryTree_better(self, root: Optional[TreeNode]) -> int:
        pass

    def diameterOfBinaryTree_optimal(self, root: Optional[TreeNode]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
#     print(sol.diameterOfBinaryTree_optimal(root))
