# mypy: disable-error-code="empty-body"
# QUESTION: Count Total Nodes in a Complete Binary Tree
# Given the root of a complete binary tree, count the number of nodes in better than
# O(n) time by exploiting the complete-tree structure.
#
# Example 1:
# Input: root = [1, 2, 3, 4, 5, 6]
# Output: 6
# Explanation: The complete binary tree has 6 nodes.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 5 * 10^4].
# 0 <= Node.val <= 5 * 10^4; the tree is guaranteed complete.


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
    def countNodesInCompleteTree_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def countNodesInCompleteTree_better(self, root: Optional[TreeNode]) -> int:
        pass

    def countNodesInCompleteTree_optimal(self, root: Optional[TreeNode]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
#     print(sol.countNodesInCompleteTree_optimal(root))
