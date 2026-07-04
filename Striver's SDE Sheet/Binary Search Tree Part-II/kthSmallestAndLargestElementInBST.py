# mypy: disable-error-code="empty-body"
# QUESTION: Kth Smallest and Largest element in BST
# Given the root node of a binary search tree (BST) and an integer k. Return the kth smallest
# and largest value (1-indexed) of all values of the nodes in the tree. Return the 1st integer
# as the kth smallest and the 2nd integer as the kth largest in the returned array.
#
# Examples:
# Example 1:
# Input: root = [3, 1, 4, null, 2], k = 1
# Output: [1, 4]
# Explanation:
# The 1st smallest value in the given BST is 1.
# The 1st largest value in the given BST is 4.
#
# Example 2:
# Input: root = [5, 3, 6, 2, null, null, null, 1], k = 3
# Output: [3, 3]
# Explanation:
# The 3rd smallest value in the given BST is 3.
# The 3rd largest value in the given BST is 3.
#
# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^5


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
    def kth_smallest_and_largest_element_in_bst_brute(
        self, root: Optional[TreeNode], k: int
    ) -> List[int]:
        pass

    def kth_smallest_and_largest_element_in_bst_better(
        self, root: Optional[TreeNode], k: int
    ) -> List[int]:
        pass

    def kth_smallest_and_largest_element_in_bst_optimal(
        self, root: Optional[TreeNode], k: int
    ) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([3, 1, 4, None, 2])
    k = 1
    print(sol.kth_smallest_and_largest_element_in_bst_optimal(root, k))
