# mypy: disable-error-code="empty-body"
# QUESTION: Check for Children Sum Property
# Given the root of a binary tree, modify it (if allowed) so that for every node its
# value equals the sum of its children's values. You may only increment node values.
#
# Example 1:
# Input: root = [2, 35, 10, 2, 3, 5, 2]
# Output: tree satisfying children sum property
# Explanation: Each parent equals the sum of its children after adjustment.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# 1 <= Node.val <= 10^5


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
    def childrenSumProperty_brute(self, root: Optional[TreeNode]) -> None:
        pass

    def childrenSumProperty_better(self, root: Optional[TreeNode]) -> None:
        pass

    def childrenSumProperty_optimal(self, root: Optional[TreeNode]) -> None:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     left = TreeNode(35, TreeNode(2), TreeNode(3))
#     root = TreeNode(2, left, TreeNode(10, TreeNode(5), TreeNode(2)))
#     sol.childrenSumProperty_optimal(root)
