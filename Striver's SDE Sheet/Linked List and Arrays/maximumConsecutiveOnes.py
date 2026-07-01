# QUESTION: Maximum Consecutive Ones
# Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array.


"""
#Brute Force:
SKIPPED — a single linear scan is already the natural approach; there is no slower "brute"
worth writing (re-scanning to measure each run would just be a worse O(n^2) version of the same).

#Better Approach:
SKIPPED — nothing sits between the trivial scan and the optimal; they are the same O(n)/O(1) idea.

#Optimal Approach:
1. The answer is the longest unbroken run of 1s. Any 0 ends the current run, so we only need
   to track the length of the current run and the best run seen so far in one pass.
2. Walk the array keeping cnt = length of the current streak of 1s. On a 1, extend the streak
   (cnt += 1); on a 0, the streak is broken so reset cnt = 0.
3. After each element, update maxi = max(maxi, cnt) so the best streak is captured even when the
   array ends while still inside a run of 1s.
4. Return maxi. One pass, no extra storage.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- The longest run of 1s only ever needs the current streak length and the max so far — a 0
  resets the streak — so a single O(1)-space pass suffices; there is nothing to optimize past it.
"""

from typing import List


class Solution:
    def maximum_consecutive_ones_brute(self) -> None:
        # SKIP: a single linear scan is the natural approach; no slower brute worth writing.
        pass

    def maximum_consecutive_ones_better(self) -> None:
        # SKIP: nothing sits between the trivial scan and the optimal — same O(n)/O(1) idea.
        pass

    def maximum_consecutive_ones_optimal(self, nums: List[int]) -> int:
        cnt = 0
        maxi = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            maxi = max(maxi, cnt)

        return maxi


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 0, 1, 1, 1]
    print(sol.maximum_consecutive_ones_optimal(nums))
