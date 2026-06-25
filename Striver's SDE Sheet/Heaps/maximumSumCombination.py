# QUESTION: Maximum Sum Combination
# Given two integer arrays nums1 and nums2 (of equal length n) and an
# integer k, return the maximum k valid sum combinations from all
# possible sum combinations, where each sum is formed by picking one
# element from nums1 and one element from nums2 (one of each per pair).
# A sum combination is the sum nums1[i] + nums2[j] for any valid pair of
# indices (i, j). Return the top k such sums in non-increasing order.
#
# Optimal approach: use a max-heap (priority queue). Sort both arrays in
# descending order, then push the top combination (nums1[0]+nums2[0])
# and explore neighbors greedily, using a visited set to avoid
# duplicates.
#
# Examples:
# Input : nums1 = [7, 3], nums2 = [1, 6], k = 2
#  Output : [13, 9]
#  Explanation : The 2 maximum combinations are made by: nums1[0] + nums2[1] = 13 nums1[1] + nums2[1] = 9
#
#  Input : nums1 = [3, 4, 5], nums2 = [2, 6, 3], k = 2
# Output : [11, 10]
# Explanation : The 2 maximum combinations are made by: nums1[2] + nums2[1] = 11 nums1[1] + nums2[1] = 10


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
    def maximum_sum_combination_brute(self) -> None:
        pass

    def maximum_sum_combination_better(self) -> None:
        pass

    def maximum_sum_combination_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
