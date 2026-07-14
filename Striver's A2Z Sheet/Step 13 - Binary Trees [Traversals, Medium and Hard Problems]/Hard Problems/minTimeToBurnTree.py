# mypy: disable-error-code="empty-body"
# QUESTION: Minimum Time Taken to Burn the Binary Tree from a Node
# Given the root of a binary tree and a target start node, fire spreads to adjacent
# nodes (parent and children) each unit of time. Return the minimum time to burn the
# entire tree.
#
# Example 1:
# Input: root = [1, 2, 3, 4, 5, null, 6], start = 5
# Output: 4
# Explanation: Fire spreads outward from node 5 and reaches the farthest node in 4 units.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# 1 <= Node.val <= 10^5; start exists in the tree.


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
    def minTimeToBurnTree_brute(self, root: Optional[TreeNode], start: int) -> int:
        pass

    def minTimeToBurnTree_better(self, root: Optional[TreeNode], start: int) -> int:
        pass

    def minTimeToBurnTree_optimal(self, root: Optional[TreeNode], start: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(6)))
#     print(sol.minTimeToBurnTree_optimal(root, 5))
