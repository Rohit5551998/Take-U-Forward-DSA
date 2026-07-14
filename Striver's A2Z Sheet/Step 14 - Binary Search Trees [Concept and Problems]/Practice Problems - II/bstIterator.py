# mypy: disable-error-code="empty-body"
# QUESTION: Binary Search Tree Iterator
# Implement the BSTIterator class that represents an iterator over the inorder
# traversal of a Binary Search Tree:
#   - BSTIterator(root): initialize the iterator; the pointer starts before the
#     smallest element.
#   - next() -> int: move the pointer to the next element (inorder) and return it.
#   - hasNext() -> bool: return True if there exists a next element, else False.
# next() and hasNext() should run in average O(1) time using O(h) memory, where h
# is the height of the tree, by keeping a controlled stack of pending nodes.
#
# Example 1:
# Input:
#   BSTIterator([7, 3, 15, null, null, 9, 20])
#   next(); next(); hasNext(); next(); hasNext()
# Output: 3, 7, True, 9, True
# Explanation: Inorder is [3, 7, 9, 15, 20]; the iterator yields them in order.
#
# Constraints:
# The number of nodes in the tree is in the range [1, 10^5].
# 0 <= Node.val <= 10^6
# At most 10^5 calls will be made to next() and hasNext().


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


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "Optional[TreeNode]" = None,
        right: "Optional[TreeNode]" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]) -> None:
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass


# if __name__ == "__main__":
#     root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
#     it = BSTIterator(root)
#     out: List[int] = []
#     while it.hasNext():
#         out.append(it.next())
#     print(out)
