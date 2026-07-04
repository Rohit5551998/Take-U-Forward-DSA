# mypy: disable-error-code="empty-body"
# QUESTION: Pre, Post, Inorder in one traversal
# Given a binary tree with root node, return the In-order, Pre-order and Post-order traversal
# of the binary tree — computed by making just one traversal of the tree.
#
# Examples:
# Example 1:
# Input: root = [1, 3, 4, 5, 2, 7, 6]
# Output: [[5, 3, 2, 1, 7, 4, 6], [1, 3, 5, 2, 4, 7, 6], [5, 2, 3, 7, 6, 4, 1]]
# Explanation: The In-order traversal is [5, 3, 2, 1, 7, 4, 6].
# The Pre-order traversal is [1, 3, 5, 2, 4, 7, 6].
# The Post-order traversal is [5, 2, 3, 7, 6, 4, 1].
#
# Example 2:
# Input: root = [1, 2, 3, null, null, null, 6]
# Output: [[2, 1, 3, 6], [1, 2, 3, 6], [2, 6, 3, 1]]
# Explanation: The In-order traversal is [2, 1, 3, 6].
# The Pre-order traversal is [1, 2, 3, 6].
# The Post-order traversal is [2, 6, 3, 1].
#
# Constraints:
# 1 <= Number of Nodes <= 10^5
# 0 <= Node.val <= 10^5


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
    def pre_post_inorder_in_one_traversal_brute(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def pre_post_inorder_in_one_traversal_better(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def pre_post_inorder_in_one_traversal_optimal(
        self, root: Optional[TreeNode]
    ) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 3, 4, 5, 2, 7, 6])
    print(sol.pre_post_inorder_in_one_traversal_optimal(root))
