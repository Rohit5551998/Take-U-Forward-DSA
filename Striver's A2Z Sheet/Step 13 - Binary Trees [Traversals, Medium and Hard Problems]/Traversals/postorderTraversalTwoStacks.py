# mypy: disable-error-code="empty-body"
# QUESTION: Postorder Traversal using 2 Stacks
# Given the root of a binary tree, return its postorder traversal iteratively
# using two stacks.
#
# Example 1:
# Input: root = [1, null, 2, 3]
# Output: [3, 2, 1]
# Explanation: Stack1 builds a root-right-left order; stack2 reverses it to L-R-Root.
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
    def postorderTraversalTwoStacks_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def postorderTraversalTwoStacks_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def postorderTraversalTwoStacks_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
#     print(sol.postorderTraversalTwoStacks_optimal(root))
