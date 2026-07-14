# mypy: disable-error-code="empty-body"
# QUESTION: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Constraints:
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.

"""
#Brute Force:
1. Fix a start index i; extend j and collect characters into a set.
2. The moment a character repeats, the window can grow no further from i, so break.
3. Track the max window length seen across all starts.
Why: every substring is examined, but the set gives O(1) duplicate detection.
TC -> O(N*N), SC -> O(N)

#Better Approach:
SKIPPED - no distinct middle tier; the sliding window (below) is the direct optimal jump from brute.

#Optimal Approach:
1. Keep a dict last[ch] = most recent index of ch, and a left pointer l.
2. Move r across the string. If s[r] was seen and its last index is >= l, jump
   l to last[s[r]] + 1 (max(l, ...) guards against l already being ahead, e.g. "acca").
3. Record last[s[r]] = r and update answer with r - l + 1.
Why: l never moves backward, so each character is visited once.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- The window is valid iff it has no repeats; on a repeat, jump the left edge just
  past the previous occurrence instead of shrinking one step at a time.
"""


class Solution:
    def lengthOfLongestSubstring_brute(self, s: str) -> int:
        maxAns = 0
        for i in range(len(s)):
            found: set[str] = set()
            for j in range(i, len(s)):
                if s[j] in found:
                    break
                found.add(s[j])
            maxAns = max(maxAns, len(found))
        return maxAns

    def lengthOfLongestSubstring_better(self, s: str) -> int:
        # SKIP: no distinct better tier; optimal sliding window is the direct improvement.
        pass

    def lengthOfLongestSubstring_optimal(self, s: str) -> int:
        maxAns = 0
        left = 0
        last: dict[str, int] = {}
        for r in range(len(s)):
            if s[r] in last:
                left = max(left, last[s[r]] + 1)
            last[s[r]] = r
            maxAns = max(maxAns, r - left + 1)
        return maxAns


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring_optimal("abcabcbb"))
