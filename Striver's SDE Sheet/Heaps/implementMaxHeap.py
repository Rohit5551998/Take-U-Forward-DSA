# QUESTION: Implement Max Heap
# Implement a Max Heap from scratch with the following methods:
#   - insert(x)    — Insert value x into the max heap.
#   - getMax()     — Return the maximum value currently in the heap
#                    (without removing it).
#   - extractMax() — Remove and return the maximum value from the heap.
#   - heapSize()   — Return the current size of the heap.
#   - isEmpty()    — Return true if the heap is empty, false otherwise.
#
# Implementation hints:
#   - Use a 1-indexed array (or 0-indexed; just stay consistent).
#   - For node at index i: parent at i/2, left child at 2i, right child at 2i+1.
#   - insert: append at the end, then "sift-up" (swap with parent while
#     parent value < own value).
#   - extractMax: swap top with last, pop the last, then "sift-down"
#     (swap with larger child while a child > self).
#   - All operations are O(log n) except getMax/heapSize/isEmpty (O(1)).


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


def implement_max_heap_brute() -> None:
    pass


def implement_max_heap_better() -> None:
    pass


def implement_max_heap_optimal() -> None:
    pass
