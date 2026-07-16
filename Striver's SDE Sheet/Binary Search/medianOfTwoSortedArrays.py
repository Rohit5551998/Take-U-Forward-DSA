# QUESTION: Median of 2 sorted arrays
# Given two sorted arrays arr1 and arr2 of size m and n respectively,
# return the median of the two sorted arrays. The median is defined as
# the middle value of a sorted list of numbers. If the total length of
# the combined sorted list (m + n) is even, the median is the average of
# the two middle values.
#
# Examples:
# Example 1:
# Input: arr1 = [1, 3], arr2 = [2]
# Output: 2.0
# Explanation: Merged sorted array = [1, 2, 3]. Median is 2.
#
# Example 2:
# Input: arr1 = [1, 2], arr2 = [3, 4]
# Output: 2.5
# Explanation: Merged sorted array = [1, 2, 3, 4]. Median = (2 + 3) / 2 = 2.5.
#
# Constraints:
# 0 <= m, n <= 1000, 1 <= m + n <= 2000
# -10^6 <= arr1[i], arr2[i] <= 10^6
#
# Follow up: The naive merge is O(m+n). Can you achieve O(log(min(m, n)))?


"""
#Brute Force:
1. The median is defined on the fully merged sorted array, so just build it.
   Two-pointer merge nums1 and nums2 into a new list `nums3`: at each step
   append the smaller of the two current heads and advance that pointer,
   keeping nums3 sorted as it grows.
2. Once one array runs out, drain the remaining tail of the other (already
   sorted) into nums3.
3. With the full merge in hand, read the median by index: if the total length
   is even, average the two middle elements at (n-1)//2 and n//2; if odd, take
   the single middle element at (n-1)//2.
TC -> O(m + n), SC -> O(m + n)  (extra merged list)

#Better Approach:
1. We never need the whole merged array — only the middle one or two elements.
   So run the same two-pointer merge but store nothing; just track the current
   element (`prev1`) and the one before it (`prev2`) as we go.
2. We only need to advance up to the middle index. Loop `total//2 + 1` times:
   before each pick, shift prev1 into prev2 (so prev2 always trails prev1 by
   one), then pick the smaller head (or drain from whichever array still has
   elements) into prev1 and advance that pointer.
3. After the loop, prev1 sits at index total//2 and prev2 at total//2 - 1. If
   total is even the median is the average of the two middle values
   (prev1 + prev2)/2; if odd it is prev1 alone. This keeps time similar to
   brute but drops the space to O(1).
TC -> O(m + n), SC -> O(1)

#Optimal Approach:
1. Reframe the median as a partition: cut the conceptually-merged array so the
   left half holds exactly (m+n+1)//2 elements. Then the median is decided by
   just the boundary elements around that cut — no merging needed.
2. We only choose how many of those left-half elements come from nums1 (mid1);
   the rest, mid2 = total - mid1, come from nums2. Binary search over mid1.
   Always search the smaller array (recurse with args swapped if n1 > n2) so
   the range is O(log(min(m,n))).
3. Search bounds are low=0, high=n1 (mid1 can range across all of the smaller
   array). For each candidate, compute the 4 boundary values: l1/l2 = last
   element on the left from nums1/nums2 (or -inf if none), r1/r2 = first
   element on the right (or +inf if that side is exhausted).
4. The cut is valid when both left maxima fit under the opposite right minima:
   l1 <= r2 and l2 <= r1. That guarantees every left element <= every right
   element, i.e. a correct split of the sorted order.
5. On a valid cut: if m+n is even the median straddles the cut, so average the
   two inner values (max(l1,l2) + min(r1,r2)) / 2; if odd the left half has the
   extra element, so the median is max(l1, l2).
6. Otherwise rebalance: if l1 > r2 we pulled too many from nums1 → high =
   mid1 - 1; if l2 > r1 we pulled too few → low = mid1 + 1. Repeat.
TC -> O(log(min(m, n))), SC -> O(1)

#KEY INSIGHT:
- The median only depends on the two elements straddling the point that splits
  the merged array into equal halves. Binary-searching how many left-half
  elements come from the smaller array finds that split in O(log(min(m,n)))
  using only the four boundary values (l1, l2, r1, r2) — never merging.
"""

import math
from typing import List


class Solution:
    def median_of_two_sorted_arrays_brute(self, nums1: List[int], nums2: List[int]) -> float:
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
        if len(nums3) % 2 == 0:
            ans = (nums3[(len(nums3) - 1) // 2] + nums3[len(nums3) // 2]) / 2
        else:
            ans = nums3[(len(nums3) - 1) // 2]
        return ans

    def median_of_two_sorted_arrays_better(self, nums1: List[int], nums2: List[int]) -> float:
        ans = -1

        i, j = 0, 0
        total = len(nums1) + len(nums2)
        prev1 = prev2 = 0

        for _ in range(total // 2 + 1):
            prev2 = prev1

            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    prev1 = nums1[i]
                    i += 1
                else:
                    prev1 = nums2[j]
                    j += 1

            elif i < len(nums1):
                prev1 = nums1[i]
                i += 1

            else:
                prev1 = nums2[j]
                j += 1

        if total % 2 == 0:
            ans = (prev1 + prev2) / 2
        else:
            ans = prev1

        return ans

    def median_of_two_sorted_arrays_optimal(self, nums1: List[int], nums2: List[int]) -> float:
        ans = -1
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            ans = self.median_of_two_sorted_arrays_optimal(nums2, nums1)
        else:
            total = (n1 + n2 + 1) // 2
            low, high = 0, n1
            while low <= high:
                mid1 = low + (high - low) // 2
                mid2 = total - mid1
                l1 = nums1[mid1 - 1] if mid1 > 0 else -math.inf
                l2 = nums2[mid2 - 1] if mid2 > 0 else -math.inf
                r1 = nums1[mid1] if mid1 < len(nums1) else math.inf
                r2 = nums2[mid2] if mid2 < len(nums2) else math.inf

                if l1 <= r2 and l2 <= r1:
                    if (n1 + n2) % 2 == 0:
                        ans = (max(l1, l2) + min(r1, r2)) / 2
                    else:
                        ans = max(l1, l2)
                    break

                if l1 > r2:
                    high = mid1 - 1

                elif l2 > r1:
                    low = mid1 + 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2, 4]
    print(sol.median_of_two_sorted_arrays_brute(nums1, nums2))
    nums1 = [1, 3]
    nums2 = [2, 4]
    print(sol.median_of_two_sorted_arrays_better(nums1, nums2))
    nums1 = [1, 3]
    nums2 = [2]
    print(sol.median_of_two_sorted_arrays_optimal(nums1, nums2))
