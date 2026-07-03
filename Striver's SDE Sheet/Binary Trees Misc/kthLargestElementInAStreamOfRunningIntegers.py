# QUESTION: Kth largest element in a stream of running integers
# Implement a class KthLargest to find the k-th largest number in a stream. It should have the
# following methods:
# - KthLargest(int k, int[] nums): Initializes the object with the integer k and the initial
#   stream of numbers in nums.
# - int add(int val): Appends the integer val to the stream and returns the k-th largest
#   element in the stream.
# Note that it is the k-th largest element in the sorted order, not the k-th distinct element.
#
# Examples:
# Example 1:
# Input: [KthLargest(3, [1, 2, 3, 4]), add(5), add(2), add(7)]
# Output: [null, 3, 3, 4]
# Explanation: initial stream = [1, 2, 3, 4], k = 3.
# add(5): stream = [1, 2, 3, 4, 5] -> returns 3
# add(2): stream = [1, 2, 2, 3, 4, 5] -> returns 3
# add(7): stream = [1, 2, 2, 3, 4, 5, 7] -> returns 4
#
# Example 2:
# Input: [KthLargest(2, [5, 5, 5, 5]), add(2), add(6), add(60)]
# Output: [null, 5, 5, 6]
# Explanation: initial stream = [5, 5, 5, 5], k = 2.
# add(2): stream = [5, 5, 5, 5, 2] -> returns 5
# add(6): stream = [5, 5, 5, 5, 2, 6] -> returns 5
# add(60): stream = [5, 5, 5, 5, 2, 6, 60] -> returns 6
#
# Constraints:
# 1 <= Number of instructions <= 1000
# -10^4 <= val & all initial values <= 10^4
# 1 <= k <= 10^4
# k - 1 <= nums.length <= 10^3
# The stream will have at least k elements after any add call.


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


class Solution:
    def kth_largest_element_in_a_stream_of_running_integers_brute(self) -> None:
        pass

    def kth_largest_element_in_a_stream_of_running_integers_better(self) -> None:
        pass

    def kth_largest_element_in_a_stream_of_running_integers_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
