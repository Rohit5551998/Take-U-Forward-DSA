# mypy: disable-error-code="empty-body"
# QUESTION: Implement Max Heap
# You need to implement the Max Heap with the following given methods.
# - insert(x)         -> insert value x to the max heap
# - getMax            -> output the maximum value from the max heap
# - extractMax        -> remove the maximum element from the heap
# - heapSize          -> return the current size of the heap
# - isEmpty           -> returns if heap is empty or not
# - changeKey(ind, val) -> update the value at given index to val (index is 0-based)
# - initializeHeap    -> initialize the heap
# Note: When extracting max, if both left and right children are equal, you must swap with the
# LEFT child.
#
# Examples:
# Example 1:
# Input: ["initializeHeap", "insert 4", "insert 9", "getMax", "extractMax", "getMax",
#         "heapSize", "isEmpty"]
# Output: [9, 4, 1, false]
# Explanation: After inserting 4 and 9, getMax returns 9. extractMax removes 9, so the next
# getMax returns 4. One element remains, so heapSize is 1 and isEmpty is false.
#
# Example 2:
# Input: ["initializeHeap", "insert 5", "insert 2", "insert 8", "changeKey 1 10", "getMax",
#         "extractMax", "getMax"]
# Output: [10, 8]
# Explanation: After the inserts, the heap array is [8, 2, 5]. changeKey(1, 10) sets index 1
# to 10, which sifts up to the root: [10, 8, 5]. getMax returns 10; extractMax removes 10,
# so the next getMax returns 8.
#
# Constraints:
# 1 <= n <= 10^5
# -10^5 <= nums[i] <= 10^5


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


class MaxHeap:
    def __init__(self) -> None:
        pass

    def insert(self, val: int) -> None:
        pass

    def get_max(self) -> int:
        pass

    def extract_max(self) -> int:
        pass


if __name__ == "__main__":
    heap = MaxHeap()
    heap.insert(4)
    heap.insert(9)
    print(heap.get_max())
    print(heap.extract_max())
    print(heap.get_max())
