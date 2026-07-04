# mypy: disable-error-code="empty-body"
# QUESTION: Children Sum Property in Binary Tree
# Given a Binary Tree, convert the value of its nodes to follow the
# Children Sum Property. The Children Sum Property in a binary tree states
# that for every node, the sum of its children's values must equal the
# node's own value (where the value of a null child is taken as 0).
# Rule: You can only INCREMENT node values; you cannot decrement them.
# You may change values any number of times, but cannot alter the tree's
# structure.
#
# Examples:
# Example 1:
# Input: Binary Tree: 2 35 10 2 3 5 2
#
# Output: Binary Tree: 45 35 10 30 5 8 2
#
# Explanation: We cannot decrement a node's value, only increment. There are many ways
# to do this, but we must ensure we only increase node values so that each node's value
# equals the sum of its left and right children.
#
# Example 2:
# Input: Binary Tree: 50 7 2 3 5 1 30
#
# Output : Binary Tree: 50 55 5 86 1 31 30
#
# Explanation: We modify the tree so each node's value becomes the sum of its left and
# right children. If a child's parent has a greater value, since we cannot decrease the
# parent, we increase the children's values so the tree follows the children sum property.


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
    def children_sum_property_in_binary_tree_brute(self, root: Optional[TreeNode]) -> None:
        pass

    def children_sum_property_in_binary_tree_better(self, root: Optional[TreeNode]) -> None:
        pass

    def children_sum_property_in_binary_tree_optimal(self, root: Optional[TreeNode]) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([2, 35, 10, 2, 3, 5, 2])
    sol.children_sum_property_in_binary_tree_optimal(root)
    print(to_level_order(root))
