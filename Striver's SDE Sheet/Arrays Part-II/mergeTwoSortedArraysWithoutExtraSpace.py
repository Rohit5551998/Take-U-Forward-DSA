# QUESTION: Merge two sorted arrays without extra space
# Given two sorted integer arrays nums1 (of size m + n, with the last n
# slots set to 0) and nums2 (of size n), merge both arrays into a single
# array sorted in non-decreasing order. The final sorted array should be
# stored inside the array nums1 and you should not use any extra space.
#
# Examples:
# Input : nums1 = [-5, -2, 4, 5, 0, 0, 0], nums2 = [-3, 1, 8]
# Output : [-5, -3, -2, 1, 4, 5, 8]
# Explanation : The merged array is: [-5, -3, -2, 1, 4, 5, 8], where [-5, -2, 4, 5] are from nums1 and [-3, 1, 8] are from nums2
#
# Input : nums1 = [0, 2, 7, 8, 0, 0, 0], nums2 = [-7, -3, -1]
# Output : [-7, -3, -1, 0, 2, 7, 8]
# Explanation : The merged array is: [-7, -3, -1, 0, 2, 7, 8], where [0, 2, 7, 8] are from nums1 and [-7, -3, -1] are from nums2


"""
(This file holds four approaches with two different I/O contracts. The first
three treat nums1 (size m) and nums2 (size n) as two separate arrays and return
both, merged across the boundary. The last one is the LeetCode-88 variant: nums1
has size m+n with its last n slots = 0, and the merge is done in place into nums1.)

#Brute Force — merge into a third array:  ..._brute
1. Classic two-pointer merge: walk i over nums1 and j over nums2, and at each
   step copy the smaller of nums1[i]/nums2[j] into a fresh array nums3 of size
   m+n (position i+j tracks how many we've placed). Drain whichever array is
   left over afterward.
2. Then copy nums3 back: the first m values overwrite nums1, the rest overwrite
   nums2. Correct and simple, but it uses a whole extra array — exactly what the
   problem forbids, so it's only the baseline.
TC -> O(m+n), SC -> O(m+n)

#Optimal Variant I — fix the boundary, then re-sort each half:  ..._optimal_variant_i
1. Target invariant: in a correct merge, every value in nums1 must be <= every
   value in nums2 (nums1 holds the smaller half, nums2 the larger half).
2. Where it can be wrong: since both arrays are already individually sorted, the
   ONLY place the invariant breaks is the seam — the largest values of nums1
   (its right end) and the smallest values of nums2 (its left end).
3. So compare across the seam with two pointers: `left = m-1` (end of nums1) and
   `right = 0` (start of nums2).
4. If nums1[left] > nums2[right] they are on the wrong sides, so swap them: the
   big value goes into nums2, the small value comes into nums1.
5. After a swap, step inward — `left -= 1`, `right += 1` — to check the next pair
   along the seam.
6. Stop as soon as nums1[left] <= nums2[right]: every value still in nums1 is now
   <= every value in nums2, so no later pair can be out of order — the partition
   between the two arrays is correct.
7. The swaps placed the right *set* of values in each array but may have left them
   unordered, so finish with `nums1.sort()` and `nums2.sort()`.
8. Caveat: `nums1[0:m]` makes an O(m) slice copy, so this isn't strictly O(1)
   auxiliary space, and it returns the two arrays separately (not one merged one).
TC -> O((m+n) log(m+n)), SC -> O(1) aux (besides the O(m) slice)

#Optimal Variant II — gap method (shell-sort shrinking gap), O(1) space:  ..._optimal_variant_ii
1. Goal: get a fully merged order across BOTH arrays using zero extra space. The
   idea is to run shell sort's shrinking-gap pass, but over the two arrays glued
   together rather than allocating a combined array.
2. Virtual indexing: pretend nums1 ++ nums2 is one array of length m+n. A virtual
   index i < m lives in nums1[i]; an index i >= m lives in nums2[i-m]. This lets a
   single index space address both arrays without ever joining them in memory.
3. Helper: swapIfGreater(a, i, b, j) compares a[i] with b[j] and swaps them if
   a[i] > b[j] — i.e. it enforces "smaller on the left" for one pair, regardless
   of which physical array each side sits in.
4. Choose the gap: start at gap = ceil((m+n)/2). The gap is the distance between
   the two virtual indices we compare in a pass.
5. One pass: slide a pair (left, right = left+gap) from the front to the end of
   the virtual array (right < m+n), and at each position call swapIfGreater on
   that pair. Three position cases decide which physical arrays are touched:
     - left in nums1, right in nums2  -> swapIfGreater(nums1, left, nums2, right-m)  (spans the seam)
     - both in nums2                  -> swapIfGreater(nums2, left-m, nums2, right-m)
     - both in nums1                  -> swapIfGreater(nums1, left, nums1, right)
6. Shrink the gap after each pass: gap = ceil(gap/2). Keep going; once a pass with
   gap == 1 completes, every adjacent pair is ordered, so the whole thing is
   sorted and we stop.
7. Why it works / cost: comparing far-apart elements first lets a value travel a
   long distance early, so by the time the gap is 1 almost nothing is left to fix.
   There are O(log(m+n)) gap values, each pass is O(m+n) work, and nothing is ever
   allocated — so it merges in place.
TC -> O((m+n) log(m+n)), SC -> O(1)

#Optimal Variant III — in-place back-fill (nums1 padded with n zeros):  ..._optimal_variant_iii
1. This is the variant where nums1 is sized m+n with the last n slots empty (0).
   The trick is to fill nums1 FROM THE BACK so we only ever write into slots
   we've already consumed or that were empty — never clobbering an unread value.
2. Pointers: left = m-1 (last real nums1 value), right = n-1 (last nums2 value),
   and the write position is left+right+1 (the current last unfilled slot).
   Place the larger of nums1[left]/nums2[right] there and step that pointer back.
3. When nums1 is exhausted, copy any remaining nums2 values into the front; any
   leftover nums1 values are already sitting in their final positions, so they
   need no move. One back-to-front pass, no extra array.
TC -> O(m+n), SC -> O(1)

#KEY INSIGHT:
- With no extra array you either (a) fix only the seam and re-sort the two halves
  — the swap and gap methods, O((m+n) log(m+n)) — or (b) when nums1 is pre-padded
  with zeros, fill it back-to-front so writes only land on already-read/empty
  slots, giving the true O(m+n) / O(1) merge. Writing front-to-back would
  overwrite unread data; going back-to-front is what makes it safe.
"""

