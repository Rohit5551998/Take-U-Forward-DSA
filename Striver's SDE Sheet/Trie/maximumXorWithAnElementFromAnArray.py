# QUESTION: Maximum Xor with an element from an array
# Given an array nums consisting of non-negative integers and a queries array, where
# queries[i] = [xi, mi]. The answer to the ith query is the maximum bitwise XOR value of xi and
# any element of nums that does not exceed mi. In other words, the answer is
# max(nums[j] XOR xi) for all j such that nums[j] <= mi. If all elements in nums are larger
# than mi, then the answer is -1.
# Return an integer array answer where answer.length == queries.length and answer[i] is the
# answer to the ith query.
#
# Examples:
# Example 1:
# Input: nums = [4, 9, 2, 5, 0, 1], queries = [[3, 0], [3, 10], [7, 5], [7, 9]]
# Output: [3, 10, 7, 14]
# Explanation:
# 1st query: x = 3, m = 0. There is only one number less than or equal to m, i.e. 0.
# 0 XOR 3 = 3. The answer is 3.
# 2nd query: x = 3, m = 10. The maximum XOR is 3 XOR 9 = 10.
# 3rd query: x = 7, m = 5. The maximum XOR is 7 XOR 0 = 7.
# 4th query: x = 7, m = 9. The maximum XOR is 7 XOR 9 = 14.
#
# Example 2:
# Input: nums = [0, 1, 2, 3, 4], queries = [[3, 1], [1, 3], [5, 6]]
# Output: [3, 3, 7]
# Explanation:
# 1st query: x = 3, m = 1. There are only two numbers less than or equal to m, i.e. 0 and 1.
# 0 XOR 3 = 3, 1 XOR 3 = 2. The larger value is 3.
# 2nd query: x = 1, m = 3. The maximum XOR is 1 XOR 2 = 3.
# 3rd query: x = 5, m = 6. The maximum XOR is 5 XOR 2 = 7.
#
# Constraints:
# - 1 <= nums.length, queries.length <= 10^5
# - queries[i].length == 2
# - 0 <= nums[i], xi, mi <= 10^9


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
    def maximum_xor_with_an_element_from_an_array_brute(self) -> None:
        pass

    def maximum_xor_with_an_element_from_an_array_better(self) -> None:
        pass

    def maximum_xor_with_an_element_from_an_array_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
