# mypy: disable-error-code="empty-body"
# QUESTION: Zig Zag / Spiral Traversal of Binary Tree
# Given the root of a binary tree, return the zigzag level order traversal: left to
# right on one level, then right to left on the next, alternating.
#
# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: [[3], [20, 9], [15, 7]]
# Explanation: Level 0 L->R, level 1 R->L, level 2 L->R.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
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
    def zigzagTraversal_brute(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def zigzagTraversal_better(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def zigzagTraversal_optimal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
#     print(sol.zigzagTraversal_optimal(root))
