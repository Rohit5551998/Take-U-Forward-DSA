# mypy: disable-error-code="empty-body"
# QUESTION: Minimum Window Substring
# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates) is
# included in the window. If there is no such substring, return the empty string "".
# The answer is guaranteed to be unique.
#
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'.
#
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
#
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be in the window, but s has only one 'a'.
#
# Constraints:
# m == s.length, n == t.length
# 1 <= m, n <= 10^5
# s and t consist of uppercase and lowercase English letters.

"""
#Brute Force:
1. For every start index i, build the frequency map of t, then a running "cnt" of how
   many of t's required characters are still satisfied.
2. Expand j from i: if s[j] is currently needed (map value > 0) increment cnt, then
   decrement the map for s[j] (a negative value means s[j] is a surplus character).
3. The first time cnt == len(t) the window [i..j] contains all of t; record its length
   if smaller and break (no need to grow this window further).
TC -> O(N*N), SC -> O(256)   (fixed-size alphabet map)

#Better Approach:
SKIPPED — the natural progression from the O(N^2) restart-per-index scan is directly
the two-pointer sliding window; there is no distinct intermediate technique.

#Optimal Approach:
1. Build t's frequency map once and set cnt = number of t-chars still needed.
2. Expand r across s: if map[s[r]] > 0 the char was needed, so increment cnt; then
   decrement map[s[r]] (surplus chars go negative, harmlessly).
3. While cnt == len(t) the window is valid: record [l..r] if it beats the best, then
   shrink from the left — add s[l] back to the map, and if that makes map[s[l]] > 0
   we have removed a genuinely-needed char so decrement cnt; advance l.
4. Return the best recorded window (via startIndex + minLen), or "" if none found.
TC -> O(2N) + O(M), SC -> O(256)

#KEY INSIGHT:
- A single counter "cnt" of satisfied requirements lets us test window validity in
  O(1). Right pointer only ever adds; left pointer only ever removes — so each index
  is touched at most twice, giving linear time. Surplus characters going negative in
  the map is what lets shrinking know exactly when a needed char is lost.
"""

import math
from typing import Dict


class Solution:
    def minWindow_brute(self, s: str, t: str) -> str:
        minLen = math.inf
        startIndex = -1
        n = len(s)
        for i in range(n):
            mpp: Dict[str, int] = {}
            for ch in t:
                mpp[ch] = mpp.get(ch, 0) + 1
            cnt = 0
            for j in range(i, n):
                if mpp.get(s[j], 0) > 0:
                    cnt += 1
                mpp[s[j]] = mpp.get(s[j], 0) - 1
                if cnt == len(t):
                    if (j - i + 1) < minLen:
                        startIndex = i
                        minLen = j - i + 1
                    break
        return s[startIndex : startIndex + int(minLen)] if startIndex != -1 else ""

    def minWindow_better(self, s: str, t: str) -> str:
        # SKIP: the step up from brute is directly the optimal sliding window.
        pass

    def minWindow_optimal(self, s: str, t: str) -> str:
        minLen = math.inf
        startIndex = -1
        cnt = 0
        left = 0
        mpp: Dict[str, int] = {}
        for ch in t:
            mpp[ch] = mpp.get(ch, 0) + 1

        for r in range(len(s)):
            if mpp.get(s[r], 0) > 0:
                cnt += 1
            mpp[s[r]] = mpp.get(s[r], 0) - 1

            while cnt == len(t):
                if r - left + 1 < minLen:
                    minLen = r - left + 1
                    startIndex = left
                mpp[s[left]] += 1
                if mpp[s[left]] > 0:
                    cnt -= 1
                left += 1

        return s[startIndex : startIndex + int(minLen)] if startIndex != -1 else ""


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow_optimal("ADOBECODEBANC", "ABC"))  # BANC
