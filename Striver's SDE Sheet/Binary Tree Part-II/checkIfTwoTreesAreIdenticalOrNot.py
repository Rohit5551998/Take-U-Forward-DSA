# mypy: disable-error-code="empty-body"
# QUESTION: Check if two trees are identical or not
# Given two Binary Trees, return true if the two trees are identical,
# otherwise return false. Two trees are said to be identical if for every
# pair of corresponding nodes:
#   1. Both nodes have the same value.
#   2. The left subtrees of both nodes are identical.
#   3. The right subtrees of both nodes are identical.
#
# Examples:
# Example 1:
# Input: p = [1, 2, 3, -1, -1, 4, 5], q = [1, 2, 3, -1, -1, 4, 5]
# Output: true
# Explanation: All nodes match in value and structure.
#
# Example 2:
# Input: p = [1, 2, 3, -1, -1, 4, 5], q = [1, 2, 3, -1, -1, 4]
# Output: false
# Explanation: Right subtree of node 3 differs — node 5 is missing in q.
#
# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -10^4 <= Node.val <= 10^4


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
    def check_if_two_trees_are_identical_or_not_brute(
        self, p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> bool:
        pass

    def check_if_two_trees_are_identical_or_not_better(
        self, p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> bool:
        pass

    def check_if_two_trees_are_identical_or_not_optimal(
        self, p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    p = build_tree([1, 2, 3, None, None, 4, 5])
    q = build_tree([1, 2, 3, None, None, 4, 5])
    print(sol.check_if_two_trees_are_identical_or_not_optimal(p, q))
