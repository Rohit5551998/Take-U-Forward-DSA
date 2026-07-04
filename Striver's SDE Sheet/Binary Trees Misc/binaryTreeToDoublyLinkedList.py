# mypy: disable-error-code="empty-body"
# QUESTION: Binary Tree to Doubly Linked List
# Given a Binary Tree, convert it into a Doubly Linked List (DLL) in-place.
# The conversion should maintain the in-order traversal order of the
# binary tree. In the resulting DLL:
#   - The `left` pointer of each node should point to the previous node.
#   - The `right` pointer of each node should point to the next node.
#   - The head of the DLL should be the leftmost (smallest in-order) node
#     of the tree.
#
# Examples:
# Example 1:
# Input: root = [10, 12, 15, 25, 30, 36]
# Output (DLL): 25 ↔ 12 ↔ 30 ↔ 10 ↔ 36 ↔ 15
# Explanation: In-order traversal of the tree is the DLL order.
#
# Example 2:
# Input: root = [1, 2, 3]
# Output (DLL): 2 ↔ 1 ↔ 3
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
# -10^4 <= Node.val <= 10^4
#
# Follow up: Can you do it in O(n) time using only O(h) recursion-stack
# space (where h is the tree height)?


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


class Solution:
    def binary_tree_to_doubly_linked_list_brute(
        self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        pass

    def binary_tree_to_doubly_linked_list_better(
        self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        pass

    def binary_tree_to_doubly_linked_list_optimal(
        self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([10, 12, 15, 25, 30, 36])
    head = sol.binary_tree_to_doubly_linked_list_optimal(root)
    out = []
    node = head
    while node is not None:
        out.append(node.val)
        node = node.right
    print(out)
