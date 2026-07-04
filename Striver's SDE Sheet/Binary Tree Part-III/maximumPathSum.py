# mypy: disable-error-code="empty-body"
# QUESTION: Maximum path sum
# Given the root of a Binary Tree, determine the maximum sum achievable
# along any path within the tree. A path in a binary tree is defined as a
# sequence of nodes where each pair of adjacent nodes is connected by an
# edge. A node can appear in the sequence at most once. The path does not
# need to pass through the root. The path sum is the sum of the node
# values along the path.
#
# Examples:
# Example 1:
# Input: root = [1, 2, 3]
# Output: 6
# Explanation: The optimal path is 2 → 1 → 3, sum = 2 + 1 + 3 = 6.
#
# Example 2:
# Input: root = [-10, 9, 20, null, null, 15, 7]
# Output: 42
# Explanation: The optimal path is 15 → 20 → 7, sum = 15 + 20 + 7 = 42.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000


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
    def maximum_path_sum_brute(self, root: Optional[TreeNode]) -> int:
        pass

    def maximum_path_sum_better(self, root: Optional[TreeNode]) -> int:
        pass

    def maximum_path_sum_optimal(self, root: Optional[TreeNode]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 2, 3])
    print(sol.maximum_path_sum_optimal(root))
