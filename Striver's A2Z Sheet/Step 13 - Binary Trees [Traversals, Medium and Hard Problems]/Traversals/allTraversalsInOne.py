# mypy: disable-error-code="empty-body"
# QUESTION: Preorder, Inorder, and Postorder Traversal in One Traversal
# Given the root of a binary tree, compute the preorder, inorder and postorder
# traversals all in a SINGLE pass using a stack of (node, state) pairs.
#
# Example 1:
# Input: root = [1, 2, 3, 4, 5]
# Output: pre = [1, 2, 4, 5, 3], in = [4, 2, 5, 1, 3], post = [4, 5, 2, 3, 1]
# Explanation: A state counter 1/2/3 decides which list a node is appended to.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -10^4 <= Node.val <= 10^4


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

from typing import List, Optional, Tuple


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
    def allTraversalsInOne_brute(
        self, root: Optional[TreeNode]
    ) -> Tuple[List[int], List[int], List[int]]:
        pass

    def allTraversalsInOne_better(
        self, root: Optional[TreeNode]
    ) -> Tuple[List[int], List[int], List[int]]:
        pass

    def allTraversalsInOne_optimal(
        self, root: Optional[TreeNode]
    ) -> Tuple[List[int], List[int], List[int]]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
#     print(sol.allTraversalsInOne_optimal(root))
