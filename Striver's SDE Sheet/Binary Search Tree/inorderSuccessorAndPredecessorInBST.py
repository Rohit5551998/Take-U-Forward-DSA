# mypy: disable-error-code="empty-body"
# QUESTION: Inorder successor and predecessor in BST
# Given the root node of a binary search tree (BST) and an integer key. Return the inorder
# predecessor and successor of the given key from the provided BST.
# Note: key will always be present in the given BST.
# If the predecessor or successor is missing then return -1.
#
# Examples:
# Example 1:
# Input: root = [5, 2, 10, 1, 4, 7, 12], key = 10
# Output: [7, 12]
# Explanation: The inorder traversal of the BST is [1, 2, 4, 5, 7, 10, 12]. The value just
# before 10 is 7 (its predecessor) and the value just after 10 is 12 (its successor).
#
# Example 2:
# Input: root = [5, 2, 10, 1, 4, 7, 12], key = 12
# Output: [10, -1]
# Explanation: In the inorder traversal [1, 2, 4, 5, 7, 10, 12], the value just before 12 is
# 10. Since 12 is the largest value in the BST, it has no successor, so -1 is returned.
#
# Constraints:
# 1 <= Number of Nodes <= 10^4
# 1 <= Node.val <= 10^5
# All the values Node.val are unique.


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
    def inorder_successor_and_predecessor_in_bst_brute(
        self, root: Optional[TreeNode], key: int
    ) -> List[int]:
        pass

    def inorder_successor_and_predecessor_in_bst_better(
        self, root: Optional[TreeNode], key: int
    ) -> List[int]:
        pass

    def inorder_successor_and_predecessor_in_bst_optimal(
        self, root: Optional[TreeNode], key: int
    ) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([5, 2, 10, 1, 4, 7, 12])
    key = 10
    print(sol.inorder_successor_and_predecessor_in_bst_optimal(root, key))
