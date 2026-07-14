# mypy: disable-error-code="empty-body"
# QUESTION: Minimum Number of Platforms
# Given the arrival and departure times of all trains that reach a railway station,
# find the minimum number of platforms required so that no train has to wait. A train
# occupies a platform from its arrival time until its departure time (inclusive); if
# one train arrives at the same time another departs, they cannot share a platform.
#
# Example 1:
# Input: arr = [900, 940, 950, 1100, 1500, 1800]
#        dep = [910, 1200, 1120, 1130, 1900, 2000]
# Output: 3
# Explanation: At 950, trains that arrived at 940 and 950 overlap with none departed
# yet, requiring 3 platforms at peak.
#
# Constraints:
# 1 <= N <= 10^5
# 0 <= arr[i] <= dep[i] <= 2359 (times in 24-hour HHMM format)

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
    def minimum_platforms_brute(self, arr: List[int], dep: List[int]) -> int:
        pass

    def minimum_platforms_better(self, arr: List[int], dep: List[int]) -> int:
        pass

    def minimum_platforms_optimal(self, arr: List[int], dep: List[int]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(
#         sol.minimum_platforms_optimal(
#             [900, 940, 950, 1100, 1500, 1800],
#             [910, 1200, 1120, 1130, 1900, 2000],
#         )
#     )
