# mypy: disable-error-code="empty-body"
# QUESTION: Merge k Sorted Lists
# You are given an array of k linked lists, each sorted in non-decreasing order.
# Merge all the lists into one sorted linked list and return its head.
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Constraints:
# - 0 <= k <= 10^4
# - 0 <= length of each list <= 500
# - -10^4 <= Node.val <= 10^4
# - each list is sorted in non-decreasing order

"""
#Brute Force:
1. Traverse all k lists and dump every value into one array.
2. Sort the array.
3. Build a fresh linked list from the sorted array.
TC -> O(K*N) + O((N*K) log(N*K)) + O(N*K), SC -> O(N*K) + O(N*K).

#Better Approach:
1. Merge the lists two at a time: start with lists[0], then repeatedly merge the
   running result with lists[i] using a standard two-sorted-list merge.
2. Return the final accumulated head.
   Downside: the growing accumulator is re-traversed each merge, so the earlier
   lists' nodes are visited many times.
TC -> O(N * k^2)  (sum of merge costs N*1 + N*2 + ... ~ N*k(k+1)/2), SC -> O(1).

#Optimal Approach:
1. Push the head of each non-empty list into a min-heap keyed by (data, list
   index) so the smallest current front is always on top. The index breaks ties
   so heterogeneous Node objects are never compared directly.
2. Pop the smallest node, append it to the result via a dummy tail, and if that
   node has a `next`, push the next into the heap.
3. Repeat until the heap is empty; return dummy.next.
TC -> O(K log K) build + O(N*K log K) processing, SC -> O(K) heap.

#KEY INSIGHT:
- A min-heap of size k always exposes the global minimum among the k list fronts
  in O(log k), so each of the N*K nodes is emitted in sorted order without ever
  re-scanning already-merged nodes — turning the better approach's O(N*k^2) into
  O(N*K log K).
"""

import heapq
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

    def mergeTwoSorted(self, head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
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

    def mergeKSortedLL_brute(self, lists: list[Optional[Node]]) -> Optional[Node]:
        vals: list[int] = []
        for node in lists:
            temp = node
            while temp is not None:
                vals.append(temp.data)
                temp = temp.next
        if not vals:
            return None
        vals.sort()
        return self.convertArr2LL(vals)

    def mergeKSortedLL_better(self, lists: list[Optional[Node]]) -> Optional[Node]:
        if not lists:
            return None
        head = lists[0]
        for i in range(1, len(lists)):
            head = self.mergeTwoSorted(head, lists[i])
        return head

    def mergeKSortedLL_optimal(self, lists: list[Optional[Node]]) -> Optional[Node]:
        if not lists:
            return None

        heap: list[tuple[int, int, Node]] = []
        for i in range(len(lists)):
            node = lists[i]
            if node is not None:
                heapq.heappush(heap, (node.data, i, node))

        newHead = Node(-1)
        temp = newHead
        while heap:
            _, index, curr = heapq.heappop(heap)
            if curr.next is not None:
                heapq.heappush(heap, (curr.next.data, index, curr.next))
            temp.next = curr
            temp = temp.next
        temp.next = None
        return newHead.next


if __name__ == "__main__":
    sol = Solution()
    lists = [
        sol.convertArr2LL([1, 4, 5]),
        sol.convertArr2LL([1, 3, 4]),
        sol.convertArr2LL([2, 6]),
    ]
    merged = sol.mergeKSortedLL_optimal(lists)
    sol.printLinkedList(merged)
