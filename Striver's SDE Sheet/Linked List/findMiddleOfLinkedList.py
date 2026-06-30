# QUESTION: Find Middle of Linked List
# Given the head of a linked list of integers, determine the middle node of the linked list. However, if the linked list has an even number of nodes, return the second middle node.
#
# Examples:
# Example 1:
# Input: LL: 1 2 3 4 5
#
# Output: 3
#
# Explanation: Node with value 3 is the middle node of this linked list.
#
# Example 2:
# Input: LL: 1 2 3 4 5 6
#
# Output: 4
#
# Explanation: In this example, the linked list has an even number of nodes hence we return the second middle node which is 4.


"""
#Brute Force:
1. We can't know the middle's position without first knowing the length, so walk
   the whole list once incrementing cnt for every node.
2. The required node is at 1-indexed position cnt // 2 + 1 — this formula gives the
   single middle for odd length and the SECOND middle for even length
   (len 5 -> position 3; len 6 -> position 4).
3. Restart temp at head and step forward (position - 1) times to land on that node.
4. Return temp. This walks the list twice (count, then re-traverse to the middle).
TC -> O(n) (O(n) + O(n/2)), SC -> O(1)

#Better Approach:
SKIPPED — no distinct intermediate tier: the problem goes straight from the
two-pass count-then-walk brute force to the one-pass tortoise-and-hare optimal.

#Optimal Approach:
1. Avoid the second pass with two pointers from head: slow advances 1 node per step,
   fast advances 2 nodes per step.
2. Loop while fast and fast.next both exist — that guarantee lets fast take a full
   two-step hop without dereferencing None.
3. By the 2:1 speed ratio, when fast reaches the end slow has travelled exactly half
   the list, so slow sits on the middle node — found in a single pass.
4. For even length the loop lets fast take one extra hop, so slow stops on the SECOND
   middle, matching the problem's requirement. Return slow.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Both approaches are O(n)/O(1), but the tortoise-and-hare finds the middle in ONE
  pass instead of two: moving fast at double speed means slow is exactly halfway when
  fast finishes. The `fast and fast.next` loop condition is also what makes even-length
  lists land on the second middle.
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    for value in values:
        node = ListNode(value)
        curr.next = node
        curr = node
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    values: List[int] = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def find_middle_of_linked_list_brute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = 0
        temp = head

        while temp is not None:
            temp = temp.next
            cnt += 1

        cnt = (cnt // 2) + 1

        temp = head
        cnt -= 1

        while cnt != 0:
            temp = temp.next  # type: ignore[union-attr]
            cnt -= 1

        return temp

    def find_middle_of_linked_list_better(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # SKIP: no distinct intermediate tier — the problem jumps from the two-pass
        # count-then-walk brute force straight to the one-pass tortoise-and-hare optimal.
        pass

    def find_middle_of_linked_list_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[union-attr]
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5])
    # head = build_linked_list([1, 2, 3, 4, 5, 6])
    mid = sol.find_middle_of_linked_list_brute(head)
    print(mid.val if mid else None)
    head = build_linked_list([1, 2, 3, 4, 5])
    # head = build_linked_list([1, 2, 3, 4, 5, 6])
    mid = sol.find_middle_of_linked_list_optimal(head)
    print(mid.val if mid else None)
