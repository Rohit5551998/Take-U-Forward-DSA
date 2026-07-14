# mypy: disable-error-code="empty-body"
# QUESTION: Serialize and Deserialize Binary Tree
# Design an algorithm to serialize a binary tree to a string and deserialize that
# string back to the original tree structure.
#
# Example 1:
# Input: root = [1, 2, 3, null, null, 4, 5]
# Output: [1, 2, 3, null, null, 4, 5]
# Explanation: deserialize(serialize(root)) reproduces the original tree.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000


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
    def serialize(self, root: Optional[TreeNode]) -> str:
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
#     print(sol.deserialize(sol.serialize(root)))
