# mypy: disable-error-code="empty-body"
# QUESTION: Boundary Traversal
# Given a Binary Tree, perform the boundary traversal of the tree. The
# boundary traversal visits the boundary nodes of the tree in an
# anti-clockwise direction:
#   1. The root.
#   2. The left boundary, top to bottom (excluding leaf nodes).
#   3. All leaf nodes, left to right.
#   4. The right boundary, bottom to top (excluding leaf nodes).
# If the root is a leaf node, return only [root.val].
#
# Examples:
# Example 1:
# Input: root = [1, 2, 3, 4, 5, 6, 7, null, null, 8, 9, null, null, null, null]
# Output: [1, 2, 4, 8, 9, 6, 7, 3]
#
# Example 2:
# Input: root = [1, 2, 3, null, 4, 5, 6]
# Output: [1, 2, 4, 5, 6, 3]


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
    def boundary_traversal_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def boundary_traversal_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def boundary_traversal_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9])
    print(sol.boundary_traversal_optimal(root))
