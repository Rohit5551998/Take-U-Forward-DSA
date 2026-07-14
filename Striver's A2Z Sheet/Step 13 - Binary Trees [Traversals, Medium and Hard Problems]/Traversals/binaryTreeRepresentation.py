# mypy: disable-error-code="empty-body"
# QUESTION: Binary Tree Representation in Python
# Represent a binary tree node using a class with a value and pointers to its
# left and right children. Build a tree from these nodes and understand how the
# structure is stored in memory.
#
# Example 1:
# Input: root value = 1, left child = 2, right child = 3
# Output: A tree with root 1, whose left is 2 and right is 3
# Explanation: Each node holds data plus references to up to two children.
#
# Constraints:
# The number of nodes is in the range [0, 10^4].
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

from typing import Optional


class Node:
    def __init__(
        self,
        val: int,
        left: "Optional[Node]" = None,
        right: "Optional[Node]" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


# if __name__ == "__main__":
#     root = Node(1, Node(2), Node(3))
#     print(root.val, root.left.val, root.right.val)
