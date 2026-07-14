# mypy: disable-error-code="empty-body"
# QUESTION: Find Pairs with a Given Sum in a Sorted Doubly Linked List
# Given the head of a doubly linked list sorted in ascending order and a target sum,
# return all pairs of values (a, b) with a <= b whose sum equals the target.
# Example 1:
# Input: 1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9, target = 7
# Output: [(1, 6), (2, 5)]
# Constraints:
# 0 <= number of nodes <= 10^5
# list is sorted in non-decreasing order

"""
#Brute Force:
1. For each node temp1, scan forward with temp2 while temp1.data + temp2.data <= target.
2. Record the pair whenever the sum equals the target.
TC -> O(n^2) worst case, SC -> O(1) (excluding output).

#Better Approach:
SKIPPED — the two-pointer method below is the intended optimal; no distinct middle tier.

#Optimal Approach (two pointers from both ends):
1. Place `left` at head and `right` at the tail.
2. While right is beyond left (right.data > left.data): compute their sum. If it exceeds
   target move right back (right.prev); if it is below target move left forward; on a match
   record the pair and move both inward.
TC -> O(n), SC -> O(1) (excluding output).

#KEY INSIGHT:
- Sorted order plus prev/next links let two pointers converge from the ends: too-large
  sums shrink via right.prev, too-small sums grow via left.next, so each pair is found in
  a single linear sweep.
"""

from typing import List, Optional, Tuple


class Node:
    def __init__(
        self,
        data: int,
        next1: Optional["Node"] = None,
        prev1: Optional["Node"] = None,
    ) -> None:
        self.data = data
        self.next = next1
        self.prev = prev1


class Solution:
    def convertArr2DLL(self, arr: List[int]) -> Optional[Node]:
        head = Node(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = Node(arr[i], None, temp)
            temp = temp.next
        return head

    def printLinkedList(self, head: Optional[Node]) -> None:
        temp = head
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def findPairsWithSum_brute(self, head: Optional[Node], target: int) -> List[Tuple[int, int]]:
        ans: List[Tuple[int, int]] = []
        if head is None or head.next is None:
            return ans
        temp1: Optional[Node] = head
        while temp1 is not None and temp1.next is not None:
            temp2 = temp1.next
            while temp2 is not None and temp1.data + temp2.data <= target:
                if temp1.data + temp2.data == target:
                    ans.append((temp1.data, temp2.data))
                temp2 = temp2.next
            temp1 = temp1.next
        return ans

    def findPairsWithSum_better(self, head: Optional[Node], target: int) -> List[Tuple[int, int]]:
        # SKIP: two-pointer method is the intended optimal; no distinct middle tier
        pass

    def findPairsWithSum_optimal(self, head: Optional[Node], target: int) -> List[Tuple[int, int]]:
        ans: List[Tuple[int, int]] = []
        if head is None or head.next is None:
            return ans
        left: Optional[Node] = head
        right: Optional[Node] = head
        while right is not None and right.next is not None:
            right = right.next
        while right is not None and left is not None and right.data > left.data:
            total = left.data + right.data
            if total > target:
                right = right.prev
            elif total < target:
                left = left.next
            else:
                ans.append((left.data, right.data))
                left = left.next
                right = right.prev
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 4, 5, 6, 8, 9]
    head = sol.convertArr2DLL(arr)
    print(sol.findPairsWithSum_optimal(head, 7))
