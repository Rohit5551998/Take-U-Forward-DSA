# mypy: disable-error-code="empty-body"
# QUESTION: Find K-th Smallest / Largest Element in BST
# Given the root of a Binary Search Tree and an integer k, return the k-th
# smallest value (1-indexed) among all node values. A related task is the k-th
# largest, which is the (N-k+1)-th smallest. An inorder traversal of a BST visits
# values in ascending order, which makes the k-th element easy to pick.
#
# Example 1:
# Input: root = [3, 1, 4, null, 2], k = 1
# Output: 1
# Explanation: Inorder is [1, 2, 3, 4]; the 1st smallest is 1.
#
# Example 2:
# Input: root = [5, 3, 6, 2, 4, null, null, 1], k = 3
# Output: 3
# Explanation: Inorder is [1, 2, 3, 4, 5, 6]; the 3rd smallest is 3.
#
# Constraints:
# The number of nodes in the tree is n, and 1 <= k <= n <= 10^4.
# 0 <= Node.val <= 10^4
# root is a valid binary search tree.


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
    def kthSmallest_brute(self, root: Optional[TreeNode], k: int) -> int:
        pass

    def kthSmallest_better(self, root: Optional[TreeNode], k: int) -> int:
        pass

    def kthSmallest_optimal(self, root: Optional[TreeNode], k: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
#     print(sol.kthSmallest_optimal(root, 1))
