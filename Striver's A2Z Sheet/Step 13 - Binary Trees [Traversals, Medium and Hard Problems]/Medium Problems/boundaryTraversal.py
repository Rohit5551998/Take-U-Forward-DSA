# mypy: disable-error-code="empty-body"
# QUESTION: Boundary Traversal of Binary Tree
# Given the root of a binary tree, return the anti-clockwise boundary traversal:
# left boundary (excluding leaves), all leaves left to right, then right boundary
# (excluding leaves) in reverse.
#
# Example 1:
# Input: root = [1, 2, 3, 4, 5, 6, 7]
# Output: [1, 2, 4, 5, 6, 7, 3]
# Explanation: Left boundary 1,2 -> leaves 4,5,6,7 -> right boundary reversed 3.
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
    def boundaryTraversal_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def boundaryTraversal_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def boundaryTraversal_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     left = TreeNode(2, TreeNode(4), TreeNode(5))
#     root = TreeNode(1, left, TreeNode(3, TreeNode(6), TreeNode(7)))
#     print(sol.boundaryTraversal_optimal(root))
