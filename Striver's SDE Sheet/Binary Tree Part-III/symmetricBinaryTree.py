# mypy: disable-error-code="empty-body"
# QUESTION: Symmetric Binary Tree
# Given the root of a Binary Tree, determine whether the tree is symmetric
# (a mirror of itself around its center). A Binary Tree is Symmetric when
# its mirror image is exactly the same as the original tree. If we draw a
# vertical line through the root, the left and right subtrees should be
# mirror images of each other in both structure and node values.
#
# Examples:
# Example 1:
# Input: root = [1, 2, 2, 3, 4, 4, 3]
# Output: true
#
# Example 2:
# Input: root = [1, 2, 2, null, 3, null, 3]
# Output: false
#
# Constraints:
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
# Note: This appears twice in the SDE sheet (Day 19) — identical problem
# to `checkForSymmetricalBTs.py`.


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
    def symmetric_binary_tree_brute(self, root: Optional[TreeNode]) -> bool:
        pass

    def symmetric_binary_tree_better(self, root: Optional[TreeNode]) -> bool:
        pass

    def symmetric_binary_tree_optimal(self, root: Optional[TreeNode]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 2, 3, 4, 4, 3])
    print(sol.symmetric_binary_tree_optimal(root))
