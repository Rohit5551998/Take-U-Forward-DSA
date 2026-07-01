# mypy: disable-error-code="empty-body"
# QUESTION: Detect a loop in LL
# Given a Linked List, determine whether the linked list contains a cycle or not.
#
# Examples:
# Input: LL: 1 2 3 4 5
#
# Output: True
# Explanation: The last node with the value of 5 has its 'next' pointer pointing back to a previous node with the value of 3. This has resulted in a loop, hence we return true.
#
# Input: LL: 1 2 3 4 9 9
#
# Output: False
# Explanation: In this example, the linked list does not have a loop hence returns false.


"""
#Brute Force:
1. If the list has a cycle, walking forward will eventually revisit a node it has already
   seen; if it is acyclic, it just runs off the end into None. So track what we've visited.
2. Walk from head keeping a hash set of visited nodes (by identity). Before moving on, check
   if the current node is already in the set — if yes, that revisit proves a loop; break.
3. Otherwise add it and advance. If we exit because temp became None, we reached the end
   with no repeat, so there is no loop. (temp != None distinguishes the two exit reasons.)
TC -> O(n), SC -> O(n)

#Better Approach:
SKIPPED — no meaningful tier between O(n)-space hashing and the O(1)-space Floyd's cycle
detection; the problem goes straight from brute (hashing) to optimal (slow/fast pointers).

#Optimal Approach:
1. Detect the cycle without extra memory using Floyd's tortoise-and-hare: two pointers moving
   at different speeds must collide inside a loop but never meet in a straight list.
2. Start slow and fast at head. Each step move slow by 1 and fast by 2.
3. If there is a loop, fast keeps lapping the track and the gap to slow shrinks by 1 each
   step until they land on the SAME node -> return True.
4. If there is no loop, fast (or fast.next) reaches None and the walk ends -> return False.
   Fast is what hits the end first, so the loop condition guards fast and fast.next.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- A cycle is detectable purely from movement: two pointers at speeds 1 and 2 must eventually
  coincide inside a loop (the faster closes the 1-step gap every tick) but can never meet if
  the list terminates — trading the hash set's O(n) space for O(1).
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


def build_linked_list_with_loop(values: List[int], pos: int) -> Optional[ListNode]:
    # Builds a list and, if pos >= 0, wires the tail's next back to the node at
    # index `pos` (0-based) to create a cycle. pos = -1 leaves it acyclic.
    head = build_linked_list(values)
    if head is None or pos < 0:
        return head

    loop_target = head
    for _ in range(pos):
        assert loop_target is not None
        loop_target = loop_target.next

    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = loop_target
    return head


class Solution:
    def detect_a_loop_in_ll_brute(self, head: Optional[ListNode]) -> bool:
        hashSet = set()
        temp = head

        while temp is not None:
            if temp in hashSet:
                break
            hashSet.add(temp)
            temp = temp.next

        return temp != None

    def detect_a_loop_in_ll_better(self, head: Optional[ListNode]) -> bool:
        # SKIP: no meaningful tier between O(n)-space hashing (brute) and O(1)-space
        # Floyd's cycle detection (optimal).
        pass

    def detect_a_loop_in_ll_optimal(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        ans = False

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                ans = True
                break

        return ans


if __name__ == "__main__":
    sol = Solution()
    # Cyclic: tail (5) points back to node at index 2 (value 3) -> expected True
    looped = build_linked_list_with_loop([1, 2, 3, 4, 5], 2)
    print(sol.detect_a_loop_in_ll_brute(looped))
    # Acyclic: no loop -> expected False
    straight = build_linked_list_with_loop([1, 2, 3, 4, 5], -1)
    print(sol.detect_a_loop_in_ll_brute(straight))
    # Cyclic: tail (5) points back to node at index 2 (value 3) -> expected True
    looped = build_linked_list_with_loop([1, 2, 3, 4, 5], 2)
    print(sol.detect_a_loop_in_ll_optimal(looped))
    # Acyclic: no loop -> expected False
    straight = build_linked_list_with_loop([1, 2, 3, 4, 5], -1)
    print(sol.detect_a_loop_in_ll_optimal(straight))
