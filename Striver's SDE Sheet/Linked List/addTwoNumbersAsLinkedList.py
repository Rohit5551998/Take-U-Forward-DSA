# QUESTION: Add two numbers as LinkedList
# Add two numbers represented as Linked Lists.
#
# Examples:
# Example 1:
# Input: num1 = 243, num2 = 564
# Output:sum = 807; L = [7,0,8]
#
# Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the or original number and then add them as → 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: Result: [8,9,9,9,0,0,0,1]
#
# Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the original number and then add them as → 9999999 + 9999 = 8999001. Refer to the image below.


"""
#Brute Force:
SKIPPED — no sensible lower tier: converting each list to an integer, adding, and
rebuilding a list is fragile (overflows in fixed-width-int languages for long lists)
and gives no algorithmic gain. The dummy-node + carry pass below is the natural method.

#Better Approach:
SKIPPED — same reason; there is no distinct intermediate between the (impractical)
integer-conversion idea and the optimal single-pass carry addition.

#Optimal Approach:
1. Add digit-by-digit like grade-school addition. Both lists store digits in REVERSE
   (least-significant first), so the heads already line up — we add left-to-right and
   let carries flow forward, no reversing needed.
2. Use a dummy head + `temp` tail so the first result node is appended exactly like
   every other node (no special-casing the head).
3. Loop while EITHER list still has nodes OR a carry remains. Begin each step's `total`
   at the incoming carry.
4. Add the current digit of each list when its node exists, advancing that pointer;
   a missing node contributes 0 (this zero-pads the shorter number).
5. Split the total: carry = total // 10 (the tens place to push forward), digit = total % 10
   (the ones place to store). Append a new node holding `digit`.
6. The `carry != 0` clause in the loop guard is what emits the extra leading node when
   the final addition overflows (e.g. 999 + 1 -> 1000) after both lists are exhausted.
7. Return dummyHead.next.
TC -> O(max(m, n)), SC -> O(max(m, n)) for the result (O(1) extra, ignoring output)

#KEY INSIGHT:
- Reverse-order storage makes the least-significant digits align at the heads, so a
  single left-to-right pass with a running carry adds the numbers. The dummy node kills
  the head special-case, and keeping `carry != 0` in the loop condition handles the
  final overflow digit with no extra code.
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
    def add_two_numbers_as_linkedlist_brute(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # SKIP: no sensible lower tier — converting lists to integers, adding, and
        # rebuilding is fragile (fixed-int overflow) and offers no algorithmic gain.
        pass

    def add_two_numbers_as_linkedlist_better(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # SKIP: no distinct intermediate between the integer-conversion idea and the
        # optimal single-pass carry addition.
        pass

    def add_two_numbers_as_linkedlist_optimal(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummyHead = ListNode()
        temp = dummyHead
        total = 0
        carry = 0
        node1, node2 = l1, l2

        while node1 is not None or node2 is not None or carry != 0:
            total = carry

            if node1 is not None:
                total += node1.val
                node1 = node1.next

            if node2 is not None:
                total += node2.val
                node2 = node2.next

            carry = total // 10
            total = total % 10

            temp.next = ListNode(total)

            temp = temp.next

        return dummyHead.next


if __name__ == "__main__":
    sol = Solution()
    l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_linked_list([9, 9, 9, 9])
    print(to_list(sol.add_two_numbers_as_linkedlist_optimal(l1, l2)))
