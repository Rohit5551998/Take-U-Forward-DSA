# mypy: disable-error-code="empty-body"
# QUESTION: Binary Tree Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of its nodes'
# values. Preorder visits Root -> Left subtree -> Right subtree.
#
# Example 1:
# Input: root = [1, null, 2, 3]
# Output: [1, 2, 3]
# Explanation: Visit root 1, then its (empty) left, then right subtree 2->3.
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
    def preorderTraversal_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def preorderTraversal_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def preorderTraversal_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
#     print(sol.preorderTraversal_optimal(root))
