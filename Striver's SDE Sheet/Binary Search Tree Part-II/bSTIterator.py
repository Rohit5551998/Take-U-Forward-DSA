# mypy: disable-error-code="empty-body"
# QUESTION: BST iterator
# Implement the BSTIterator class that represents an iterator over the
# in-order traversal of a binary search tree (BST):
#   BSTIterator(TreeNode root) — Initializes an object. The pointer should
#       be initialized to a non-existent number smaller than any element
#       in the BST.
#   boolean hasNext() — Returns true if there exists a number in the
#       traversal to the right of the pointer, otherwise returns false.
#   int next() — Moves the pointer to the right, then returns the number
#       at the pointer.
# Notice that calling next() immediately after construction should return
# the smallest element in the BST.
#
# Examples:
# Example 1:
# Input:
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext",
#  "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output: [null, 3, 7, true, 9, true, 15, true, 20, false]
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to hasNext and next.
#
# Follow up: Could you implement next() and hasNext() to run in average
# O(1) time and use O(h) memory, where h is the height of the tree?


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


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        pass

    def next(self) -> int:
        pass

    def has_next(self) -> bool:
        pass


if __name__ == "__main__":
    it = BSTIterator(build_tree([7, 3, 15, None, None, 9, 20]))
    print(it.next())
    print(it.next())
    print(it.has_next())
    print(it.next())
    print(it.has_next())
