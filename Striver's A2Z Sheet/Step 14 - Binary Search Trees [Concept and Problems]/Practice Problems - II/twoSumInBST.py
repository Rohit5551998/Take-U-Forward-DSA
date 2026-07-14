# mypy: disable-error-code="empty-body"
# QUESTION: Two Sum IV - Input is a BST
# Given the root of a Binary Search Tree and an integer k, return True if there
# exist two distinct nodes in the BST whose values add up to k, and False
# otherwise. The inorder traversal of a BST is sorted, which enables a two-pointer
# or BST-iterator based approach in addition to a hash-set scan.
#
# Example 1:
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 9
# Output: True
# Explanation: 2 + 7 = 9 (also 3 + 6 = 9), so a valid pair exists.
#
# Example 2:
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 28
# Output: False
# Explanation: No two distinct node values sum to 28.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
# root is a valid binary search tree.
# -10^5 <= k <= 10^5


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
    def findTarget_brute(self, root: Optional[TreeNode], k: int) -> bool:
        pass

    def findTarget_better(self, root: Optional[TreeNode], k: int) -> bool:
        pass

    def findTarget_optimal(self, root: Optional[TreeNode], k: int) -> bool:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
#     print(sol.findTarget_optimal(root, 9))
