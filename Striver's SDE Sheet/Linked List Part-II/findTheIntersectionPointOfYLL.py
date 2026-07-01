# QUESTION: Find the intersection point of Y LL
# Given the heads of two singly linked-lists headA and headB , return the node at which the two lists intersect . If the two linked lists have no intersection at all, return null.
#
# Examples:
# Example 1:
# Input:
# List 1 = [1,3,1,2,4], List 2 = [3,2,4]
# Output:
# 2
# Explanation: Here, both lists intersecting nodes start from node 2.
#
#  Example 2:
# Input:
#  List1 = [1,2,7], List 2 = [2,8,1]
# Output:
#  Null
# Explanation: Here, both lists do not intersect and thus no intersection node is present.


"""
#Brute Force:
1. Two lists intersect at a node they physically SHARE (same object, not same value),
   so after the intersection every node is common. Find the first shared node.
2. For each node of list A (outer loop), walk the whole of list B (inner loop) and
   compare by identity (temp1 == temp2 is object identity here). The first A-node that
   is found somewhere in B is the intersection; break out of both loops.
3. Every A-node triggers a full B-scan, giving n*m work.
TC -> O(n*m), SC -> O(1)

#Better Approach:
1. Avoid rescanning B for every A-node by remembering all of A first.
2. Put every node of A into a hash set (by identity). Then walk B once; the first B-node
   already present in the set is the shared node, because from the intersection onward the
   nodes are the exact same objects.
3. One pass to fill the set, one pass to probe it -> linear time, at the cost of storing A.
TC -> O(n + m), SC -> O(n)

#Optimal Variant I — length difference (find_..._optimal_variant_i):
1. The two lists share a common tail, so their ends align. If one list is longer, its extra
   front nodes can never be the intersection. Cancel that head start, then walk both together.
2. Measure both lengths l1, l2 in one pass each.
3. Advance the pointer on the longer list by |l1 - l2| so both pointers now have the same
   number of nodes remaining until the (shared) end.
4. Move both pointers one step at a time; the first position where they are the same object
   is the intersection. If they both fall off the end (None), there is no intersection.
TC -> O(n + m), SC -> O(1)

#Optimal Variant II — two-pointer head switch (find_..._optimal_variant_ii):
1. Same goal without measuring lengths: make both pointers travel the exact same total
   distance so they line up at the intersection.
2. Start temp1 at headA, temp2 at headB. Each step advance both; when a pointer hits the end,
   redirect it to the OTHER list's head instead of None.
3. After the switch, temp1 covers lenA + lenB and temp2 covers lenB + lenA — equal totals —
   so they arrive at the first shared node together. If there is no intersection, both become
   None at the same step and the loop stops, returning None.
TC -> O(n + m), SC -> O(1)

#KEY INSIGHT:
- Intersection is about shared NODES (identity), not equal values, and past the meeting point
  the two lists are literally the same nodes. Every improvement is about erasing the length
  gap between the lists so two pointers reach that shared tail in lockstep — either by
  measuring and skipping the difference (Variant I) or by swapping heads so both walk
  lenA + lenB total (Variant II).
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


def build_y_linked_lists(
    a_only: List[int], b_only: List[int], common: List[int]
) -> tuple[Optional[ListNode], Optional[ListNode]]:
    # Builds a Y shape: list A = a_only + common, list B = b_only + common,
    # where the `common` suffix is the SAME set of physical nodes shared by both
    # lists (that shared node is the intersection point).
    common_head = build_linked_list(common)

    def attach(prefix: List[int]) -> Optional[ListNode]:
        head = build_linked_list(prefix)
        if head is None:
            return common_head
        tail = head
        while tail.next is not None:
            tail = tail.next
        tail.next = common_head
        return head

    return attach(a_only), attach(b_only)


class Solution:
    def find_the_intersection_point_of_y_ll_brute(
        self, head_a: Optional[ListNode], head_b: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp1 = head_a
        temp2 = head_b
        ans = None

        while temp1 is not None:
            while temp2 is not None:
                if temp1 == temp2:
                    ans = temp1
                    break
                temp2 = temp2.next

            if ans is not None:
                break

            temp1 = temp1.next
            temp2 = head_b
        return ans

    def find_the_intersection_point_of_y_ll_better(
        self, head_a: Optional[ListNode], head_b: Optional[ListNode]
    ) -> Optional[ListNode]:
        hashSet = set()
        temp1 = head_a
        temp2 = head_b
        ans = None

        while temp1 is not None:
            hashSet.add(temp1)
            temp1 = temp1.next

        while temp2 is not None:
            if temp2 in hashSet:
                ans = temp2
                break
            temp2 = temp2.next

        return ans

    def find_the_intersection_point_of_y_ll_optimal_variant_i(
        self, head_a: Optional[ListNode], head_b: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp1 = head_a
        temp2 = head_b
        ans = None

        l1, l2 = 0, 0
        while temp1 is not None:
            l1 += 1
            temp1 = temp1.next

        while temp2 is not None:
            l2 += 1
            temp2 = temp2.next

        if l1 > l2:
            temp1 = head_a
            l1 = l1 - l2
            while l1 > 0:
                temp1 = temp1.next
                l1 -= 1
            temp2 = head_b
        else:
            temp2 = head_b
            l2 = l2 - l1
            while l2 > 0:
                temp2 = temp2.next
                l2 -= 1
            temp1 = head_a

        while temp1 is not None and temp2 is not None:
            if temp1 == temp2:
                ans = temp1
                break

            temp1 = temp1.next
            temp2 = temp2.next

        return ans

    def find_the_intersection_point_of_y_ll_optimal_variant_ii(
        self, head_a: Optional[ListNode], head_b: Optional[ListNode]
    ) -> Optional[ListNode]:
        temp1 = head_a
        temp2 = head_b

        while temp1 != temp2:
            temp1 = head_b if temp1 is None else temp1.next
            temp2 = head_a if temp2 is None else temp2.next

        return temp1


if __name__ == "__main__":
    sol = Solution()
    # List A = [1, 3, 1] + [2, 4], List B = [3] + [2, 4]; shared tail starts at node 2.
    # Expected intersection value: 2
    head_a, head_b = build_y_linked_lists([1, 3, 1], [3], [2, 4])
    node = sol.find_the_intersection_point_of_y_ll_brute(head_a, head_b)
    print(node.val if node else None)

    head_a, head_b = build_y_linked_lists([1, 3, 1], [3], [2, 4])
    node = sol.find_the_intersection_point_of_y_ll_better(head_a, head_b)
    print(node.val if node else None)

    head_a, head_b = build_y_linked_lists([1, 3, 1], [3], [2, 4])
    node = sol.find_the_intersection_point_of_y_ll_optimal_variant_i(head_a, head_b)
    print(node.val if node else None)

    head_a, head_b = build_y_linked_lists([1, 3, 1], [3], [2, 4])
    node = sol.find_the_intersection_point_of_y_ll_optimal_variant_ii(head_a, head_b)
    print(node.val if node else None)
