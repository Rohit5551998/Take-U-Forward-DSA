# mypy: disable-error-code="empty-body"
# QUESTION: Intersection of Two Linked Lists
# Given the heads of two singly linked lists that may merge and share a common tail,
# return the node at which they intersect (by identity, not value), or None if they
# never intersect.
# Example 1:
# Input: listA = 1 -> 2 -> 3 and listB = 4 -> 5, where listB's 5 links into listA's 2
# Output: node with value 2
# Example 2:
# Input: two disjoint lists
# Output: None
# Constraints:
# 0 <= nodes in each list <= 10^5

"""
#Brute Force:
1. Store every node of list1 (by identity) in a hash set.
2. Walk list2; the first node already present in the set is the intersection -> return it.
3. No match -> None.
TC -> O(n + m), SC -> O(n).

#Better Approach:
1. Measure both lengths and compute their difference d.
2. Advance the longer list's pointer by d so both have equal remaining length.
3. Walk both in lockstep; the first node where the pointers are identical is the answer.
TC -> O(2*max(n,m)) + O(|n-m|) + O(min(n,m)), SC -> O(1).

#Optimal Approach (two-pointer swap):
1. Start t1 at head1 and t2 at head2.
2. Step both forward; when a pointer hits None, redirect it to the *other* list's head.
3. After at most n+m steps they either meet at the intersection node or both reach None.
TC -> O(2*max(n,m)), SC -> O(1).

#KEY INSIGHT:
- Redirecting each pointer to the opposite head equalizes the total distance travelled
  (n + m for both), so they align at the intersection without measuring lengths.
"""

from typing import List, Optional, Set


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

    def findIntersection_brute(
        self, head1: Optional[Node], head2: Optional[Node]
    ) -> Optional[Node]:
        seen: Set[Node] = set()
        temp = head1
        while temp is not None:
            seen.add(temp)
            temp = temp.next
        temp = head2
        while temp is not None:
            if temp in seen:
                return temp
            temp = temp.next
        return None

    def getDifference(self, head1: Optional[Node], head2: Optional[Node]) -> int:
        len1, len2 = 0, 0
        temp1, temp2 = head1, head2
        while temp1 is not None or temp2 is not None:
            if temp1 is not None:
                len1 += 1
                temp1 = temp1.next
            if temp2 is not None:
                len2 += 1
                temp2 = temp2.next
        return len1 - len2

    def findIntersection_better(
        self, head1: Optional[Node], head2: Optional[Node]
    ) -> Optional[Node]:
        diff = self.getDifference(head1, head2)
        if diff < 0:
            while diff != 0 and head2 is not None:
                head2 = head2.next
                diff += 1
        else:
            while diff != 0 and head1 is not None:
                head1 = head1.next
                diff -= 1
        while head1 is not None and head2 is not None:
            if head1 == head2:
                return head1
            head1 = head1.next
            head2 = head2.next
        return None

    def findIntersection_optimal(
        self, head1: Optional[Node], head2: Optional[Node]
    ) -> Optional[Node]:
        if head1 is None or head2 is None:
            return None
        temp1: Optional[Node] = head1
        temp2: Optional[Node] = head2
        while temp1 != temp2:
            temp1 = head2 if temp1 is None else temp1.next
            temp2 = head1 if temp2 is None else temp2.next
        return temp1


if __name__ == "__main__":
    sol = Solution()
    head = sol.convertArr2LL([1, 2, 3])
    head1 = sol.convertArr2LL([4, 5])
    # Make list2 intersect list1 at the node holding value 2.
    if head1 is not None and head is not None:
        head1.next.next = head.next  # type: ignore[union-attr]
    res = sol.findIntersection_optimal(head, head1)
    print(res.data if res is not None else None)
