# mypy: disable-error-code="empty-body"
# QUESTION: Fruit Into Baskets
# You have two baskets, each can hold only one type of fruit (unlimited count).
# Given fruits[i] = type of fruit at tree i, starting from any tree pick one fruit
# per tree moving right, stopping when a fruit can't fit. Return the maximum fruits
# you can pick. Equivalent to: longest subarray with at most 2 distinct values.
# Example 1:
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees (types {1,2}).
# Example 2:
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2] (types {2,3}).
# Constraints:
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length

"""
#Brute Force:
1. Fix start i; extend j collecting distinct fruit types in a set.
2. While the set size stays <= 2, update max length; else break.
Why: literal check of the "at most 2 baskets" rule on every window.
TC -> O(N*N), SC -> O(1)   (set size bounded by 3)

#Better Approach:
1. Sliding window with a count map; expand r, adding fruits[r].
2. While more than 2 distinct types, shrink from l, deleting a type when its count hits 0.
3. Record window length once valid.
Why: window shrinks only as needed; each index enters/leaves once.
TC -> O(2N), SC -> O(1)

#Optimal Approach:
1. Same map, but shrink at most one step (if instead of while).
2. When distinct > 2, slide both edges by one so the window only translates.
3. Max length is monotonic, so a translating window still captures the best.
Why: we only care about the longest window, so the left edge never needs to pass the best.
TC -> O(N), SC -> O(1)

#KEY INSIGHT:
- Reframe the puzzle as "longest subarray with <= 2 distinct elements" and solve
  with a size-monotonic sliding window.
"""

from typing import List


class Solution:
    def totalFruit_brute(self, fruits: List[int]) -> int:
        maxLen = 0
        for i in range(len(fruits)):
            types: set[int] = set()
            for j in range(i, len(fruits)):
                types.add(fruits[j])
                if len(types) <= 2:
                    maxLen = max(maxLen, j - i + 1)
                else:
                    break
        return maxLen

    def totalFruit_better(self, fruits: List[int]) -> int:
        maxLen = 0
        mpp: dict[int, int] = {}
        left = 0
        for r in range(len(fruits)):
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1
            while len(mpp) > 2:
                mpp[fruits[left]] -= 1
                if mpp[fruits[left]] == 0:
                    del mpp[fruits[left]]
                left += 1
            maxLen = max(maxLen, r - left + 1)
        return maxLen

    def totalFruit_optimal(self, fruits: List[int]) -> int:
        maxLen = 0
        mpp: dict[int, int] = {}
        left = 0
        for r in range(len(fruits)):
            mpp[fruits[r]] = mpp.get(fruits[r], 0) + 1
            if len(mpp) > 2:
                mpp[fruits[left]] -= 1
                if mpp[fruits[left]] == 0:
                    del mpp[fruits[left]]
                left += 1
            else:
                maxLen = max(maxLen, r - left + 1)
        return maxLen


if __name__ == "__main__":
    sol = Solution()
    print(sol.totalFruit_optimal([1, 2, 3, 2, 2]))
