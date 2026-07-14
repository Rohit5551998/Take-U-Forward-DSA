# mypy: disable-error-code="empty-body"
# QUESTION: Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2. Merge the
# two lists into one sorted list by splicing together the nodes of the two lists,
# and return the head of the merged list.
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Constraints:
# - 0 <= number of nodes in each list <= 50
# - -100 <= Node.val <= 100
# - both lists are sorted in non-decreasing order

"""
#Brute Force:
1. Collect all values from both lists into one array.
2. Sort the array.
3. Build a fresh linked list from the sorted array.
TC -> O(N1 + N2) + O(N log N) + O(N), SC -> O(N) array + O(N) new list.

#Better Approach:
SKIPPED — the two-pointer splice below is both the better and the optimal; there
is no distinct middle tier for a two-list merge.

#Optimal Approach:
1. Create a dummy node and a `temp` tail pointer at it.
2. Walk both lists together: append the node with the smaller `data` to
   `temp.next`, advance that list's pointer and `temp`.
3. When one list is exhausted, splice the remaining (already sorted) tail of the
   other directly onto `temp.next`.
4. Return dummy.next. This reuses existing nodes, so no new allocation and O(1)
   extra space.
TC -> O(N1 + N2), SC -> O(1).

#KEY INSIGHT:
- A dummy head removes the special-case for choosing the first node, and because
  both inputs are already sorted, one linear pass picking the smaller front node
  each step produces a fully sorted result by splicing (not copying) nodes.
"""

from typing import Optional


class Node:
    def __init__(self, data: int, next1: Optional["Node"] = None) -> None:
        self.data = data
        self.next = next1


class Solution:
    def convertArr2LL(self, arr: list[int]) -> Optional[Node]:
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i], None)
            temp = temp.next
        return head

    def printLinkedList(self, head: Optional[Node]) -> None:
        temp = head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def merge2SortedLL_brute(self, head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
        vals: list[int] = []
        for h in (head1, head2):
            temp = h
            while temp is not None:
                vals.append(temp.data)
                temp = temp.next
        if not vals:
            return None
        vals.sort()
        return self.convertArr2LL(vals)

    def merge2SortedLL_better(self) -> None:
        # SKIP: two-pointer splice is both better and optimal for a two-list merge.
        pass

    def merge2SortedLL_optimal(
        self, head1: Optional[Node], head2: Optional[Node]
    ) -> Optional[Node]:
        newHead = Node(-1)
        temp = newHead
        while head1 is not None and head2 is not None:
            if head1.data < head2.data:
                temp.next = head1
                temp = temp.next
                head1 = head1.next
            else:
                temp.next = head2
                temp = temp.next
                head2 = head2.next
            temp.next = None
        temp.next = head1 if head1 is not None else head2
        return newHead.next


if __name__ == "__main__":
    sol = Solution()
    head1 = sol.convertArr2LL([0, 1, 2, 4, 5, 6, 7])
    head2 = sol.convertArr2LL([5, 6, 7, 8])
    merged = sol.merge2SortedLL_optimal(head1, head2)
    sol.printLinkedList(merged)
