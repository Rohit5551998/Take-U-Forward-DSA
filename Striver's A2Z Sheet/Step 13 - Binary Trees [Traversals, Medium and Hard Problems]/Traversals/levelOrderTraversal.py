# mypy: disable-error-code="empty-body"
# QUESTION: Level Order Traversal of Binary Tree
# Given the root of a binary tree, return the level order traversal of its nodes'
# values (i.e. from left to right, level by level).
#
# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: [[3], [9, 20], [15, 7]]
# Explanation: Each inner list is one level, top to bottom.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
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
    def levelOrderTraversal_brute(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def levelOrderTraversal_better(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def levelOrderTraversal_optimal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#     print(sol.levelOrderTraversal_optimal(root))
