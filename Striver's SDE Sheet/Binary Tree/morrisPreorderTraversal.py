# mypy: disable-error-code="empty-body"
# QUESTION: Morris Preorder Traversal
# Given the root of a binary tree, return the preorder traversal of the binary tree.
# Morris Preorder Traversal is a tree traversal algorithm aiming to achieve a space complexity
# of O(1) without recursion or an external data structure.
#
# Examples:
# Example 1:
# Input: root = [1, 4, null, 4, 2]
# Output: [1, 4, 4, 2]
# Explanation: Root 1 is visited first, then its left child 4, then that node's left child 4,
# then its right child 2. The root has no right subtree.
#
# Example 2:
# Input: root = [1]
# Output: [1]
# Explanation: Only root node is present.
#
# Constraints:
# 1 <= Number of Nodes <= 100
# -100 <= Node.val <= 100


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
    def morris_preorder_traversal_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def morris_preorder_traversal_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def morris_preorder_traversal_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 4, None, 4, 2])
    print(sol.morris_preorder_traversal_optimal(root))
