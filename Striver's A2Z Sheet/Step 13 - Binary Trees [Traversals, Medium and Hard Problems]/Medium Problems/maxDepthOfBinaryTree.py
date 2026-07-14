# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth: the number of nodes
# along the longest path from the root down to the farthest leaf node.
#
# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: 3
# Explanation: Longest root-to-leaf path is 3 -> 20 -> 15 (or 7), length 3.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
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
    def maxDepthOfBinaryTree_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def maxDepthOfBinaryTree_better(self, root: Optional[TreeNode]) -> int:
        pass

    def maxDepthOfBinaryTree_optimal(self, root: Optional[TreeNode]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#     print(sol.maxDepthOfBinaryTree_optimal(root))
