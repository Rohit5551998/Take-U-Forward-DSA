# mypy: disable-error-code="empty-body"
# QUESTION: Size of the largest BST in a Binary Tree
# Given the root of a Binary Tree, where each node has an integer value,
# return the size (number of nodes) of the largest subtree that is also a
# valid Binary Search Tree (BST). A BST is a binary tree where for every
# node:
#   - All nodes in its left subtree have values strictly less than the
#     node's value.
#   - All nodes in its right subtree have values strictly greater than the
#     node's value.
#   - Both subtrees are themselves BSTs.
#
# Examples:
# Example 1:
# Input: root = [10, 5, 15, 1, 8, null, 7]
# Output: 3
# Explanation: The largest BST subtree is rooted at node 5 with values
# {1, 5, 8} — size 3.
#
# Example 2:
# Input: root = [4, 2, 7, 1, 3]
# Output: 5
# Explanation: The whole tree is itself a BST.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
#
# Follow up: Can you solve it in O(n) time using a single post-order
# traversal that returns (size, min, max, is-bst) per subtree?


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
    def size_of_the_largest_bst_in_a_binary_tree_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def size_of_the_largest_bst_in_a_binary_tree_better(self, root: Optional[TreeNode]) -> int:
        pass

    def size_of_the_largest_bst_in_a_binary_tree_optimal(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([10, 5, 15, 1, 8, None, 7])
    print(sol.size_of_the_largest_bst_in_a_binary_tree_optimal(root))
