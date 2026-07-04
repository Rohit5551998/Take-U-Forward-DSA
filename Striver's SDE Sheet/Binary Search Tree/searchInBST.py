# mypy: disable-error-code="empty-body"
# QUESTION: Search in BST
# Given a Binary Search Tree and a key value, return the node in the BST having data equal
# to 'key', otherwise return null.
#
# Examples:
# Input :8 5 12 4 7 10 14 -1 -1 6 -1 -1 -1 13 -1, Key = 10
# Output :True
#
# Input :4 2 6 1 3 5 7, Key = 3
#
# Output :false
# Explanation :


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
    def search_in_bst_brute(self, root: Optional[TreeNode], key: int) -> bool:
        pass

    def search_in_bst_better(self, root: Optional[TreeNode], key: int) -> bool:
        pass

    def search_in_bst_optimal(self, root: Optional[TreeNode], key: int) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([8, 5, 12, 4, 7, 10, 14])
    key = 10
    print(sol.search_in_bst_optimal(root, key))
