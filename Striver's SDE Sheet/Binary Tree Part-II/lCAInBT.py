# mypy: disable-error-code="empty-body"
# QUESTION: LCA in BT
# Given the root of a binary tree, find the lowest common ancestor (LCA)
# of two given nodes (p, q) in the tree. The lowest common ancestor is
# defined between two nodes p and q as the lowest node in the tree that
# has both p and q as descendants (where we allow a node to be a
# descendant of itself).
#
# Examples:
# Example 1:
# Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 1
# Output: 3
#
# Example 2:
# Input: root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], p = 5, q = 4
# Output: 5
# Explanation: Node 5 is an ancestor of node 4 (and of itself).
#
# Constraints:
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique. p != q. p and q both exist in the tree.


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
    def lca_in_bt_brute(self, root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
        pass

    def lca_in_bt_better(self, root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
        pass

    def lca_in_bt_optimal(self, root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = 5
    q = 1
    ans = sol.lca_in_bt_optimal(root, p, q)
    print(ans.val if ans else None)
