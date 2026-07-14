# mypy: disable-error-code="empty-body"
# QUESTION: Introduction to Trees (Types of Binary Trees)
# A tree is a hierarchical, non-linear data structure made up of nodes, where
# each node stores data and links to child nodes. A binary tree is a tree in
# which every node has at most two children, referred to as the left child and
# the right child. This problem asks you to understand and classify the common
# types of binary trees given a description of their structure:
#   - Full Binary Tree: every node has either 0 or 2 children.
#   - Complete Binary Tree: all levels are completely filled except possibly the
#     last, and the last level is filled from left to right.
#   - Perfect Binary Tree: all internal nodes have 2 children and all leaf nodes
#     are at the same level.
#   - Balanced Binary Tree: the height is O(log N) for N nodes (the height
#     difference between left and right subtrees of every node is bounded).
#   - Degenerate (skewed) Tree: every parent has exactly one child, so the tree
#     behaves like a linked list.
# Given the number of nodes and the children-count of each node, return the
# classification (type) of the binary tree as a string.
#
# Example 1:
# Input: nodes = 3, tree = root(1) with left child 2 and right child 3
# Output: "Full Binary Tree"
# Explanation: Every node has either 0 children (nodes 2 and 3) or exactly 2
# children (node 1), so the tree is full. It is also perfect and complete.
#
# Example 2:
# Input: nodes = 3, tree = root(1) with only a left child 2, which has a left
#        child 3
# Output: "Degenerate Tree"
# Explanation: Each parent has exactly one child, so the tree is skewed and
# behaves like a linked list.
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


class Solution:
    def classify_binary_tree_brute(self, root: Optional[Node]) -> str:
        pass

    def classify_binary_tree_better(self, root: Optional[Node]) -> str:
        pass

    def classify_binary_tree_optimal(self, root: Optional[Node]) -> str:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.classify_binary_tree_optimal(Node(1, Node(2), Node(3)))
