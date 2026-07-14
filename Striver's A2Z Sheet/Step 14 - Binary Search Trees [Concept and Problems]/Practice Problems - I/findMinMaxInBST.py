# mypy: disable-error-code="empty-body"
# QUESTION: Find Minimum and Maximum in a Binary Search Tree
# Given the root of a Binary Search Tree, find the minimum and maximum values
# stored in it. In a BST the smallest value lies at the leftmost node and the
# largest value lies at the rightmost node.
#
# Example 1:
# Input: root = [8, 3, 10, 1, 6, null, 14]
# Output: min = 1, max = 14
# Explanation: Leftmost node holds 1 (minimum); rightmost node holds 14 (maximum).
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# -10^9 <= Node.val <= 10^9
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

from typing import Optional, Tuple


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
    def findMinMax_brute(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        pass

    def findMinMax_better(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        pass

    def findMinMax_optimal(self, root: Optional[TreeNode]) -> Tuple[int, int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(10, None, TreeNode(14)))
#     print(sol.findMinMax_optimal(root))
