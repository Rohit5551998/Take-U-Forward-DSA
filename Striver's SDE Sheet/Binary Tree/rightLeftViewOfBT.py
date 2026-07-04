# mypy: disable-error-code="empty-body"
# QUESTION: Right/Left View of BT
# Given the root of a binary tree, imagine yourself standing on the right
# (or left) side of it. Return the values of the nodes you can see ordered
# from top to bottom. The Right View shows the rightmost node at each
# level; the Left View shows the leftmost node at each level.
#
# Examples:
# Example 1:
# Input: root = [1, 2, 3, null, 5, null, 4]
# Output (Right View): [1, 3, 4]
# Output (Left View):  [1, 2, 5]
#
# Example 2:
# Input: root = [1, null, 3]
# Output (Right View): [1, 3]
# Output (Left View):  [1, 3]
#
# Constraints:
# The number of nodes in the tree is in the range [0, 100].
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
    def right_left_view_of_bt_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def right_left_view_of_bt_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def right_left_view_of_bt_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 3, None, 5, None, 4])
    print(sol.right_left_view_of_bt_optimal(root))
