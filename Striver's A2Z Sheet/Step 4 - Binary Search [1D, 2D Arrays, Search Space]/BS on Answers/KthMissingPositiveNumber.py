# mypy: disable-error-code="empty-body"
# QUESTION: Kth Missing Positive Number
# Given a strictly increasing array of positive integers arr and an integer k,
# return the kth positive integer that is missing from arr.
# Example 1:
# Input: arr = [4,7,9,10], k = 4
# Output: 6
# Explanation: Missing positives are 1,2,3,5,6,8,... The 4th is 6.
# Constraints:
# 1 <= len(arr) <= 1000
# 1 <= arr[i] <= 1000, arr strictly increasing.

"""
#Brute Force:
1. Walk arr; while arr[i] <= k, that value shifts our target up by one so k += 1.
2. When arr[i] > k (or the array ends), k is the kth missing number.
TC -> O(N), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier; binary search is the improvement.

#Optimal Approach:
1. At index i, the count of missing numbers before arr[i] is arr[i] - (i + 1)
   (values seen vs values expected). This count is monotone increasing.
2. Binary search for the boundary: if missing(mid) < k go right (low = mid + 1),
   else go left (high = mid - 1).
3. After the loop, low is the first index with missing >= k. The answer is
   low + k (derivation: arr[high] + (k - missing(high)) simplifies to k + high + 1
   = k + low).
TC -> O(logN), SC -> O(1)

#KEY INSIGHT:
- The number of missing positives before each index is monotone, so binary search
  locates where the kth missing falls; a closed-form then gives the value.
"""

from typing import List


class Solution:
    def kth_missing_brute(self, arr: List[int], k: int) -> int:
        for x in arr:
            if x <= k:
                k += 1
            else:
                break
        return k

    def kth_missing_better(self, arr: List[int], k: int) -> int:
        # SKIP: no distinct better tier between linear scan and binary search.
        pass

    def kth_missing_optimal(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = low + (high - low) // 2
            missing = arr[mid] - (mid + 1)
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        return low + k


if __name__ == "__main__":
    sol = Solution()
    print(sol.kth_missing_optimal([4, 7, 9, 10], 4))
