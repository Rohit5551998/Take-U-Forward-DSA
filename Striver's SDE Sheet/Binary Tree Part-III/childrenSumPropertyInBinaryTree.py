# QUESTION: Children Sum Property in Binary Tree
# Given a Binary Tree, convert the value of its nodes to follow the
# Children Sum Property. The Children Sum Property in a binary tree states
# that for every node, the sum of its children's values must equal the
# node's own value (where the value of a null child is taken as 0).
# Rule: You can only INCREMENT node values; you cannot decrement them.
# You may change values any number of times, but cannot alter the tree's
# structure.
#
# Examples:
# Example 1:
# Input: Binary Tree: 2 35 10 2 3 5 2
#
# Output: Binary Tree: 45 35 10 30 5 8 2
#
# Explanation: We cannot decrement the value of the node but only increment. There are many different ways to do this but we have to ensure that we are only increasing the values of the nodes in such a way that its value is equal to the sum of its left and right children.
#
# Example 2:
# Input: Binary Tree: 50 7 2 3 5 1 30
#
# Output : Binary Tree: 50 55 5 86 1 31 30
#
# Explanation: We modify the tree in such a way that the value of each node becomes the value of its left and right children. If a node is a left or right child and its parent is of a greater value, since we cannot decrease the value of the parent, we increase the value of the children nodes so that the Binary Tree follows the children sum property.


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
    def children_sum_property_in_binary_tree_brute(self) -> None:
        pass

    def children_sum_property_in_binary_tree_better(self) -> None:
        pass

    def children_sum_property_in_binary_tree_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
