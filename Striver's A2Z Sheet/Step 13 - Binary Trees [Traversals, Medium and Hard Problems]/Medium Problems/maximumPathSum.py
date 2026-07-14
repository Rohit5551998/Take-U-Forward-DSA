# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Path Sum in Binary Tree
# Given a non-empty binary tree, return the maximum path sum. A path is any
# sequence of nodes connected by parent-child edges; it need not pass through the root.
#
# Example 1:
# Input: root = [-10, 9, 20, null, null, 15, 7]
# Output: 42
# Explanation: Optimal path 15 -> 20 -> 7 = 42.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 10^4].
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
    def maximumPathSum_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def maximumPathSum_better(self, root: Optional[TreeNode]) -> int:
        pass

    def maximumPathSum_optimal(self, root: Optional[TreeNode]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#     print(sol.maximumPathSum_optimal(root))
