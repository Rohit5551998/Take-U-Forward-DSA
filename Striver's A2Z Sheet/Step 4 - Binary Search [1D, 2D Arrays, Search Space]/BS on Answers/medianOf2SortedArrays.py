# mypy: disable-error-code="empty-body"
# QUESTION: Median of Two Sorted Arrays
# Given two sorted arrays a and b, return the median of the merged sorted array.
# If the combined length is even, the median is the average of the two middle
# elements.
# Example 1:
# Input: a = [1,2], b = [3,4]
# Output: 2.5
# Explanation: Merged = [1,2,3,4]; median = (2+3)/2 = 2.5.
# Constraints:
# 1 <= len(a) + len(b) <= 2*10^5

"""
#Brute Force:
1. Fully merge a and b, then pick the middle element (odd) or average the two
   middles (even).
TC -> O(N1 + N2), SC -> O(N1 + N2)

#Better Approach:
1. Merge conceptually with two pointers, no extra array. Track the two middle
   indices ind1, ind2 and capture their values as the counter passes them.
TC -> O(N1 + N2), SC -> O(1)

#Optimal Approach:
1. Ensure a is the smaller array. Left half must hold left = (n1+n2+1)//2 elements.
2. Binary search mid1 (elements taken from a) in [0, n1]; mid2 = left - mid1.
3. l1,l2 are the left-side maxima (or -inf); r1,r2 are the right-side minima (+inf).
   A valid split needs l1 <= r2 and l2 <= r1.
4. When valid: odd total -> median = max(l1, l2); even -> (max(l1,l2)+min(r1,r2))/2.
5. If l1 > r2 shrink a's left (high = mid1 - 1); else grow it (low = mid1 + 1).
TC -> O(log(min(N1, N2))), SC -> O(1)

#KEY INSIGHT:
- The median is a special "kth element" cut where the left half holds exactly half
  the elements; binary search the partition of the smaller array to find it.
"""

import math
from typing import List


class Solution:
    def median_brute(self, a: List[int], b: List[int]) -> float:
        merged: List[int] = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        return (merged[n // 2] + merged[n // 2 - 1]) / 2.0

    def median_better(self, a: List[int], b: List[int]) -> float:
        n1, n2 = len(a), len(b)
        n = n1 + n2
        ind1, ind2 = n // 2 - 1, n // 2
        ind1el, ind2el = -1, -1
        cnt, i, j = 0, 0, 0
        while i < n1 and j < n2:
            if a[i] < b[j]:
                val = a[i]
                i += 1
            else:
                val = b[j]
                j += 1
            if cnt == ind1:
                ind1el = val
            if cnt == ind2:
                ind2el = val
            cnt += 1
        while i < n1:
            if cnt == ind1:
                ind1el = a[i]
            if cnt == ind2:
                ind2el = a[i]
            cnt += 1
            i += 1
        while j < n2:
            if cnt == ind1:
                ind1el = b[j]
            if cnt == ind2:
                ind2el = b[j]
            cnt += 1
            j += 1
        if n % 2 == 1:
            return float(ind2el)
        return (ind1el + ind2el) / 2.0

    def median_optimal(self, a: List[int], b: List[int]) -> float:
        n1, n2 = len(a), len(b)
        if n1 > n2:
            return self.median_optimal(b, a)
        n = n1 + n2
        left = (n1 + n2 + 1) // 2
        low, high = 0, n1
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            l1 = a[mid1 - 1] if mid1 > 0 else -math.inf
            l2 = b[mid2 - 1] if mid2 > 0 else -math.inf
            r1 = a[mid1] if mid1 < n1 else math.inf
            r2 = b[mid2] if mid2 < n2 else math.inf
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return float(max(l1, l2))
                return (max(l1, l2) + min(r1, r2)) / 2.0
            if l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0.0


if __name__ == "__main__":
    sol = Solution()
    print(sol.median_optimal([1, 2], [3, 4]))
