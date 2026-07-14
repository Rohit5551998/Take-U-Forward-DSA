# mypy: disable-error-code="empty-body"
# QUESTION: Print All Nodes at a Distance K in Binary Tree
# Given the root of a binary tree, a target node value, and an integer k, return the
# values of all nodes that are at distance k from the target node (in any direction).
#
# Example 1:
# Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], target = 5, k = 2
# Output: [7, 4, 1]
# Explanation: Nodes 7, 4 and 1 are all 2 edges away from node 5.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 500].
# 0 <= Node.val <= 500; 0 <= k <= 1000.


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
    def allNodesDistanceK_brute(self, root: Optional[TreeNode], target: int, k: int) -> List[int]:
        pass

    def allNodesDistanceK_better(self, root: Optional[TreeNode], target: int, k: int) -> List[int]:
        pass

    def allNodesDistanceK_optimal(self, root: Optional[TreeNode], target: int, k: int) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     left = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
#     root = TreeNode(3, left, TreeNode(1, TreeNode(0), TreeNode(8)))
#     print(sol.allNodesDistanceK_optimal(root, 5, 2))
