# mypy: disable-error-code="empty-body"
# QUESTION: Populating Next Right Pointers in Each Node
# You are given a perfect binary tree where:
#   - All leaves are on the same level.
#   - Every parent has exactly two children.
# Each node has the structure:
#   struct Node { int val; Node *left; Node *right; Node *next; }
# Populate each `next` pointer so that it points to its next right node on
# the same level. If there is no next right node, the next pointer should
# be set to NULL. Initially, all next pointers are set to NULL.
#
# Examples:
# Example 1:
# Input: root = [1, 2, 3, 4, 5, 6, 7]
# Output: [1, #, 2, 3, #, 4, 5, 6, 7, #]
# Explanation: Each level's nodes are connected via next pointers; the
# last node of each level points to NULL (shown as #).
#
# Example 2:
# Input: root = []
# Output: []
#
# Constraints:
# The number of nodes in the tree is in the range [0, 2^12 - 1].
# -1000 <= Node.val <= 1000
#
# Follow up: You may only use constant extra space. Recursive approaches
# are fine — implicit stack memory does not count as extra space.


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
        next: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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
    def populating_next_right_pointers_in_each_node_brute(
        self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        pass

    def populating_next_right_pointers_in_each_node_better(
        self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        pass

    def populating_next_right_pointers_in_each_node_optimal(
        self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 3, 4, 5, 6, 7])
    print(to_level_order(sol.populating_next_right_pointers_in_each_node_optimal(root)))
