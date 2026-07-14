# mypy: disable-error-code="empty-body"
# QUESTION: Delete a Given Node in a Linked List (O(1) approach)
# You are given direct access to a node (not the head) in a singly linked list, and
# you must delete that node. The given node is guaranteed NOT to be the tail node,
# and the list has at least two nodes. You do not have access to the head of the list.
# Example 1:
# Input: head = 1 -> 2 -> 3 -> 4 -> 5, node = the node with value 3
# Output: 1 -> 2 -> 4 -> 5
# Explanation: The node with value 3 is removed; only that node reference is supplied.
# Example 2:
# Input: head = 4 -> 5 -> 1 -> 9, node = the node with value 5
# Output: 4 -> 1 -> 9
# Constraints:
# 2 <= number of nodes <= 1000
# The given node is not the tail and is an actual node in the list.

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

from typing import List, Optional


class Node:
    def __init__(self, data: int, next1: Optional["Node"] = None) -> None:
        self.data = data
        self.next = next1


class Solution:
    def convertArr2LL(self, arr: List[int]) -> Optional[Node]:
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next
        return head

    def printLinkedList(self, head: Optional[Node]) -> None:
        temp = head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def deleteGivenNode_brute(self, node: Node) -> None:
        pass

    def deleteGivenNode_better(self, node: Node) -> None:
        pass

    def deleteGivenNode_optimal(self, node: Node) -> None:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     head = sol.convertArr2LL([1, 2, 3, 4, 5])
#     target = head.next.next  # node with value 3
#     sol.deleteGivenNode_optimal(target)
#     sol.printLinkedList(head)
