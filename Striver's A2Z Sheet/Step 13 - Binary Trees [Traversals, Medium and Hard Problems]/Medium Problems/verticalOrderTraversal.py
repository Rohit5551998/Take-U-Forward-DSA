# mypy: disable-error-code="empty-body"
# QUESTION: Vertical Order Traversal of Binary Tree
# Given the root of a binary tree, return the vertical order traversal: group nodes
# by column (root at column 0, left is -1, right is +1). Within the same row and
# column, order by value.
#
# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: [[9], [3, 15], [20], [7]]
# Explanation: Columns -1, 0, 1, 2 read left to right.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# 0 <= Node.val <= 1000


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
    def verticalOrderTraversal_brute(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def verticalOrderTraversal_better(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def verticalOrderTraversal_optimal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#     print(sol.verticalOrderTraversal_optimal(root))
