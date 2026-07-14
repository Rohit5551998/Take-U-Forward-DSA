# mypy: disable-error-code="empty-body"
# QUESTION: Right / Left View of Binary Tree
# Given the root of a binary tree, return the right view: the values of the nodes
# you can see ordered from top to bottom when standing on the right side (the last
# node of each level). The left view is symmetric.
#
# Example 1:
# Input: root = [1, 2, 3, null, 5, null, 4]
# Output: [1, 3, 4]
# Explanation: Rightmost node at each level: 1, then 3, then 4.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
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
    def rightLeftViewOfBinaryTree_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def rightLeftViewOfBinaryTree_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def rightLeftViewOfBinaryTree_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
#     print(sol.rightLeftViewOfBinaryTree_optimal(root))
