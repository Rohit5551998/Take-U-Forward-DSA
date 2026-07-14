# mypy: disable-error-code="empty-body"
# QUESTION: Segregate Odd and Even Nodes in a Linked List
# Given the head of a singly linked list, group all nodes at odd positions together
# followed by all nodes at even positions (positions are 1-indexed), preserving the
# relative order within each group. Return the new head.
# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 1 -> 3 -> 5 -> 2 -> 4
# Explanation: Odd positions (1,3,5) come first, then even positions (2,4).
# Constraints:
# 0 <= number of nodes <= 10^5

"""
#Brute Force:
1. Collect values at odd positions into one array and even positions into another.
2. Overwrite the list's node values: odd-position values first, then even-position values.
TC -> O(2n), SC -> O(n).

#Better Approach:
SKIPPED — the in-place two-chain split below is optimal; no distinct middle tier.

#Optimal Approach:
1. Keep two dummy-headed chains: an odd chain and an even chain (with their tails).
2. Walk the original list; detach each node and append it to the odd or even chain based
   on its 1-indexed position parity.
3. Link the odd tail to the even head and return the odd chain's head.
TC -> O(n), SC -> O(1).

#KEY INSIGHT:
- Splicing existing nodes into two separate chains and then joining them re-links the list
  in place with only O(1) extra pointers — no value copying and no second array.
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

    def segregateEvenAndOddNodes_brute(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: value-copy array method is naive; next step is optimal
        pass

    def segregateEvenAndOddNodes_better(self, head: Optional[Node]) -> Optional[Node]:
        # SKIP: no distinct middle tier
        pass

    def segregateEvenAndOddNodes_optimal(self, head: Optional[Node]) -> Optional[Node]:
        oddHead, evenHead = Node(-1), Node(-1)
        oddTail, evenTail = oddHead, evenHead
        curr = head
        cnt = 0
        while curr is not None:
            cnt += 1
            temp = curr
            curr = curr.next
            temp.next = None
            if cnt % 2 == 1:
                oddTail.next = temp
                oddTail = oddTail.next
            else:
                evenTail.next = temp
                evenTail = evenTail.next
        oddTail.next = evenHead.next
        return oddHead.next


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    head = sol.segregateEvenAndOddNodes_optimal(head)
    sol.printLinkedList(head)
