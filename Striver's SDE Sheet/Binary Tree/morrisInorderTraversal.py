# mypy: disable-error-code="empty-body"
# QUESTION: Morris Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of the binary tree. Morris
# Inorder Traversal is a tree traversal algorithm aiming to achieve a space complexity of O(1)
# without recursion or an external data structure. It uses the concept of "threaded" binary
# trees, where temporary links (threads) to the inorder predecessor's right pointer are created
# and later removed during the traversal.
#
# Examples:
# Example 1:
# Input: root = [1, 4, null, 4, 2]
# Output: [4, 4, 2, 1]
# Explanation: The root 1 has a left child 4, which in turn has left child 4 and right child 2.
# Inorder (left, node, right) visits 4, 4, 2, then the root 1.
#
# Example 2:
# Input: root = [1, null, 2, 3]
# Output: [1, 3, 2]
# Explanation: The root 1 has no left child; its right child 2 has a left child 3. Inorder
# visits 1 first, then 3, then 2.
#
# Constraints:
# 1 <= Number of Nodes <= 100
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
    def morris_inorder_traversal_brute(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def morris_inorder_traversal_better(self, root: Optional[TreeNode]) -> List[int]:
        pass

    def morris_inorder_traversal_optimal(self, root: Optional[TreeNode]) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, 4, None, 4, 2])
    print(sol.morris_inorder_traversal_optimal(root))
