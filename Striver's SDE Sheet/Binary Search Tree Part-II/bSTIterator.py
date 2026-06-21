# QUESTION: BST iterator
# Implement the BSTIterator class that represents an iterator over the
# in-order traversal of a binary search tree (BST):
#   BSTIterator(TreeNode root) — Initializes an object. The pointer should
#       be initialized to a non-existent number smaller than any element
#       in the BST.
#   boolean hasNext() — Returns true if there exists a number in the
#       traversal to the right of the pointer, otherwise returns false.
#   int next() — Moves the pointer to the right, then returns the number
#       at the pointer.
# Notice that calling next() immediately after construction should return
# the smallest element in the BST.
#
# Examples:
# Example 1:
# Input:
# ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
# Output: [null, 3, 7, true, 9, true, 15, true, 20, false]
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to hasNext and next.
#
# Follow up: Could you implement next() and hasNext() to run in average
# O(1) time and use O(h) memory, where h is the height of the tree?


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


def bst_iterator_brute() -> None:
    pass


def bst_iterator_better() -> None:
    pass


def bst_iterator_optimal() -> None:
    pass
