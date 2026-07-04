# mypy: disable-error-code="empty-body"
# QUESTION: Print root to leaf path in BT
# Given the root of a binary tree, return all the root-to-leaf paths in the binary tree.
# A leaf node of a binary tree is the node which does not have a left and right child.
#
# Examples:
# Example 1:
# Input: root = [1, 2, 3, null, 5, null, 4]
# Output: [[1, 2, 5], [1, 3, 4]]
# Explanation: There are only two paths from root to leaf.
# From root 1 to leaf 5: 1 -> 2 -> 5.
# From root 1 to leaf 4: 1 -> 3 -> 4.
#
# Example 2:
# Input: root = [1, 2, 3, 4, 5]
# Output: [[1, 2, 4], [1, 2, 5], [1, 3]]
# Explanation: The leaves are 4, 5 and 3, giving the paths 1 -> 2 -> 4, 1 -> 2 -> 5 and 1 -> 3.
#
# Constraints:
# 1 <= Number of Nodes <= 3*10^3
# -10^3 <= Node.val <= 10^3


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
    def print_root_to_leaf_path_in_bt_brute(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def print_root_to_leaf_path_in_bt_better(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

    def print_root_to_leaf_path_in_bt_optimal(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 3, None, 5, None, 4])
    print(sol.print_root_to_leaf_path_in_bt_optimal(root))
