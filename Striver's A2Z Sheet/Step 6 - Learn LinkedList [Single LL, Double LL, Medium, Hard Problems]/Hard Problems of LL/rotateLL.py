# mypy: disable-error-code="empty-body"
# QUESTION: Rotate List
# Given the head of a linked list, rotate the list to the right by k places.
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Explanation: Rotating right by 2 moves the last two nodes to the front.
# Constraints:
# - 0 <= number of nodes <= 500
# - -100 <= Node.val <= 100
# - 0 <= k <= 2 * 10^9

"""
#Brute Force:
SKIPPED — repeatedly moving the last node to the front k times is O(n*k) and is
just a slower version of the same idea; not a genuinely different algorithm.

#Better Approach:
SKIPPED — no distinct middle tier; the single-pass link-and-cut method below is
the standard optimal.

#Optimal Approach:
1. Handle empty / single-node lists: nothing to rotate, return head.
2. Traverse to the last node while counting the length `cnt`. `temp` now points
   at the tail.
3. Reduce the rotations with k = k % cnt (rotating by a full length is a no-op).
   If k == 0 after the mod, return head unchanged.
4. Make the list circular by connecting the tail back to the head
   (temp.next = head).
5. The new tail sits at position (cnt - k) from the original head. Advance
   `temp` that many steps.
6. The node after the new tail is the new head. Break the circle by setting the
   new tail's next to None, then return the new head.
TC -> O(n) + O(n - n % k), SC -> O(1)

#KEY INSIGHT:
- Rotating right by k is equivalent to cutting the list open (cnt - k) nodes
  from the front. Joining the tail to the head first turns it into a ring, so
  the rotation becomes a single "walk to the break point and cut" operation.
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

    def rotateLL_brute(self) -> None:
        # SKIP: O(n*k) repeated single rotations, same idea but slower.
        pass

    def rotateLL_better(self) -> None:
        # SKIP: no distinct middle tier before the link-and-cut optimal.
        pass

    def rotateLL_optimal(self, head: Optional[Node], k: int) -> Optional[Node]:
        if head is None or head.next is None:
            return head

        cnt = 1
        temp = head
        while temp.next is not None:
            cnt += 1
            temp = temp.next

        k = k % cnt
        if k == 0:
            return head

        temp.next = head  # make it circular

        end = cnt - k
        while end:
            end -= 1
            temp = temp.next

        head = temp.next
        temp.next = None
        return head


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 4, 6, 7, 5, 1, 0]
    head = sol.convertArr2LL(arr)
    sol.printLinkedList(head)
    head = sol.rotateLL_optimal(head, 13)
    sol.printLinkedList(head)
