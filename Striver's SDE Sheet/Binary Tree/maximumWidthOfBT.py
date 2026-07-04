# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Width of BT
# Given a Binary Tree, return its maximum width. The maximum width of a
# Binary Tree is the maximum diameter among all its levels. The width or
# diameter of a level is the number of nodes between the leftmost and
# rightmost non-null nodes on that level, where the count INCLUDES any null
# nodes between them (as if the tree were full / heap-indexed).
#
# Examples:
# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width is between nodes 5 and 9 on level 3 (4 positions).
#
# Example 2:
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 8
# Explanation: The maximum width is between nodes 6 and 7 on level 4 (8 positions).
#
# Constraints:
# The number of nodes in the tree is in the range [1, 3000].
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
    def maximum_width_of_bt_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def maximum_width_of_bt_better(self, root: Optional[TreeNode]) -> int:
        pass

    def maximum_width_of_bt_optimal(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 3, 2, 5, 3, None, 9])
    print(sol.maximum_width_of_bt_optimal(root))
