# mypy: disable-error-code="empty-body"
# QUESTION: Check if a tree is a BST or not
# Given the root node of a binary tree, return true if the given binary
# tree is a valid binary search tree (BST), else false. A valid BST is
# defined as follows:
#   1. The left subtree of a node contains only nodes with keys strictly
#      less than the node's key.
#   2. The right subtree of a node contains only nodes with keys strictly
#      greater than the node's key.
#   3. Both the left and right subtrees must also be binary search trees.
#
# Examples:
# Example 1:
# Input: root = [2, 1, 3]
# Output: true
#
# Example 2:
# Input: root = [5, 1, 4, null, null, 3, 6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -2^31 <= Node.val <= 2^31 - 1


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

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    # Level-order build with None for missing children (LeetCode style).
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        left_val = values[i] if i < len(values) else None
        if left_val is not None:
            node.left = TreeNode(left_val)
            queue.append(node.left)
        i += 1
        right_val = values[i] if i < len(values) else None
        if right_val is not None:
            node.right = TreeNode(right_val)
            queue.append(node.right)
        i += 1
    return root


def to_level_order(root: Optional[TreeNode]) -> List[Optional[int]]:
    # Serialize to a level-order list with None markers (trailing None trimmed).
    result: List[Optional[int]] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            result.append(None)
            continue
        result.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    def check_if_a_tree_is_a_bst_or_not_brute(self, root: Optional[TreeNode]) -> bool:
        pass

    def check_if_a_tree_is_a_bst_or_not_better(self, root: Optional[TreeNode]) -> bool:
        pass

    def check_if_a_tree_is_a_bst_or_not_optimal(self, root: Optional[TreeNode]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([2, 1, 3])
    print(sol.check_if_a_tree_is_a_bst_or_not_optimal(root))
