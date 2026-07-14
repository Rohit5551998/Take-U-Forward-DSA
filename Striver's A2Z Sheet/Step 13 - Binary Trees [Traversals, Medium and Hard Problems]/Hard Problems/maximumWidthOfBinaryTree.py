# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Width of Binary Tree
# Given the root of a binary tree, return the maximum width. The width of a level is
# the number of nodes between the leftmost and rightmost non-null nodes (including
# nulls between them), using position indexing.
#
# Example 1:
# Input: root = [1, 3, 2, 5, 3, null, 9]
# Output: 4
# Explanation: The widest level has nodes at positions spanning width 4.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 3000].
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
    def maximumWidthOfBinaryTree_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def maximumWidthOfBinaryTree_better(self, root: Optional[TreeNode]) -> int:
        pass

    def maximumWidthOfBinaryTree_optimal(self, root: Optional[TreeNode]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
#     print(sol.maximumWidthOfBinaryTree_optimal(root))
