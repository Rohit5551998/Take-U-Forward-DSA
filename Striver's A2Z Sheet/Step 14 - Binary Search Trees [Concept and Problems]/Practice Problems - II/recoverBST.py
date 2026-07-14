# mypy: disable-error-code="empty-body"
# QUESTION: Recover Binary Search Tree (Correct BST with Two Nodes Swapped)
# You are given the root of a Binary Search Tree in which the values of exactly two
# nodes were swapped by mistake. Recover the tree by swapping their values back so
# it becomes a valid BST again, without changing its structure. In the inorder
# sequence of a correct BST every value is increasing; a swap creates one or two
# descending adjacent pairs that pinpoint the offending nodes.
#
# Example 1:
# Input: root = [1, 3, null, null, 2]
# Output: [3, 1, null, null, 2]
# Explanation: Nodes 1 and 3 were swapped; swapping their values fixes the BST.
#
# Example 2:
# Input: root = [3, 1, 4, null, null, 2]
# Output: [2, 1, 4, null, null, 3]
# Explanation: Nodes 2 and 3 were swapped; correcting them restores the BST.
#
# Constraints:
# The number of nodes in the tree is in the range [2, 1000].
# -2^31 <= Node.val <= 2^31 - 1
# Exactly two nodes' values are swapped; solve using O(1) auxiliary space (Morris)
# for the optimal approach.


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
    def recoverTree_brute(self, root: Optional[TreeNode]) -> None:
        pass

    def recoverTree_better(self, root: Optional[TreeNode]) -> None:
        pass

    def recoverTree_optimal(self, root: Optional[TreeNode]) -> None:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
#     sol.recoverTree_optimal(root)
#     print(root.val)
