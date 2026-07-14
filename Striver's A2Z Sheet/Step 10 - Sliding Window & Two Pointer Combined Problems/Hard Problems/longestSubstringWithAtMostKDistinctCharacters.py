# mypy: disable-error-code="empty-body"
# QUESTION: Longest Substring with At Most K Distinct Characters
# Given a string s and an integer k, return the length of the longest substring of s
# that contains at most k distinct characters.
# Example 1:
# Input: s = "aaabbccd", k = 2
# Output: 5
# Explanation: "aaabb" contains 2 distinct characters ('a','b') and has length 5.
# Example 2:
# Input: s = "abcddefg", k = 3
# Output: 4
# Explanation: "cdde" has 3 distinct characters and length 4.
# Constraints:
# 1 <= s.length <= 5 * 10^4
# 0 <= k <= 26

"""
#Brute Force:
1. Fix start i; extend j collecting distinct characters in a set.
2. While the set size stays <= k, update max length; else break.
Why: literal check of the "at most k distinct" rule on every window.
TC -> O(N*N), SC -> O(K)

#Better Approach:
1. Sliding window with a count map; expand r adding s[r].
2. While distinct count > k, shrink from l, deleting a char when its count hits 0.
3. Record the valid window length.
Why: each index enters and leaves the window once.
TC -> O(2N), SC -> O(K)

#Optimal Approach:
1. Same map, but shrink at most one step (if instead of while).
2. When distinct > k, slide both edges by one so the window only translates.
3. Max length is monotonic, so a translating window still captures the best.
Why: we only want the longest window, so the left edge never has to pass the best.
TC -> O(N), SC -> O(K)

#KEY INSIGHT:
- The "longest window with <= k distinct" answer is size-monotonic, so once the
  window reaches its best length it need only translate, never shrink below it.
"""


class Solution:
    def kDistinctChars_brute(self, s: str, k: int) -> int:
        maxLen = 0
        for i in range(len(s)):
            distinct: set[str] = set()
            for j in range(i, len(s)):
                distinct.add(s[j])
                if len(distinct) <= k:
                    maxLen = max(maxLen, j - i + 1)
                else:
                    break
        return maxLen

    def kDistinctChars_better(self, s: str, k: int) -> int:
        maxLen = 0
        mpp: dict[str, int] = {}
        left = 0
        for r in range(len(s)):
            mpp[s[r]] = mpp.get(s[r], 0) + 1
            while len(mpp) > k:
                mpp[s[left]] -= 1
                if mpp[s[left]] == 0:
                    del mpp[s[left]]
                left += 1
            maxLen = max(maxLen, r - left + 1)
        return maxLen

    def kDistinctChars_optimal(self, s: str, k: int) -> int:
        maxLen = 0
        mpp: dict[str, int] = {}
        left = 0
        for r in range(len(s)):
            mpp[s[r]] = mpp.get(s[r], 0) + 1
            if len(mpp) > k:
                mpp[s[left]] -= 1
                if mpp[s[left]] == 0:
                    del mpp[s[left]]
                left += 1
            else:
                maxLen = max(maxLen, r - left + 1)
        return maxLen


if __name__ == "__main__":
    sol = Solution()
    print(sol.kDistinctChars_optimal("aaabbccd", 2))
