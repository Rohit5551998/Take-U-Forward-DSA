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


class Solution:
    def construct_a_bt_from_postorder_and_inorder_brute(self) -> None:
        pass

    def construct_a_bt_from_postorder_and_inorder_better(self) -> None:
        pass

    def construct_a_bt_from_postorder_and_inorder_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
