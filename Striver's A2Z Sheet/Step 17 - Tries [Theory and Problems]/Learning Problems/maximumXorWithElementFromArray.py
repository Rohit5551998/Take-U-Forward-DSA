# mypy: disable-error-code="empty-body"
# QUESTION: Maximum XOR With an Element From Array
# You are given an array nums of non-negative integers and a 2D array queries where
# queries[i] = [xi, mi]. The answer to the i-th query is the maximum bitwise XOR
# value of xi and any element of nums that does not exceed mi. In other words, the
# answer is max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements
# in nums are larger than mi, then the answer is -1.
# Return an integer array answer where answer.length == queries.length and
# answer[i] is the answer to the i-th query.
#
# Example 1:
# Input: nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# Output: [3,3,7]
# Explanation:
#   [3,1] -> nums with value <= 1 are [0,1]; max(3^0,3^1)=max(3,2)=3
#   [1,3] -> nums with value <= 3 are [0,1,2,3]; max(1^0..1^3)=3
#   [5,6] -> nums with value <= 6 are [0,1,2,3,4]; max(5^0..5^4)=7
#
# Example 2:
# Input: nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# Output: [15,-1,5]
#
# Constraints:
# - 1 <= nums.length, queries.length <= 10^5
# - queries[i].length == 2
# - 0 <= nums[j], xi, mi <= 10^9

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
    def maximizeXor_brute(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pass

    def maximizeXor_better(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pass

    def maximizeXor_optimal(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pass


if __name__ == "__main__":
    # sol = Solution()
    # print(sol.maximizeXor_optimal([0, 1, 2, 3, 4], [[3, 1], [1, 3], [5, 6]]))
    pass
