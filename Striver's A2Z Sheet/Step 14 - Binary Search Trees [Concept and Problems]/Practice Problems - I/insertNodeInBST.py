# mypy: disable-error-code="empty-body"
# QUESTION: Insert a given Node in Binary Search Tree
# You are given the root of a Binary Search Tree and a value val to insert. Insert
# val into the BST such that the BST property is preserved, and return the root of
# the modified tree. It is guaranteed that the new value does not already exist in
# the tree. There may be many valid ways to insert; any valid BST is accepted.
#
# Example 1:
# Input: root = [4, 2, 7, 1, 3], val = 5
# Output: [4, 2, 7, 1, 3, 5]
# Explanation: 5 is inserted as the left child of 7, keeping the BST valid.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -10^8 <= Node.val <= 10^8
# All values Node.val are unique.
# -10^8 <= val <= 10^8
# It is guaranteed that val does not exist in the original BST.


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
    def insertIntoBST_brute(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pass

    def insertIntoBST_better(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pass

    def insertIntoBST_optimal(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
#     print(sol.insertIntoBST_optimal(root, 5))
