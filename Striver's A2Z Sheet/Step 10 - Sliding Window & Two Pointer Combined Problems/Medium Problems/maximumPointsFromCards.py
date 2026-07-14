# mypy: disable-error-code="empty-body"
# QUESTION: Maximum Points You Can Obtain from Cards
# There are cards arranged in a row, cardPoints[i] is the score of the i-th card.
# In one step you take one card from the beginning or the end of the row. You must
# take exactly k cards. Return the maximum score obtainable.
# Example 1:
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: Take the three from the right end: 1 + 6 + 5 = 12.
# Example 2:
# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Constraints:
# 1 <= cardPoints.length <= 10^5
# 1 <= cardPoints[i] <= 10^4
# 1 <= k <= cardPoints.length

"""
#Brute Force:
1. Any choice of k cards from the ends is: take some prefix of length p and some
   suffix of length k-p. Try all p from 0..k, summing prefix+suffix each time.
2. Track the max.
Why: enumerates every legal split between left-taken and right-taken cards.
TC -> O(N*K) if sums recomputed, SC -> O(1)

#Better Approach:
SKIPPED - no distinct middle tier; the sliding-sum below is the direct O(K) optimal.

#Optimal Approach (sliding the split):
1. Start by taking the first k cards; record that sum as the initial answer.
2. Slide the "cut" one card at a time: drop the rightmost taken-from-left card and
   instead take the next card from the right end. Update the running sum in O(1).
3. Track the running max across all splits.
Why: each of the k+1 prefix/suffix splits is reached by one O(1) swap from the previous.
TC -> O(2K), SC -> O(1)

#KEY INSIGHT:
- Taking k cards from the two ends = choosing a prefix of size p and suffix of size
  k-p. Slide the boundary maintaining the sum incrementally instead of resumming.
"""

from typing import List


class Solution:
    def maxScore_brute(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        maxPoints = 0
        for p in range(k + 1):
            left = sum(cardPoints[:p])
            right = sum(cardPoints[n - (k - p) :]) if (k - p) > 0 else 0
            maxPoints = max(maxPoints, left + right)
        return maxPoints

    def maxScore_better(self, cardPoints: List[int], k: int) -> int:
        # SKIP: no distinct better tier; go straight to the O(K) sliding-sum optimal.
        pass

    def maxScore_optimal(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        sumPoints = sum(cardPoints[:k])
        maxPoints = sumPoints
        for i in range(k - 1, -1, -1):
            sumPoints -= cardPoints[i]
            sumPoints += cardPoints[n + i - k]
            maxPoints = max(maxPoints, sumPoints)
        return maxPoints


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxScore_optimal([1, 2, 3, 4, 5, 6, 1], 3))
