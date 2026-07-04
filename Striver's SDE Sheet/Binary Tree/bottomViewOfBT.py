# mypy: disable-error-code="empty-body"
# QUESTION: Bottom view of BT
# Given a Binary Tree, return its Bottom View. The Bottom View of a Binary Tree is the set
# of nodes visible when we see the tree from the bottom.
#
# Examples:
# Example 1:
# Input:Binary Tree: 1 2 3 4 10 9 11 -1 5 -1 -1 -1 -1 -1 -1 -1 6
#
# Output:Bottom View Traversal: [4, 5, 6, 3, 11]
# Explanation: The bottom view comprises the nodes that are the last encountered nodes
# for each vertical index.
#
# Example 2:
# Input:Binary Tree: 2 7 5 2 6 -1 9 -1 -1 5 11 4 -1
#
# Output : Bottom View: [2 5 6 11 4 9]
# Explanation:


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
    def bottom_view_of_bt_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def bottom_view_of_bt_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def bottom_view_of_bt_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 3, 4, 10, 9, 11])
    print(sol.bottom_view_of_bt_optimal(root))
