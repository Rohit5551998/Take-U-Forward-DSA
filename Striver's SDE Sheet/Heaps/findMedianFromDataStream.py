# mypy: disable-error-code="empty-body"
# QUESTION: Find Median from Data Stream
# Implement the MedianFinder class:
#   MedianFinder()         — Initializes the object.
#   void addNum(int num)   — Adds the integer num from the data stream.
#   double findMedian()    — Returns the median of all elements seen so
#                            far. If the size of the list is even, the
#                            median is the average of the two middle
#                            values (use float division).
#
# Follow up:
#   1. If all integer numbers from the stream are in the range [0, 100],
#      can you optimize your solution?
#   2. If 99% of all integer numbers from the stream are in the range
#      [0, 100], can you optimize your solution?
#
# Optimal approach: maintain two heaps — a max-heap for the lower half
# and a min-heap for the upper half — kept balanced (size difference ≤ 1).
# - addNum is O(log n)
# - findMedian is O(1)
#
# Examples:
# Input : [MedianFinder(), addNum(1), addNum(2), addNum(3), findMedian()]
# Output : [null, null, null, null, 2]
# Explanation: addNum(1) → [1]; addNum(2) → [1, 2]; addNum(3) → [1, 2, 3];
# findMedian() returns 2 as the median of [1, 2, 3].
#
# Input : [MedianFinder(), addNum(1), addNum(6), findMedian(), addNum(3), findMedian()]
# Output : [null, null, null, 3.5, null, 3]
# Explanation: addNum(1) → [1]; addNum(6) → [1, 6]; findMedian() returns (1+6)/2 = 3.5;
# addNum(3) → [1, 3, 6]; findMedian() returns 3 as the median.


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


class MedianFinder:
    def __init__(self) -> None:
        pass

    def add_num(self, num: int) -> None:
        pass

    def find_median(self) -> float:
        pass


if __name__ == "__main__":
    mf = MedianFinder()
    mf.add_num(1)
    mf.add_num(2)
    mf.add_num(3)
    print(mf.find_median())
