# mypy: disable-error-code="empty-body"
# QUESTION: Number of Substrings Containing All Three Characters
# Given a string s consisting only of characters 'a', 'b' and 'c', return the
# number of substrings containing at least one occurrence of all these characters.
# Example 1:
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one of each are "abc", "abca",
#   "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (last one).
# Example 2:
# Input: s = "aaacb"
# Output: 3
# Constraints:
# 3 <= s.length <= 5 * 10^4
# s consists only of 'a', 'b' and 'c'.

"""
#Brute Force:
1. Fix start i; extend j marking which of a/b/c have appeared.
2. The instant all three are present, every extension to the end is also valid,
   so add (n - j) and break the inner loop.
Why: once a window at i is complete, all longer windows from i are complete too.
TC -> O(N*N), SC -> O(1)

#Better Approach:
SKIPPED - no distinct middle tier between the O(N^2) scan and the O(N) last-seen trick.

#Optimal Approach (last-seen index):
1. Track lastSeen['a'/'b'/'c'], all initialized to -1.
2. At index i, update lastSeen[s[i]] = i. If all three are seen, let m = min of the three.
3. Then s[m], s[m-1], ..., s[0] are all valid left endpoints ending at i, i.e. add (m + 1).
Why: the smallest last-seen index is the latest possible left edge that still keeps
   all three chars; everything at or before it is valid.
TC -> O(N), SC -> O(1)

#KEY INSIGHT:
- For each right end i, the number of valid substrings ending at i equals
  (min last-seen index of a,b,c) + 1 - once all three have appeared.
"""


class Solution:
    def numberOfSubstrings_brute(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            seen: dict[str, int] = {}
            for j in range(i, len(s)):
                seen[s[j]] = 1
                if seen.get("a", 0) + seen.get("b", 0) + seen.get("c", 0) == 3:
                    count += len(s) - j
                    break
        return count

    def numberOfSubstrings_better(self, s: str) -> int:
        # SKIP: no distinct better tier; jump straight to the last-seen O(N) method.
        pass

    def numberOfSubstrings_optimal(self, s: str) -> int:
        count = 0
        lastSeen = {"a": -1, "b": -1, "c": -1}
        for i in range(len(s)):
            lastSeen[s[i]] = i
            mini = min(lastSeen["a"], lastSeen["b"], lastSeen["c"])
            if mini != -1:
                count += 1 + mini
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSubstrings_optimal("abcabc"))
