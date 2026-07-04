# mypy: disable-error-code="empty-body"
# QUESTION: Vertical Order Traversal
# Given a Binary Tree, return the Vertical Order Traversal of it starting
# from the leftmost vertical to the rightmost vertical. If there are
# multiple nodes passing through a vertical line, they should be ordered
# from top to bottom by their row (level), and within the same row by
# their value in ascending order.
#
# Examples:
# Example 1:
# Input: root = [3, 9, 20, null, null, 15, 7]
# Output: [[9], [3, 15], [20], [7]]
#
# Example 2:
# Input: root = [1, 2, 3, 4, 5, 6, 7]
# Output: [[4], [2], [1, 5, 6], [3], [7]]
# Explanation: Node 5 and node 6 are at the same vertical and same level,
# so they appear together sorted by value.


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
    def vertical_order_traversal_brute(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def vertical_order_traversal_better(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def vertical_order_traversal_optimal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(sol.vertical_order_traversal_optimal(root))
