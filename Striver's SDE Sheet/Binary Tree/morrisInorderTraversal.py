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


class Solution:
    def morris_inorder_traversal_brute(self) -> None:
        pass

    def morris_inorder_traversal_better(self) -> None:
        pass

    def morris_inorder_traversal_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
