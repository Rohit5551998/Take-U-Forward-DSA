# mypy: disable-error-code="empty-body"
# QUESTION: Postorder Traversal
# Given the root of a Binary Tree, create a function that performs a postorder traversal
# using two stacks and returns an array containing the traversal sequence.
#
# Examples:
# Example 1:
# Input: Binary Tree: 4 2 5 3 -1 7 6 -1 9 -1 -1 8 -1 1
# Output: [1, 9, 3, 2, 7, 8, 6, 5, 4]
# Explanation: We traverse the binary tree in Left, Right, Root order recursively. This
# results in the following traversal:
# 1 → 9 → 3 → 2 → 7 → 8 → 6 → 5 → 4.
#
# Example 2:
# Input: Binary Tree: 1 2 3 4 5 6 7 -1 -1 8 -1 -1 -1 9 10
# Output: [1, 2, 4, 5, 8, 3, 6, 7, 9, 10]
# Explanation: We traverse the binary tree in Left, Right, Root order recursively. This
# results in the following traversal:
# 1 → 2 → 4 → 5 → 8 → 3 → 6 → 7 → 9 → 10.


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
    def postorder_traversal_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def postorder_traversal_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def postorder_traversal_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 3, 4, 5, None, 6])
    print(sol.postorder_traversal_optimal(root))
