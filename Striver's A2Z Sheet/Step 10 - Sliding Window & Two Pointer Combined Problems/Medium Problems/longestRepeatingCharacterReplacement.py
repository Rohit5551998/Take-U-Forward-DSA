# mypy: disable-error-code="empty-body"
# QUESTION: Longest Repeating Character Replacement
# You are given a string s and an integer k. You can choose any character of the
# string and change it to any other uppercase English character. You can do this
# at most k times. Return the length of the longest substring containing the same
# letter you can get after performing the above operations.
# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with 'B's or vice versa.
# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle -> "AABBBBA" has "BBBB".
# Constraints:
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.
# 0 <= k <= s.length

"""
#Brute Force:
1. Fix start i; extend j maintaining a freq map and maxFreq (highest single-char count).
2. Changes needed = windowLen - maxFreq. While changes <= k the window is achievable.
3. Update max length; break once changes exceed k.
Why: a window can become one letter iff we replace all non-majority chars (<= k of them).
TC -> O(N*N), SC -> O(1)   (map bounded by 26)

#Better Approach:
1. Sliding window: expand r, update maxFreq.
2. While windowLen - maxFreq > k, shrink from l (decrement its freq).
3. Record the valid window length.
Why: same replacement rule but amortized single-pass shrinking.
TC -> O(2N), SC -> O(1)

#Optimal Approach:
1. Same window but shrink at most one step (if instead of while) - and we deliberately
   do NOT recompute maxFreq downward.
2. Because the answer only grows, a stale (never-decreasing) maxFreq is safe: the window
   only translates, never reporting a smaller-than-best length.
Why: maxFreq is monotonic non-decreasing over the run, so the window size is monotonic.
TC -> O(N), SC -> O(1)

#KEY INSIGHT:
- A window is valid iff (length - count of its most frequent char) <= k. Keeping a
  non-decreasing maxFreq lets the window grow monotonically without ever shrinking below best.
"""


class Solution:
    def characterReplacement_brute(self, s: str, k: int) -> int:
        maxLen = 0
        for i in range(len(s)):
            mpp: dict[str, int] = {}
            maxFreq = 0
            for j in range(i, len(s)):
                mpp[s[j]] = mpp.get(s[j], 0) + 1
                maxFreq = max(maxFreq, mpp[s[j]])
                if (j - i + 1) - maxFreq <= k:
                    maxLen = max(maxLen, j - i + 1)
                else:
                    break
        return maxLen

    def characterReplacement_better(self, s: str, k: int) -> int:
        maxLen = 0
        maxFreq = 0
        mpp: dict[str, int] = {}
        left = 0
        for r in range(len(s)):
            mpp[s[r]] = mpp.get(s[r], 0) + 1
            maxFreq = max(maxFreq, mpp[s[r]])
            while (r - left + 1) - maxFreq > k:
                mpp[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, r - left + 1)
        return maxLen

    def characterReplacement_optimal(self, s: str, k: int) -> int:
        maxLen = 0
        maxFreq = 0
        mpp: dict[str, int] = {}
        left = 0
        for r in range(len(s)):
            mpp[s[r]] = mpp.get(s[r], 0) + 1
            maxFreq = max(maxFreq, mpp[s[r]])
            if (r - left + 1) - maxFreq > k:
                mpp[s[left]] -= 1
                left += 1
            else:
                maxLen = max(maxLen, r - left + 1)
        return maxLen


if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement_optimal("AABABBA", 1))
