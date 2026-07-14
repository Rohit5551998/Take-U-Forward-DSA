# mypy: disable-error-code="empty-body"
# QUESTION: Min Heap and Max Heap Implementation
# Implement a binary Min Heap and a binary Max Heap from scratch using an array.
# Support the core operations:
#   - insert(val): add a value while maintaining the heap property (heapify-up)
#   - extractTop(): remove and return the root (min for min-heap, max for max-heap)
#     while maintaining the heap property (heapify-down)
#   - peek(): return the root without removing it
# For a node at index i (0-based): parent = (i-1)//2, left = 2*i+1, right = 2*i+2.
#
# Example 1:
# Input: MinHeap; insert 3, insert 1, insert 2; extractTop(); extractTop()
# Output: 1, then 2
# Explanation: The min-heap keeps the smallest element at the root.
#
# Constraints:
# 1 <= number of operations <= 10^5
# -10^9 <= value <= 10^9


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


class MinHeap:
    def __init__(self) -> None:
        pass

    def insert(self, val: int) -> None:
        pass

    def peek(self) -> int:
        pass

    def extractTop(self) -> int:
        pass


class MaxHeap:
    def __init__(self) -> None:
        pass

    def insert(self, val: int) -> None:
        pass

    def peek(self) -> int:
        pass

    def extractTop(self) -> int:
        pass


# if __name__ == "__main__":
#     h = MinHeap()
#     for x in (3, 1, 2):
#         h.insert(x)
#     print(h.extractTop(), h.extractTop())
