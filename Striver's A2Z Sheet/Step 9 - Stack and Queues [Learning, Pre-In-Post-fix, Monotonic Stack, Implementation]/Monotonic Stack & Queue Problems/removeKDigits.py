# mypy: disable-error-code="empty-body"
# QUESTION: Remove K Digits
# Given a non-negative integer as a string num and an integer k, remove exactly
# k digits so the resulting number is the smallest possible. Return it as a
# string (without leading zeros; "0" if empty).
# Example 1:
# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Removing 4, 3 and 2 leaves the smallest number 1219.
# Constraints:
# 1 <= k <= num.length <= 10^5
# num consists of digits and has no leading zeros except "0" itself.

"""
#Optimal Approach:
1. Build a monotonic increasing stack of digits. For each digit, while the top
   is greater than the current digit and k > 0, pop it (removing a larger, more
   significant digit lowers the value most). Push the current digit.
2. If k remains after the scan, the digits are non-decreasing, so remove the last
   k digits from the end.
3. Strip leading zeros; if the result is empty return "0", else join it.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- A greedy monotonic stack removes the leftmost "peak" digit each time, which
  reduces the number more than removing any later digit for the same cost.
"""


class Solution:
    def findSolution(self, num: str, k: int) -> str:
        st: list[str] = []
        for value in num:
            while st and k > 0 and st[-1] > value:
                k -= 1
                st.pop()
            st.append(value)

        while st and k > 0:
            k -= 1
            st.pop()

        while st and st[0] == "0":
            st = st[1:]

        if not st:
            return "0"
        return "".join(st)


if __name__ == "__main__":
    print(Solution().findSolution("1432219", 3))
