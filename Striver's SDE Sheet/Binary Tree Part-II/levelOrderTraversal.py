# mypy: disable-error-code="empty-body"
# QUESTION: Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values
# (i.e., from left to right, level by level).
#
# Examples:
# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: [[3], [9, 20], [15, 7]]
# Explanation: Level 0 has the root 3, level 1 has its children 9 and 20, and level 2 has
# 20's children 15 and 7.
#
# Example 2:
# Input: root = [1, 4, null, 4, 2]
# Output: [[1], [4], [4, 2]]
# Explanation: Level 0 has the root 1, level 1 has its left child 4, and level 2 has that
# node's children 4 and 2.
#
# Constraints:
# 0 <= Number of Nodes <= 2000
# -1000 <= Node.val <= 2000


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
    def level_order_traversal_brute(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def level_order_traversal_better(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def level_order_traversal_optimal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(sol.level_order_traversal_optimal(root))
