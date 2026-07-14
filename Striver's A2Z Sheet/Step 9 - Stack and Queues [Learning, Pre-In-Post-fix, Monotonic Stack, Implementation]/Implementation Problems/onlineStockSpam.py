# mypy: disable-error-code="empty-body"
# QUESTION: Online Stock Span
# Design a StockSpanner that, given today's stock price via next(price), returns
# the span: the number of consecutive days (ending today) the price was <=
# today's price.
# Example 1:
# Input: prices = [100, 80, 60, 70, 60, 75, 85] (fed one by one to next)
# Output: [1, 1, 1, 2, 1, 4, 6]
# Explanation: For 70 the span is 2 (70, 60); for 85 the span is 6.
# Constraints:
# 1 <= price <= 10^5
# next is called up to 10^4 times.

"""
#Optimal Approach:
1. Keep a monotonic (decreasing) stack of indices of previous prices plus the
   full price history and a running index.
2. On next(price): record the price, then pop all stack indices whose price is
   <= today's price (those days are engulfed by today's span).
3. The previous greater element is the new stack top (or -1). Push today's index.
4. Span = currentIndex - previousGreaterIndex.
TC -> O(1) amortised per call (each index pushed/popped once), SC -> O(N)

#KEY INSIGHT:
- The span reaches back to the most recent strictly-greater price, so a
  decreasing monotonic stack of indices gives that boundary in amortised O(1).
"""


class Solution:
    def __init__(self) -> None:
        self.stockList: list[int] = []
        self.stack: list[int] = []
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        self.stockList.append(price)
        while self.stack and price >= self.stockList[self.stack[-1]]:
            self.stack.pop()
        pge = -1 if not self.stack else self.stack[-1]
        self.stack.append(self.index)
        return self.index - pge


if __name__ == "__main__":
    prices = [100, 80, 60, 70, 60, 75, 85]
    spanner = Solution()
    print([spanner.next(price) for price in prices])
