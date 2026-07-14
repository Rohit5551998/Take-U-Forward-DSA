# mypy: disable-error-code="empty-body"
# QUESTION: Search in a Binary Search Tree
# You are given the root of a Binary Search Tree (BST) and an integer val. Return
# the node whose value equals val (i.e. the subtree rooted at that node). If no
# such node exists, return null.
#
# Example 1:
# Input: root = [4, 2, 7, 1, 3], val = 2
# Output: [2, 1, 3]
# Explanation: The node with value 2 is found; its subtree is [2, 1, 3].
#
# Example 2:
# Input: root = [4, 2, 7, 1, 3], val = 5
# Output: []
# Explanation: 5 is not present in the BST.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 10^7
# root is a valid binary search tree.
# 1 <= val <= 10^7


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
    def searchBST_brute(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pass

    def searchBST_better(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pass

    def searchBST_optimal(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
#     print(sol.searchBST_optimal(root, 2))
