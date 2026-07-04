# mypy: disable-error-code="empty-body"
# QUESTION: Ceil in a BST
# Given the root of a binary search tree and a key value, find the ceil
# value for that key.
# Ceil Value Node: The node with the smallest value greater than or equal
# to the key value. If no such node exists, return -1.
#
# Examples:
# Example 1:
# Input: root = [8, 4, 12, 2, 6, 10, 14], key = 11
# Output: 12
# Explanation: 12 is the smallest value in the BST ≥ 11.
#
# Example 2:
# Input: root = [8, 4, 12, 2, 6, 10, 14], key = 15
# Output: -1
# Explanation: No node has value ≥ 15.
#
# Constraints:
# 1 <= number of nodes in BST <= 10^5
# 1 <= node value <= 10^5


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
    def ceil_in_a_bst_brute(self, root: Optional[TreeNode], key: int) -> int:
        pass

    def ceil_in_a_bst_better(self, root: Optional[TreeNode], key: int) -> int:
        pass

    def ceil_in_a_bst_optimal(self, root: Optional[TreeNode], key: int) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([8, 4, 12, 2, 6, 10, 14])
    key = 11
    print(sol.ceil_in_a_bst_optimal(root, key))
