# mypy: disable-error-code="empty-body"
# QUESTION: Binary Tree Traversals in Binary Tree (BFS & DFS)
# Given the root of a binary tree, understand the two families of traversals:
# Depth-First (Inorder, Preorder, Postorder) and Breadth-First (Level order).
# This is the conceptual entry point before implementing each traversal.
#
# Example 1:
# Input: root = [1, 2, 3, 4, 5]
# Output: DFS preorder = [1, 2, 4, 5, 3]; BFS level order = [1, 2, 3, 4, 5]
# Explanation: DFS goes deep first; BFS explores level by level.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
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
    def binaryTreeTraversals_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def binaryTreeTraversals_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def binaryTreeTraversals_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
#     print(sol.binaryTreeTraversals_optimal(root))
