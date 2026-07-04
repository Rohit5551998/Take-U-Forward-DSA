# mypy: disable-error-code="empty-body"
# QUESTION: Construct a BT from Preorder and Inorder
# Given the Preorder and Inorder traversal of a Binary Tree, construct the unique Binary
# Tree represented by them.
#
# Examples:
# Input : preorder = [3, 9, 20, 15, 7] , inorder = [9, 3, 15, 20, 7]
# Output : [3, 9, 20, null, null, 15, 7]
# Explanation : The output tree is shown below.
#
# Input : preorder = [3, 4, 5, 6, 2, 9] , inorder = [5, 4, 6, 3, 2, 9]
# Output : [3, 4, 2, 5, 6, null, 9]
# Explanation : The output tree is shown below.


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
    def construct_a_bt_from_preorder_and_inorder_brute(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def construct_a_bt_from_preorder_and_inorder_better(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def construct_a_bt_from_preorder_and_inorder_optimal(
        self, preorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    print(to_level_order(sol.construct_a_bt_from_preorder_and_inorder_optimal(preorder, inorder)))
