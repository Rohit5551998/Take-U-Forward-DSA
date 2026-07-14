# mypy: disable-error-code="empty-body"
# QUESTION: Merge M Sorted Lists (Merge K Sorted Lists)
# You are given an array of k linked-lists, each linked-list sorted in ascending
# order. Merge all the linked-lists into one sorted linked-list and return its
# head.
#
# Example 1:
# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Explanation: Merging the three sorted lists yields one sorted list.
#
# Example 2:
# Input: lists = []
# Output: []
#
# Constraints:
# 0 <= k <= 10^4
# 0 <= list length <= 500
# -10^4 <= Node.val <= 10^4


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
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeKLists_brute(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass

    def mergeKLists_better(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass

    def mergeKLists_optimal(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     a = ListNode(1, ListNode(4, ListNode(5)))
#     b = ListNode(1, ListNode(3, ListNode(4)))
#     c = ListNode(2, ListNode(6))
#     print(sol.mergeKLists_optimal([a, b, c]))
