# mypy: disable-error-code="empty-body"
# QUESTION: Top View of Binary Tree
# Given the root of a binary tree, return the top view: the set of nodes visible
# when the tree is viewed from directly above, ordered left to right by column.
#
# Example 1:
# Input: root = [1, 2, 3, 4, 5, 6, 7]
# Output: [4, 2, 1, 3, 7]
# Explanation: First node encountered in each vertical column (BFS order).
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -1000 <= Node.val <= 1000


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
    def topViewOfBinaryTree_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def topViewOfBinaryTree_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def topViewOfBinaryTree_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     left = TreeNode(2, TreeNode(4), TreeNode(5))
#     root = TreeNode(1, left, TreeNode(3, TreeNode(6), TreeNode(7)))
#     print(sol.topViewOfBinaryTree_optimal(root))
