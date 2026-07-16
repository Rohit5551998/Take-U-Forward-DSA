# QUESTION: Kth element of 2 sorted arrays
# Given two sorted arrays `a` and `b` of size m and n respectively, find
# the k-th element (1-indexed) of the final sorted array obtained by
# merging them.
#
# Examples:
# Example 1:
# Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5
# Output: 6
# Explanation: The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th
# element of this array is 6.
#
# Example 2:
# Input: a = [100, 112, 256, 349, 770], b = [72, 86, 113, 119, 265, 445, 892], k = 7
# Output: 256
# Explanation: The final sorted array is [72, 86, 100, 112, 113, 119, 256, 265, 349, 445,
# 770, 892]. The 7th element of this array is 256.


"""
#Brute Force:
1. The k-th element of the merged array is trivially found if we actually
   build that merged array. So do a standard two-pointer merge of the two
   already-sorted inputs into a new list `nums3`.
2. Walk `i` over nums1 and `j` over nums2 together; at each step append the
   smaller of nums1[i] / nums2[j] and advance that pointer. This keeps nums3
   sorted as it grows.
3. Once one array is exhausted, drain the leftover tail of the other array
   into nums3 (it is already sorted, so just copy it over).
4. Now nums3 is the full sorted merge. Scan it and return the element whose
   1-indexed position equals k (i.e. index k-1).
TC -> O(m + n), SC -> O(m + n)  (extra list of size m+n)

#Better Approach:
1. Building the whole merged array wastes space — we only care about the
   k-th element, so we never need to store anything. Run the same two-pointer
   merge but instead of appending, just remember the last value we "would
   have placed" in `ans` and count how many elements we have placed so far.
2. On each iteration pick the smaller current element (or, when one array is
   used up, take from the other), overwrite `ans`, and advance that pointer.
   The l-th iteration (0-indexed) settles the (l+1)-th smallest element.
3. Stop the moment we have placed k elements (l+1 == k); `ans` then holds the
   k-th smallest. This drops the O(m+n) space to O(1). The loop is bounded by
   `range(total)` so l can reach total-1 — i.e. l+1 can reach any valid k
   (1 .. m+n), not just the middle — and the break fires exactly at the k-th.
TC -> O(k), SC -> O(1)

#Optimal Approach:
1. We never actually need to walk k steps. Reframe it: the k-th element is the
   largest value in the "left half" once the merged array is split so that
   exactly k elements sit on the left. So we only need to decide how many of
   those k come from nums1 (call it mid1); the rest, mid2 = k - mid1, come
   from nums2.
2. Binary search over mid1 to find that split. Always search on the smaller
   array (swap via recursion if n1 > n2) so the search space stays
   O(log(min(m,n))).
3. mid1 can't be arbitrary: at least max(0, k - n2) elements must come from
   nums1 (nums2 can supply at most n2), and at most min(n1, k). These are the
   binary-search bounds `low`/`high`.
4. For a candidate split, look at the 4 boundary elements: l1/l2 = last
   element taken from nums1/nums2 (or -inf if none), r1/r2 = first element NOT
   taken (or +inf if the array is used up).
5. A split is valid when both left maxima fit under the other side's right
   minimum: l1 <= r2 and l2 <= r1. When valid, every left element is <= every
   right element, so the k-th smallest is max(l1, l2) — return it.
6. If l1 > r2, we took too many from nums1 → move high = mid1 - 1. If l2 > r1,
   we took too few → move low = mid1 + 1. Repeat until a valid split is found.
TC -> O(log(min(m, n))), SC -> O(1)

#KEY INSIGHT:
- The k-th element is just the max of the left partition when the merged array
  is cut so exactly k elements lie on the left. Binary-searching how many of
  those k come from the smaller array turns an O(k) walk into O(log(min(m,n))),
  checked purely via the four boundary values around each candidate cut.
"""

import math
from typing import List


class Solution:
    def kth_element_of_two_sorted_arrays_brute(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> int:
        nums3 = []
        ans = -1

        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1

        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1

        for i in range(0, len(nums3)):
            if i + 1 == k:
                ans = nums3[i]
                break

        return ans

    def kth_element_of_two_sorted_arrays_better(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> int:
        ans = -1
        i, j = 0, 0
        total = len(nums1) + len(nums2)

        for l in range(total):
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    ans = nums1[i]
                    i += 1
                else:
                    ans = nums2[j]
                    j += 1

            elif i < len(nums1):
                ans = nums1[i]
                i += 1

            else:
                ans = nums2[j]
                j += 1

            if l + 1 == k:
                break

        return ans

    def kth_element_of_two_sorted_arrays_optimal(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> int:
        ans = -1
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            ans = self.kth_element_of_two_sorted_arrays_optimal(nums2, nums1, k)
        else:
            total = k
            low, high = max(0, k - n2), min(n1, k)
            while low <= high:
                mid1 = low + (high - low) // 2
                mid2 = total - mid1
                l1 = nums1[mid1 - 1] if mid1 > 0 else -math.inf
                l2 = nums2[mid2 - 1] if mid2 > 0 else -math.inf
                r1 = nums1[mid1] if mid1 < n1 else math.inf
                r2 = nums2[mid2] if mid2 < n2 else math.inf
                if l1 <= r2 and l2 <= r1:
                    ans = max(l1, l2)
                    break
                if l1 > r2:
                    high = mid1 - 1
                elif l2 > r1:
                    low = mid1 + 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print(sol.kth_element_of_two_sorted_arrays_brute(a, b, k))
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print(sol.kth_element_of_two_sorted_arrays_better(a, b, k))
    a = [2, 3, 6, 7, 9]
    b = [1, 4, 8, 10]
    k = 5
    print(sol.kth_element_of_two_sorted_arrays_optimal(a, b, k))