from typing import List, Tuple


class Solution:
    def merge_two_sorted_arrays_without_extra_space_brute(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> Tuple[List[int], List[int]]:
        nums3 = [0 for _ in range(n + m)]
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                nums3[i + j] = nums1[i]
                i += 1
            else:
                nums3[i + j] = nums2[j]
                j += 1

        while i < m:
            nums3[i + j] = nums1[i]
            i += 1

        while j < n:
            nums3[i + j] = nums2[j]
            j += 1

        for i in range(0, len(nums3)):
            if i < m:
                nums1[i] = nums3[i]
            else:
                nums2[i - m] = nums3[i]

        return nums1, nums2

    def merge_two_sorted_arrays_without_extra_space_optimal_variant_i(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> Tuple[List[int], List[int]]:
        nums1 = nums1[0:m]
        left = m - 1
        right = 0

        while left >= 0 and right < n:
            if nums1[left] > nums2[right]:
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left -= 1
                right += 1
            else:
                break

        nums1.sort()
        nums2.sort()

        return nums1, nums2

    def swapIfGreater(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if nums1[m] > nums2[n]:
            nums1[m], nums2[n] = nums2[n], nums1[m]

    def merge_two_sorted_arrays_without_extra_space_optimal_variant_ii(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> Tuple[List[int], List[int]]:
        gap = int((n + m) / 2) + int((n + m) % 2)

        while gap > 0:
            left = 0
            right = gap
            while right < m + n:
                # arr1 & arr2
                if left < m and right >= m:
                    self.swapIfGreater(nums1, left, nums2, right - m)
                # Both in arr2
                elif left >= m and right >= m:
                    self.swapIfGreater(nums2, left - m, nums2, right - m)
                # Both in arr1
                elif left < m and right < m:
                    self.swapIfGreater(nums1, left, nums1, right)
                left += 1
                right += 1

            if gap > 1:
                gap = int(gap / 2) + int((gap) % 2)
            else:
                break

        return nums1, nums2

    def merge_two_sorted_arrays_without_extra_space_optimal_variant_iii(
        self, nums1: List[int], m: int, nums2: List[int], n: int
    ) -> List[int]:
        # In place nums1 updation
        left = m - 1
        right = n - 1

        while left >= 0 and right >= 0:
            if nums1[left] >= nums2[right]:
                nums1[left + right + 1] = nums1[left]
                left -= 1
            else:
                nums1[left + right + 1] = nums2[right]
                right -= 1

        while right >= 0:
            nums1[left + right + 1] = nums2[right]
            right -= 1

        return nums1


if __name__ == "__main__":
    sol = Solution()
    arr1, arr2 = [-5, -2, 4, 5], [-3, 1, 8]
    print(sol.merge_two_sorted_arrays_without_extra_space_brute(arr1, 4, arr2, 3))
    arr1, arr2 = [-5, -2, 4, 5], [-3, 1, 8]
    print(sol.merge_two_sorted_arrays_without_extra_space_optimal_variant_i(arr1, 4, arr2, 3))
    arr1, arr2 = [-5, -2, 4, 5], [-3, 1, 8]
    print(sol.merge_two_sorted_arrays_without_extra_space_optimal_variant_ii(arr1, 4, arr2, 3))
    arr1, arr2 = [-5, -2, 4, 5, 0, 0, 0], [-3, 1, 8]
    print(sol.merge_two_sorted_arrays_without_extra_space_optimal_variant_iii(arr1, 4, arr2, 3))
