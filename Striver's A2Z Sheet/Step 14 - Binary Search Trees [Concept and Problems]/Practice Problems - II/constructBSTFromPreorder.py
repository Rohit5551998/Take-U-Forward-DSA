# mypy: disable-error-code="empty-body"
# QUESTION: Construct a BST from a Preorder Traversal
# Given an array preorder representing the preorder traversal of a Binary Search
# Tree, construct the BST and return its root. In a BST preorder, the first element
# is the root, the following contiguous block of values smaller than the root form
# the left subtree, and the remaining larger values form the right subtree.
#
# Example 1:
# Input: preorder = [8, 5, 1, 7, 10, 12]
# Output: [8, 5, 10, 1, 7, null, 12]
# Explanation: 8 is root; {5,1,7} < 8 build the left subtree; {10,12} > 8 the right.
#
# Constraints:
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# All the values of preorder are unique.
# preorder is guaranteed to be the preorder traversal of a valid BST.


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
    def bstFromPreorder_brute(self, preorder: List[int]) -> Optional[TreeNode]:
        pass

    def bstFromPreorder_better(self, preorder: List[int]) -> Optional[TreeNode]:
        pass

    def bstFromPreorder_optimal(self, preorder: List[int]) -> Optional[TreeNode]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.bstFromPreorder_optimal([8, 5, 1, 7, 10, 12]))
