# mypy: disable-error-code="empty-body"
# QUESTION: Palindrome partitioning
# Given a string s, partition string s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitions of string s.
#
# Examples:
# Example 1:
# Input: s = "aabaa"
# Output: [["a", "a", "b", "a", "a"], ["a", "a", "b", "aa"], ["a", "aba", "a"],
#          ["aa", "b", "a", "a"], ["aa", "b", "aa"], ["aabaa"]]
# Explanation: Above are all the possible ways in which the string can be partitioned so that
# each substring is a palindrome.
#
# Example 2:
# Input: s = "baa"
# Output: [["b", "a", "a"], ["b", "aa"]]
# Explanation: Above are all the possible ways in which the string can be partitioned so that
# each substring is a palindrome.
#
# Constraints:
# 1 <= s.length <= 16
# s contains only lowercase English letters.


"""
#Brute Force:
SKIPPED — enumerating EVERY palindrome partition is inherently exhaustive; there
is no cruder non-recursive baseline. The backtracking below IS the natural first
(and only) solution for the "return all partitions" version of this problem.

#Better Approach:
SKIPPED — no intermediate tier. You could precompute an n×n isPalindrome DP table
to make each check O(1) instead of O(n), but that trims a factor inside the same
exponential algorithm — it doesn't change the approach class, so brute == optimal.

#Optimal Approach (partition_string + palindrome_partitioning_optimal):
1. Think of partitioning as repeatedly choosing "where does the FIRST piece end?"
   Every recursion level owns a starting position `index` and decides the cut.
2. Loop i from index to end. The candidate first piece is s[index..i]. Only if
   that substring is a palindrome is the cut legal — so check is_palindrome first.
3. If it's a palindrome, append it to the running partition `subs`, then recurse
   from i+1 to partition the REMAINING suffix the same way. This builds the rest
   of the partition on top of the piece we just committed to.
4. Backtrack: pop the piece so the next value of i starts from a clean slate and
   we explore a different first-cut length instead.
5. Base case: when index reaches the end of the string, every character has been
   consumed by some palindrome piece, so `subs` is one complete valid partition —
   append a COPY (list(subs)) to ans, since subs keeps mutating as we backtrack.
6. is_palindrome is a two-pointer scan over s[left..right] using index bounds
   (no substring allocation for the test), O(len) per call — this is the
   per-piece cost multiplied across the recursion tree.
TC -> O(2^n * n * k), SC -> O(n) recursion depth + O(output) for the answers
  (n = len(s); ~2^(n-1) possible partitions, each costs O(n) for palindrome
   checks along the path plus O(k) to copy a partition of ~k pieces)

#KEY INSIGHT:
- Model the problem as "pick the length of the next palindromic prefix, then
  recurse on the rest." The palindrome test on s[index..i] is what prunes illegal
  cuts, so we only ever descend into partitions that are valid so far — no invalid
  partition is ever fully built and thrown away.
"""

from typing import List


class Solution:
    def palindrome_partitioning_brute(self, s: str) -> List[List[str]]:
        # SKIP: enumerating all palindrome partitions is inherently exhaustive —
        # there's no cruder non-recursive baseline; backtracking is the first tier.
        pass

    def palindrome_partitioning_better(self, s: str) -> List[List[str]]:
        # SKIP: no intermediate tier — an n×n isPalindrome DP table only trims a
        # factor inside the same exponential algorithm, not the approach class.
        pass

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        ans = True
        while left < right:
            if s[left] != s[right]:
                ans = False
                break
            left += 1
            right -= 1
        return ans

    def partition_string(self, s: str, ans: List[List[str]], subs: List[str], index: int) -> None:
        if index == len(s):
            ans.append(list(subs))

        else:
            for i in range(index, len(s)):
                if self.is_palindrome(s, index, i):
                    subs.append(s[index : i + 1])
                    self.partition_string(s, ans, subs, i + 1)
                    subs.pop()

        return

    def palindrome_partitioning_optimal(self, s: str) -> List[List[str]]:
        ans = []
        subs = []
        self.partition_string(s, ans, subs, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "aabaa"
    print(sol.palindrome_partitioning_optimal(s))
