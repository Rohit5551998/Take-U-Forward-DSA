# mypy: disable-error-code="empty-body"
# QUESTION: LCA in BST
# Given the root node of a binary search tree (BST) and two node values p, q. Return the lowest
# common ancestor (LCA) of the two nodes in the BST. The lowest common ancestor of two nodes p
# and q is the lowest node in the tree that has both p and q as descendants (a node is allowed
# to be a descendant of itself).
#
# Examples:
# Example 1:
# Input: root = [5, 3, 6, 2, 4, null, 7], p = 2, q = 4
# Output: 3
# Explanation: Nodes 2 and 4 are the left and right children of node 3, so node 3 is the lowest
# node that is an ancestor of both.
#
# Example 2:
# Input: root = [5, 3, 6, 2, 4, null, 7], p = 2, q = 7
# Output: 5
# Explanation: Node 2 lies in the left subtree of root 5 and node 7 lies in the right subtree,
# so their lowest common ancestor is the root node 5.
#
# Constraints:
# 1 <= Number of Nodes <= 10^4
# 1 <= Node.val <= 10^5
# All values in the BST are unique.
# The values p and q are always present in the given BST.


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
    def lca_in_bst_brute(self, root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
        pass

    def lca_in_bst_better(self, root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
        pass

    def lca_in_bst_optimal(self, root: Optional[TreeNode], p: int, q: int) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([5, 3, 6, 2, 4, None, 7])
    p = 2
    q = 4
    ans = sol.lca_in_bst_optimal(root, p, q)
    print(ans.val if ans else None)
