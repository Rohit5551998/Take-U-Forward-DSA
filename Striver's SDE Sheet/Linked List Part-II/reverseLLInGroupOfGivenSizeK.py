# QUESTION: Reverse LL in group of given size K
# Given the head of a singly linked list containing integers, reverse the nodes of the list in
# groups of k and return the head of the modified list. If the number of nodes is not a
# multiple of k, then the remaining nodes at the end should be kept as is and not reversed.
# Do not change the values of the nodes, only change the links between nodes.
#
# Examples:
# Example 1:
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: head -> 2 -> 1 -> 4 -> 3 -> 5
# Explanation: The groups 1 -> 2 and 3 -> 4 were reversed as 2 -> 1 and 4 -> 3.
#
# Example 2:
# Input: head -> 1 -> 2 -> 3 -> 4 -> 5, k = 3
# Output: head -> 3 -> 2 -> 1 -> 4 -> 5
# Explanation: The groups 1 -> 2 -> 3 were reversed as 3 -> 2 -> 1.
# Note that 4 -> 5 was not reversed.
#
# Constraints:
# 1 <= k <= number of nodes in the linked list <= 10^5
# -10^4 <= ListNode.val <= 10^4


"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
SKIPPED — no distinct middle tier exists. The problem goes straight from an
extra-space brute force to the in-place pointer-relinking optimal; nothing
sensible sits in between.

#Optimal Approach:
1. Reverse each k-sized block in place and stitch the blocks together. No extra
   list is needed because reversing only rewires next pointers — the only real
   bookkeeping is remembering where the previous block ended so it can be
   connected to the current block's new head.
2. Keep temp at the start of the current block. find_kth_node walks k-1 steps
   ahead to locate the block's last node (kthNode).
3. If kthNode is None, fewer than k nodes remain — the leftover tail must stay
   in original order, so just attach it to the previous block's tail
   (back.next = temp) and stop. back starts as None, which doubles as the
   "no block reversed yet" signal: if the whole list is shorter than k, there
   is nothing to reconnect and head is returned untouched.
4. Otherwise detach the block before reversing: save front = kthNode.next, then
   cut with kthNode.next = None so reverse_ll only reverses this k-node slice
   and cannot run past the block boundary.
5. Reverse the slice with the standard recursive reverse_ll. Afterwards kthNode
   is the block's new head and temp (the old first node) is its new tail.
6. Reconnect the block: for the very first block the overall head itself moves
   (head = newHead); for every later block the previous block's tail back is
   pointed at kthNode.
7. Slide forward: the just-reversed block's tail (temp) becomes the new back,
   and temp = front jumps to the next block's start. Every node is visited
   twice — once by the k-th-node scan, once by the reversal.
TC -> O(2n) ~ O(n), SC -> O(k) (recursion stack of reverse_ll, one block deep at a time)

#KEY INSIGHT:
- Reversing in k-groups is just "reverse a whole linked list" applied to a
  detached slice: cut the block out (kthNode.next = None), reverse it, then
  re-stitch using two anchors — the previous block's tail (back) and the next
  block's head (front). The head pointer changes exactly once, at the first block.
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
    def reverse_ll_in_group_of_given_size_k_brute(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        pass

    def reverse_ll_in_group_of_given_size_k_better(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        pass

    def reverse_ll(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        if head is None or head.next is None:
            ans = head
        else:
            newHead = self.reverse_ll(head.next)
            front = head.next
            head.next = None
            front.next = head
            ans = newHead
        return ans

    def find_kth_node(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = curr
        k -= 1
        while k > 0 and temp is not None:
            temp = temp.next
            k -= 1
        return temp

    def reverse_ll_in_group_of_given_size_k_optimal(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        temp = head
        back: Optional[ListNode] = None

        while temp is not None:
            kthNode = self.find_kth_node(temp, k)
            if kthNode is None:
                if back is not None:
                    back.next = temp
                break
            front = kthNode.next
            kthNode.next = None
            newHead = self.reverse_ll(temp)

            if temp == head:
                head = newHead
            else:
                back.next = kthNode  # type: ignore[union-attr]

            back = temp
            temp = front
        return head


if __name__ == "__main__":
    sol = Solution()
    head = build_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 2
    # print(to_list(sol.reverse_ll(head)))
    print(to_list(sol.reverse_ll_in_group_of_given_size_k_optimal(head, k)))
