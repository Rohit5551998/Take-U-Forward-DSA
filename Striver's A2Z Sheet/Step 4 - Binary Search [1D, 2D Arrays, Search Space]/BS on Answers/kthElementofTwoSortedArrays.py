# mypy: disable-error-code="empty-body"
# QUESTION: Kth Element of Two Sorted Arrays
# Given two sorted arrays a and b and an integer k, return the kth (1-indexed)
# smallest element of the merged sorted array.
# Example 1:
# Input: a = [1,2], b = [3,4], k = 4
# Output: 4
# Explanation: Merged = [1,2,3,4]; the 4th element is 4.
# Constraints:
# 1 <= len(a), len(b) <= 10^5
# 1 <= k <= len(a) + len(b)

"""
#Brute Force:
1. Fully merge a and b into one sorted array, then return element at index k-1.
TC -> O(N1 + N2), SC -> O(N1 + N2)

#Better Approach:
1. Merge conceptually with two pointers but do NOT store the merged array; keep a
   counter and capture the value when the counter hits k-1.
TC -> O(N1 + N2), SC -> O(1)

#Optimal Approach:
1. Ensure a is the smaller array (swap if needed). We choose a partition taking
   `left = k` elements from the left across both arrays.
2. Binary search mid1 (count taken from a) in [max(0, k-n2), min(n1, k)];
   mid2 = k - mid1 comes from b.
3. l1,l2 = last elements on the left of each array (or -inf); r1,r2 = first on the
   right (or +inf). A valid partition satisfies l1 <= r2 and l2 <= r1.
4. When valid, the kth element is max(l1, l2). If l1 > r2 shrink a's left
   (high = mid1 - 1), else grow it (low = mid1 + 1).
TC -> O(log(min(N1, N2))), SC -> O(1)

#KEY INSIGHT:
- Finding the kth element is choosing where to cut so that exactly k elements sit
  on the left across both arrays with left-max <= right-min; binary search the cut.
"""

import math
from typing import List


class Solution:
    def kth_element_brute(self, a: List[int], b: List[int], k: int) -> int:
        merged: List[int] = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged[k - 1]

    def kth_element_better(self, a: List[int], b: List[int], k: int) -> int:
        m, n = len(a), len(b)
        cnt = 0
        i, j = 0, 0
        ele = -1
        while i < m and j < n:
            if a[i] < b[j]:
                if cnt == k - 1:
                    ele = a[i]
                cnt += 1
                i += 1
            else:
                if cnt == k - 1:
                    ele = b[j]
                cnt += 1
                j += 1
        while i < m:
            if cnt == k - 1:
                ele = a[i]
            cnt += 1
            i += 1
        while j < n:
            if cnt == k - 1:
                ele = b[j]
            cnt += 1
            j += 1
        return ele

    def kth_element_optimal(self, a: List[int], b: List[int], k: int) -> int:
        n1, n2 = len(a), len(b)
        if n1 > n2:
            return self.kth_element_optimal(b, a, k)
        left = k
        low, high = max(0, k - n2), min(n1, k)
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
            l1 = a[mid1 - 1] if mid1 > 0 else -math.inf
            l2 = b[mid2 - 1] if mid2 > 0 else -math.inf
            r1 = a[mid1] if mid1 < n1 else math.inf
            r2 = b[mid2] if mid2 < n2 else math.inf
            if l1 <= r2 and l2 <= r1:
                return int(max(l1, l2))
            if l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    print(sol.kth_element_optimal([1, 2], [3, 4], 4))
