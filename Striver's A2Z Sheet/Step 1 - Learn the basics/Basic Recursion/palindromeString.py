# mypy: disable-error-code="empty-body"
# QUESTION: Check if a String is a Palindrome using Recursion
# Given a string, determine whether it reads the same forwards and backwards.
# (Comparisons are case-insensitive and ignore non-alphanumeric characters.)
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
# Explanation: After cleaning -> "amanaplanacanalpanama", a palindrome.
# Constraints:
# 0 <= len(s) <= 100000

"""
#Brute Force:
1. Iterative two-pointer: compare s[l] and s[r] moving inward.
TC -> O(n), SC -> O(1)

#Better Approach:
SKIPPED - no distinct intermediate approach.

#Optimal Approach:
1. Recursive two-pointer over indices i and n-1-i.
2. If i has reached the middle (i >= n-1-i), all pairs matched -> return True.
3. If s[i] != s[n-1-i] return False; otherwise recurse with i+1.
TC -> O(n), SC -> O(n) recursion stack

#KEY INSIGHT:
- A string is a palindrome iff the outer character pair matches AND the inner substring
  is a palindrome; recursion peels one pair per frame.
"""

import re


class Solution:
    def isPalindrome_brute(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindrome_better(self, s: str) -> bool:
        # SKIP: no distinct intermediate approach.
        pass

    def isPalindrome_optimal(self, s: str, i: int) -> bool:
        n = len(s)
        if i >= n - 1 - i:
            return True
        if s[i] != s[n - 1 - i]:
            return False
        return self.isPalindrome_optimal(s, i + 1)


if __name__ == "__main__":
    sol = Solution()
    raw = "A man, a plan, a canal: Panama"
    cleaned = re.sub(r"[^a-zA-Z0-9]", "", raw).lower()
    print(sol.isPalindrome_optimal(cleaned, 0))
