# mypy: disable-error-code="empty-body"
# QUESTION: Delete a Node in Binary Search Tree
# Given the root of a Binary Search Tree and a key, delete the node whose value
# equals key and return the (possibly new) root of the modified BST. Deletion must
# preserve the BST property. When the deleted node has two children, it is commonly
# replaced by its inorder predecessor (or successor).
#
# Example 1:
# Input: root = [5, 3, 6, 2, 4, null, 7], key = 3
# Output: [5, 4, 6, 2, null, null, 7]
# Explanation: Node 3 has two children; replaced so the BST stays valid.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -10^5 <= Node.val <= 10^5
# Each node has a unique value.
# root is a valid binary search tree.
# -10^5 <= key <= 10^5


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
    def deleteNode_brute(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pass

    def deleteNode_better(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pass

    def deleteNode_optimal(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6, None, TreeNode(7)))
#     print(sol.deleteNode_optimal(root, 3))
