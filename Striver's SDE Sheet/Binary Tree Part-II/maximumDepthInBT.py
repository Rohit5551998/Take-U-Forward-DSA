# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Depth in BT
# Given the root of a Binary Tree, return the maximum depth (also called
# height) of the tree. The maximum depth is the number of nodes along the
# longest path from the root node down to the farthest leaf node.
#
# Examples:
# Example 1:
# Input: root = [1, 2, 5, -1, -1, 4, 6, 5]
# Output: 4
# Explanation: The longest path is 1 → 5 → 4 → 5 (4 nodes).
#
# Example 2:
# Input: root = [3, 1, 2]
# Output: 2
# Explanation: The longest path from root to a leaf has 2 nodes.
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
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
    def maximum_depth_in_bt_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def maximum_depth_in_bt_better(self, root: Optional[TreeNode]) -> int:
        pass

    def maximum_depth_in_bt_optimal(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(sol.maximum_depth_in_bt_optimal(root))
