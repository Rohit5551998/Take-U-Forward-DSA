# mypy: disable-error-code="empty-body"
# QUESTION: Flatten Binary Tree to Linked List
# Given the root of a Binary Tree, flatten it to a linked list in-place.
# The "linked list" should use the same TreeNode class where:
#   - The right child pointer points to the next node in the list.
#   - The left child pointer is always null.
# The linked list should follow the same order as the pre-order traversal
# of the binary tree.
#
# Examples:
# Example 1:
# Input: root = [1, 2, 5, 3, 4, null, 6]
# Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6]
#
# Example 2:
# Input: root = []
# Output: []
#
# Constraints:
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
#
# Follow up: Can you flatten the tree in-place (with O(1) extra space)?


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
    def flatten_binary_tree_to_linked_list_brute(self, root: Optional[TreeNode]) -> None:
        pass

    def flatten_binary_tree_to_linked_list_better(self, root: Optional[TreeNode]) -> None:
        pass

    def flatten_binary_tree_to_linked_list_optimal(self, root: Optional[TreeNode]) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 5, 3, 4, None, 6])
    sol.flatten_binary_tree_to_linked_list_optimal(root)
    print(to_level_order(root))
