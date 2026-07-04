# mypy: disable-error-code="empty-body"
# QUESTION: Largest rectangle in a histogram
# Given an array of integers 'heights' representing a histogram's bar heights where the
# width of each bar is 1, return the area of the largest rectangle in the histogram.
#
# Examples:
# Example:
#
# Input: N =6, heights[] = {2,1,5,6,2,3}
# Output: 10


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


class Solution:
    def largest_rectangle_in_a_histogram_brute(self, heights: List[int]) -> int:
        pass

    def largest_rectangle_in_a_histogram_better(self, heights: List[int]) -> int:
        pass

    def largest_rectangle_in_a_histogram_optimal(self, heights: List[int]) -> int:
        pass


if __name__ == "__main__":
    sol = Solution()
    heights = [2, 1, 5, 6, 2, 3]
    print(sol.largest_rectangle_in_a_histogram_optimal(heights))
