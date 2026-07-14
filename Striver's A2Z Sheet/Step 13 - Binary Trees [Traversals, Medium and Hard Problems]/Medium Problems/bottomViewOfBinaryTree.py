# mypy: disable-error-code="empty-body"
# QUESTION: Bottom View of Binary Tree
# Given the root of a binary tree, return the bottom view: the set of nodes visible
# when the tree is viewed from directly below, ordered left to right by column.
#
# Example 1:
# Input: root = [20, 8, 22, 5, 3, 4, 25]
# Output: [5, 3, 4, 25, 22]
# Explanation: Last node encountered in each vertical column (BFS order).
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
    def bottomViewOfBinaryTree_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def bottomViewOfBinaryTree_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def bottomViewOfBinaryTree_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     left = TreeNode(8, TreeNode(5), TreeNode(3))
#     root = TreeNode(20, left, TreeNode(22, TreeNode(4), TreeNode(25)))
#     print(sol.bottomViewOfBinaryTree_optimal(root))
