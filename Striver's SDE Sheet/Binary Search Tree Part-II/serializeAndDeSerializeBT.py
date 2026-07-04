# mypy: disable-error-code="empty-body"
# QUESTION: Serialize and De-serialize BT
# Given a Binary Tree, design an algorithm to serialize and deserialize it.
# Serialization is the process of converting a tree into a sequence of bits
# so that it can be stored in a file or memory buffer, or transmitted
# across a network. There is no restriction on HOW the serialization and
# deserialization takes place. You just need to ensure that a binary tree
# can be serialized to a string, and that string can be deserialized to
# reconstruct the original tree structure exactly.
#
# Examples:
# Example 1:
# Input:  root = [1, 2, 3, null, null, 4, 5]
# Output: [1, 2, 3, null, null, 4, 5]
# Explanation: serialize(root) -> "1,2,3,#,#,4,5,#,#,#,#" (or any encoding);
# deserialize(s) must reconstruct an identical tree.
#
# Example 2:
# Input: root = []
# Output: []
#
# Constraints:
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
#
# Note: Striver groups this with BST problems, though it applies to any
# binary tree (the value ordering of BST nodes isn't required by the
# encoding).


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


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        pass

    def deserialize(self, data: str) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    codec = Codec()
    tree = build_tree([1, 2, 3, None, None, 4, 5])
    data = codec.serialize(tree)
    print(to_level_order(codec.deserialize(data)))
