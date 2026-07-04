# mypy: disable-error-code="empty-body"
# QUESTION: Two sum in BST
# Given the root of a Binary Search Tree and an integer k, return true if there exist two
# elements in the BST such that their sum is equal to k, or false otherwise.
#
# Examples:
# Input:Binary Search Tree: 5 3 6 2 4 -1 7, K = 9
#
# Output: True
#
# Input:Binary Search Tree: 7 3 10 2 6 9 11 1 5 8 -1 -1 -1 -1 -1 4 -1 -1 -1
#
# Output : True
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
    def two_sum_in_bst_brute(self, root: Optional[TreeNode], k: int) -> bool:
        pass

    def two_sum_in_bst_better(self, root: Optional[TreeNode], k: int) -> bool:
        pass

    def two_sum_in_bst_optimal(self, root: Optional[TreeNode], k: int) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    k = 9
    print(sol.two_sum_in_bst_optimal(root, k))
