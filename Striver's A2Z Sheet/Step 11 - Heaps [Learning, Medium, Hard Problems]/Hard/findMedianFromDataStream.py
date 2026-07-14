# mypy: disable-error-code="empty-body"
# QUESTION: Find Median from Data Stream
# The median is the middle value in an ordered integer list. If the list size is
# even, the median is the average of the two middle values. Design a data
# structure that supports adding integers from a data stream and finding the
# running median. Implement MedianFinder:
#   - addNum(num): add the integer num to the data structure
#   - findMedian(): return the median of all elements so far
#
# Example 1:
# Input: addNum(1); addNum(2); findMedian(); addNum(3); findMedian()
# Output: 1.5, then 2.0
# Explanation: [1, 2] -> median 1.5; [1, 2, 3] -> median 2.0.
#
# Constraints:
# -10^5 <= num <= 10^5
# At least one element exists before calling findMedian
# At most 5 * 10^4 calls to addNum and findMedian


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

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


# if __name__ == "__main__":
#     mf = MedianFinder()
#     mf.addNum(1)
#     mf.addNum(2)
#     print(mf.findMedian())
#     mf.addNum(3)
#     print(mf.findMedian())
