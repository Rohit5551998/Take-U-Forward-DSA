# mypy: disable-error-code="empty-body"
# QUESTION: Kth Largest Element in a Stream
# Design a class to find the kth largest element in a stream. Note that it is the
# kth largest element in the sorted order, not the kth distinct element.
# Implement KthLargest:
#   - KthLargest(k, nums): initialize with integer k and the stream nums
#   - add(val): append val to the stream and return the kth largest element in the
#     stream so far
#
# Example 1:
# Input:
#   KthLargest(3, [4, 5, 8, 2]); add(3); add(5); add(10); add(9); add(4)
# Output: 4, 5, 5, 8, 8
# Explanation: After each add, the 3rd largest element in the running stream is
# returned.
#
# Constraints:
# 1 <= k <= 10^4
# 0 <= nums.length <= 10^4
# -10^4 <= nums[i], val <= 10^4
# At most 10^4 calls to add


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

from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]) -> None:
        pass

    def add(self, val: int) -> int:
        pass


# if __name__ == "__main__":
#     kth = KthLargest(3, [4, 5, 8, 2])
#     print(kth.add(3), kth.add(5), kth.add(10), kth.add(9), kth.add(4))
