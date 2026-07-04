# mypy: disable-error-code="empty-body"
# QUESTION: Construct a BT from Postorder and Inorder
# Given two integer arrays postorder and inorder, where postorder is the postorder traversal of
# a binary tree and inorder is the inorder traversal of the same tree, construct and return the
# binary tree using the postorder and inorder arrays.
#
# Examples:
# Example 1:
# Input: postorder = [9, 15, 7, 20, 3], inorder = [9, 3, 15, 20, 7]
# Output: [3, 9, 20, null, null, 15, 7]
# Explanation: The last postorder element 3 is the root; inorder splits the rest into the left
# subtree [9] and the right subtree [15, 20, 7], which is built recursively (20 with children
# 15 and 7).
#
# Example 2:
# Input: postorder = [5, 6, 4, 9, 2, 3], inorder = [5, 4, 6, 3, 2, 9]
# Output: [3, 4, 2, 5, 6, null, 9]
# Explanation: The last postorder element 3 is the root; inorder splits the rest into the left
# subtree [5, 4, 6] (4 with children 5 and 6) and the right subtree [2, 9] (2 with right child 9).
#
# Constraints:
# 1 <= Number of Nodes <= 3000
# -10^4 <= Node.val <= 10^4
# All values in the given tree are unique.
# Each value of inorder also appears in postorder.
# Postorder is guaranteed to be the postorder traversal of the tree.
# Inorder is guaranteed to be the inorder traversal of the tree.


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
    def construct_a_bt_from_postorder_and_inorder_brute(
        self, postorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def construct_a_bt_from_postorder_and_inorder_better(
        self, postorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        pass

    def construct_a_bt_from_postorder_and_inorder_optimal(
        self, postorder: List[int], inorder: List[int]
    ) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    postorder = [9, 15, 7, 20, 3]
    inorder = [9, 3, 15, 20, 7]
    print(to_level_order(sol.construct_a_bt_from_postorder_and_inorder_optimal(postorder, inorder)))
