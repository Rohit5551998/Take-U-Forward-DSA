# mypy: disable-error-code="empty-body"
# QUESTION: Construct a BST from a preorder traversal
# Given an array of integers `preorder`, which represents the preorder
# traversal of a BST, construct the tree and return its root. It is
# guaranteed that it is always possible to find a binary search tree with
# the given requirements for the test cases.
# A binary search tree is a binary tree where for every node:
#   - Values strictly less than the node are in its left subtree.
#   - Values strictly greater than the node are in its right subtree.
# A preorder traversal of a binary tree first displays the value of the
# node, then traverses the left subtree, then the right subtree.
#
# Examples:
# Example 1:
# Input: preorder = [8, 5, 1, 7, 10, 12]
# Output: [8, 5, 10, 1, 7, null, 12]
#
# Example 2:
# Input: preorder = [1, 3]
# Output: [1, null, 3]
#
# Constraints:
# 1 <= preorder.length <= 100
# 1 <= preorder[i] <= 10^8
# All the values of preorder are unique.


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
    def construct_a_bst_from_a_preorder_traversal_brute(
        self, preorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def construct_a_bst_from_a_preorder_traversal_better(
        self, preorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def construct_a_bst_from_a_preorder_traversal_optimal(
        self, preorder: List[int]
    ) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    preorder = [8, 5, 1, 7, 10, 12]
    print(to_level_order(sol.construct_a_bst_from_a_preorder_traversal_optimal(preorder)))
