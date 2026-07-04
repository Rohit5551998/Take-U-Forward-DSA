# mypy: disable-error-code="empty-body"
# QUESTION: Diameter of Binary Tree
# Given the root of the Binary Tree, return the length of its diameter.
# The diameter of a binary tree is the length of the longest path between
# any two nodes in the tree. This path may or may not pass through the
# root. The length of a path is the number of edges between its endpoints.
#
# Examples:
# Example 1:
# Input: root = [1, 2, 3, 4, 5]
# Output: 3
# Explanation: The longest path is [4, 2, 1, 3] or [5, 2, 1, 3], length 3.
#
# Example 2:
# Input: root = [1, 2]
# Output: 1
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^4].
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
    def diameter_of_binary_tree_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def diameter_of_binary_tree_better(self, root: Optional[TreeNode]) -> int:
        pass

    def diameter_of_binary_tree_optimal(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 3, 4, 5])
    print(sol.diameter_of_binary_tree_optimal(root))
