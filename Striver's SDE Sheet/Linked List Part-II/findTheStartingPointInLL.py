# QUESTION: Find the starting point in LL
# Given the head of a singly linked list, the task is to find the starting point of a loop in the
# linked list if it exists. Return the starting node if a loop exists; otherwise, return null.
#
# A loop exists in a linked list if some node in the list can be reached again by continuously
# following the next pointer. Internally, pos denotes the index (0-based) of the node from where
# the loop starts. Note that pos is not passed as a parameter.
#
# Examples:
# Example 1:
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1
# Output (value of the returned node is displayed): 2
# Explanation: The tail of the linked list connects to the node at 1st index.
#
# Example 2:
# Input: head -> 1 -> 3 -> 7 -> 4, pos = -1
# Output (value of the returned node is displayed): null
# Explanation: No loop is present in the linked list.
#
# Constraints:
# 0 <= number of nodes in the cycle <= 10^5
# 0 <= ListNode.val <= 10^4
# pos is -1 or a valid index in the linked list


"""
#Brute Force:
1. The first node ever REVISITED while walking the list is exactly the cycle
   start: every node before the loop is passed once, and the walk re-enters
   the loop precisely at its entry point.
2. Walk with temp, storing each visited node OBJECT in a hash set — objects,
   not values, because values can repeat across different nodes.
3. Before adding, check membership: if temp is already in the set, this is the
   revisited node → return it as the cycle start.
4. If temp falls off the end (None), the list has no cycle → return None.
TC -> O(n) (one walk, O(1) average set ops), SC -> O(n) (set can hold all nodes)

#Better Approach:
SKIPPED — no distinct middle tier exists. The problem goes straight from the
O(n)-space hash-set walk to Floyd's O(1)-space two-pointer algorithm; nothing
sensible sits in between.

#Optimal Approach:
1. Floyd's cycle detection, phase 1: slow steps one node, fast steps two. If a
   cycle exists fast can never escape it, and inside the loop fast gains on
   slow by exactly one node per step — so they MUST meet; with no cycle fast
   just runs off the end (None).
2. Both pointers start from a dummy node placed before head. That is the same
   as running Floyd on a list one node longer, which stays consistent because
   phase 2 resets to the dummy as well.
3. Guard first: a None head or single non-looping node can't hold a cycle →
   return None immediately.
4. If the loop exited because fast hit the end (slow != fast), no cycle →
   return None.
5. Phase 2: reset fast to the dummy start and advance BOTH pointers one step
   at a time. Why they collide at the loop entry: the distance from the start
   to the cycle entry equals the distance from the meeting point forward to
   that same entry (modulo the loop length) — a consequence of fast having
   walked exactly twice slow's distance when they met.
6. The node where they meet now is the starting point of the loop → return it.
TC -> O(n) + O(n) ~ O(n), SC -> O(1) (two pointers, nothing else)

#KEY INSIGHT:
- Inside the loop the gap between fast and slow shrinks by one each step, so a
  meeting is guaranteed. And because fast walked exactly 2x slow's distance,
  head-to-entry distance ≡ meetingPoint-to-entry distance (mod loop length) —
  so two one-step walkers from (head, meeting point) land together exactly at
  the cycle entry, with zero extra memory.
"""

from typing import List, Optional, Tuple


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


def build_linked_list_with_cycle(
    values: List[int], pos: int
) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    # pos is the 0-based index the tail links back to; pos = -1 means no cycle.
    # Returns (head, cycle_start) so tests can assert node identity, not just value.
    dummy = ListNode()
    curr = dummy
    nodes: List[ListNode] = []
    for value in values:
        node = ListNode(value)
        nodes.append(node)
        curr.next = node
        curr = node
    cycle_start = nodes[pos] if 0 <= pos < len(nodes) else None
    if nodes and cycle_start is not None:
        nodes[-1].next = cycle_start
    return dummy.next, cycle_start


def to_list(head: Optional[ListNode]) -> List[int]:
    # Only safe on acyclic lists — loops forever on a cycle.
    values: List[int] = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


class Solution:
    def find_the_starting_point_in_ll_brute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashSet = set()
        temp = head
        ans = None
        while temp is not None:
            if temp in hashSet:
                ans = temp
                break
            hashSet.add(temp)
            temp = temp.next
        return ans

    def find_the_starting_point_in_ll_better(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # SKIP: no tier between the O(n)-space hash-set walk and Floyd's O(1)-space two-pointer
        pass

    def find_the_starting_point_in_ll_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        ans = None

        if head is None or head.next is None:
            return ans

        slow = fast = dummyHead
        while fast is not None and fast.next is not None:
            slow = slow.next  # type: ignore[assignment]
            fast = fast.next.next  # type: ignore[assignment]
            if slow == fast:
                break

        if slow == fast:
            fast = dummyHead

            while slow != fast:
                slow = slow.next  # type: ignore[assignment]
                fast = fast.next  # type: ignore[assignment]

            ans = slow

        return ans


if __name__ == "__main__":
    sol = Solution()
    head, expected = build_linked_list_with_cycle([1, 2, 3, 4, 5], 2)  # cycle starts at value 3
    start = sol.find_the_starting_point_in_ll_brute(head)
    print(start.val if start else None, start is expected)  # expect: 3 True
    head, expected = build_linked_list_with_cycle([1, 2, 3, 4, 5], 2)  # cycle starts at value 3
    start = sol.find_the_starting_point_in_ll_optimal(head)
    print(start.val if start else None, start is expected)  # expect: 3 True
    head2, _ = build_linked_list_with_cycle([1, 2, 3, 4, 5], -1)  # no cycle
    print(sol.find_the_starting_point_in_ll_brute(head2))  # expect: None
    head2, _ = build_linked_list_with_cycle([1, 2, 3, 4, 5], -1)  # no cycle
    print(sol.find_the_starting_point_in_ll_optimal(head2))  # expect: None
