# mypy: disable-error-code="empty-body"
# QUESTION: Root to Node Path in Binary Tree
# Given the root of a binary tree and a target node value, return the path from the
# root to that node as a list of values.
#
# Example 1:
# Input: root = [1, 2, 3, 4, 5, 6, 7], target = 5
# Output: [1, 2, 5]
# Explanation: Path from root 1 down to node 5.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
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
    def rootToNodePath_brute(self, root: Optional[TreeNode], target: int) -> List[int]:
        pass

    def rootToNodePath_better(self, root: Optional[TreeNode], target: int) -> List[int]:
        pass

    def rootToNodePath_optimal(self, root: Optional[TreeNode], target: int) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     left = TreeNode(2, TreeNode(4), TreeNode(5))
#     root = TreeNode(1, left, TreeNode(3, TreeNode(6), TreeNode(7)))
#     print(sol.rootToNodePath_optimal(root, 5))
