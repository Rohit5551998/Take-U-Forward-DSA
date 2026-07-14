# mypy: disable-error-code="empty-body"
# QUESTION: Assign Cookies
# There are some children and some cookies. Each child i has a greed factor g[i],
# the minimum size of a cookie the child will be content with. Each cookie j has a
# size s[j]. If s[j] >= g[i], we assign cookie j to child i, and the child is content.
# Maximize the number of content children and return that maximum number.
#
# Example 1:
# Input: g = [1, 2, 3], s = [1, 1]
# Output: 1
# Explanation: Only one cookie of size 1 satisfies the child with greed 1.
#
# Constraints:
# 1 <= len(g) <= 3 * 10^4
# 0 <= len(s) <= 3 * 10^4
# 1 <= g[i], s[j] <= 2^31 - 1

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
    def assign_cookies_brute(self, g: List[int], s: List[int]) -> int:
        pass

    def assign_cookies_better(self, g: List[int], s: List[int]) -> int:
        pass

    def assign_cookies_optimal(self, g: List[int], s: List[int]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.assign_cookies_optimal([1, 2, 3], [1, 1]))
