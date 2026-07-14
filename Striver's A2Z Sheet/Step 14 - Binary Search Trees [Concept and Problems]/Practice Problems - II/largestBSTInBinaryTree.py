# mypy: disable-error-code="empty-body"
# QUESTION: Largest BST in a Binary Tree
# Given the root of a binary tree (not necessarily a BST), find the size (number of
# nodes) of the largest subtree that is itself a valid Binary Search Tree. A subtree
# qualifies when every node in it obeys the BST property. Solve it bottom-up: for
# each node combine information from its children (min, max, size, and whether each
# child subtree is a BST) to decide if the subtree rooted here is a BST.
#
# Example 1:
# Input: root = [10, 5, 15, 1, 8, null, 7]
# Output: 3
# Explanation: The subtree [5, 1, 8] is the largest valid BST, of size 3. The whole
# tree is not a BST because 7 sits in 15's subtree but is < 10.
#
# Example 2:
# Input: root = [5, 2, 4, 1, 3]
# Output: 2
# Explanation: The largest BST subtree has 2 nodes.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# -10^9 <= Node.val <= 10^9


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
    def largestBST_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def largestBST_better(self, root: Optional[TreeNode]) -> int:
        pass

    def largestBST_optimal(self, root: Optional[TreeNode]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     root = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(8)), TreeNode(15, None, TreeNode(7)))
#     print(sol.largestBST_optimal(root))
