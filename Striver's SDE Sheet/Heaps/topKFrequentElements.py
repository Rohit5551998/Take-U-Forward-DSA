# QUESTION: Top K Frequent Elements
# Given an integer array `nums` and an integer k, return the k most
# frequent elements. You may return the answer in any order.
#
# Examples:
# Example 1:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
# Follow up: Your algorithm's time complexity must be better than
# O(n log n), where n is the array's size.
#
# Approaches:
#   - O(n + u log u): count frequencies with a hashmap, then sort
#     entries by count.
#   - O(n + u log k): count frequencies, then keep a min-heap of size k
#     keyed by frequency.
#   - O(n): count frequencies, then use bucket sort indexed by
#     frequency (buckets of size up to n).


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


def top_k_frequent_elements_brute() -> None:
    pass


def top_k_frequent_elements_better() -> None:
    pass


def top_k_frequent_elements_optimal() -> None:
    pass
