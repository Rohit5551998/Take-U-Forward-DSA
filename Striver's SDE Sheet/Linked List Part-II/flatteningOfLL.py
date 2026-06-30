# QUESTION: Flattening of LL
# Given a linked list containing ‘N’ head nodes where every node in the linked list contains two pointers: ‘Next’ points to the next node in the list ‘Child’ pointer to.


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


class ListNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional["ListNode"] = None,
        child: Optional["ListNode"] = None,
    ) -> None:
        self.val = val
        self.next = next
        self.child = child


def build_flattened(rows: List[List[int]]) -> Optional[ListNode]:
    # Each inner list becomes a vertical chain linked through `child`;
    # the row heads are linked left-to-right through `next`.
    top_dummy = ListNode()
    top_tail = top_dummy
    for row in rows:
        if not row:
            continue
        row_head = ListNode(row[0])
        col_tail = row_head
        for value in row[1:]:
            node = ListNode(value)
            col_tail.child = node
            col_tail = node
        top_tail.next = row_head
        top_tail = row_head
    return top_dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    # The fully flattened list is threaded through `child` pointers.
    values: List[int] = []
    while head is not None:
        values.append(head.val)
        head = head.child
    return values


class Solution:
    def flattening_of_ll_brute(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

    def flattening_of_ll_better(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

    def flattening_of_ll_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


if __name__ == "__main__":
    sol = Solution()
    head = build_flattened([[3, 7, 8, 30], [8, 10, 20], [10, 20], [2, 22, 50]])
    # print(to_list(sol.flattening_of_ll_optimal(head)))
