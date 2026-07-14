# mypy: disable-error-code="empty-body"
# QUESTION: Iterative Inorder Traversal of Binary Tree
# Given the root of a binary tree, return its inorder traversal WITHOUT recursion,
# using an explicit stack.
#
# Example 1:
# Input: root = [1, null, 2, 3]
# Output: [1, 3, 2]
# Explanation: Go left as far as possible, process node, then move right.
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
    def iterativeInorderTraversal_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def iterativeInorderTraversal_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def iterativeInorderTraversal_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
#     print(sol.iterativeInorderTraversal_optimal(root))
