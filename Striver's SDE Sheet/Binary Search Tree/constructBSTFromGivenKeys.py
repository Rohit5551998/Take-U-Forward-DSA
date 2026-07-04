# mypy: disable-error-code="empty-body"
# QUESTION: Construct BST from given keys
# Given an integer array `nums` where the elements are sorted in ascending
# order, convert it to a height-balanced binary search tree. A
# height-balanced binary tree is a binary tree in which the depth of the
# two subtrees of every node never differs by more than one.
#
# Examples:
# Example 1:
# Input: nums = [-10, -3, 0, 5, 9]
# Output: [0, -3, 9, -10, null, 5]
# Explanation: [0, -10, 5, null, -3, null, 9] is also a valid answer.
#
# Example 2:
# Input: nums = [1, 3]
# Output: [3, 1] (or [1, null, 3])
#
# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums is sorted in a strictly increasing order.


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
    def construct_bst_from_given_keys_brute(self, nums: List[int]) -> Optional[TreeNode]:
        pass

    def construct_bst_from_given_keys_better(self, nums: List[int]) -> Optional[TreeNode]:
        pass

    def construct_bst_from_given_keys_optimal(self, nums: List[int]) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [-10, -3, 0, 5, 9]
    print(to_level_order(sol.construct_bst_from_given_keys_optimal(nums)))
