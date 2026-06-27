# QUESTION: Inversion of Array (Pre-req: Merge Sort)
# Given an array of N integers, count the number of inversions in the array
# (typically solved using merge sort). An inversion is defined as a pair
# (i, j) such that i < j and arr[i] > arr[j].
#
# Examples:
# Example 1:
# Input: N = 5, array[] = {1, 2, 3, 4, 5}
# Output: 0
# Explanation: A sorted array has 0 inversions.
#
# Example 2:
# Input: N = 5, array[] = {5, 4, 3, 2, 1}
# Output: 10
# Explanation: A reverse-sorted array has the maximum possible inversions:
# n*(n-1)/2. For n=5, that's 4 + 3 + 2 + 1 = 10.
#
# Example 3:
# Input: N = 5, array[] = {5, 3, 2, 1, 4}
# Output: 7
# Explanation: The 7 inversion pairs are: (5,3), (5,2), (5,1), (5,4),
# (3,2), (3,1), (2,1). The pairs (2,4) and (1,4) do not qualify because
# they are in correct order.
#
# Constraints:
# 1 <= N <= 10^5
# 1 <= arr[i] <= 10^9


"""
#Brute Force:
1. An inversion is any pair (i, j) with i < j and nums[i] > nums[j], so the most
   direct method is to literally examine every such ordered pair.
2. Fix a left index i, then let j run over every position to its right
   (j from i+1 to end). This guarantees i < j for every pair considered, exactly
   once each.
3. For each pair, if nums[i] > nums[j] the order is "wrong", so it's an inversion
   — increment the counter cnt.
4. After all pairs are checked, cnt is the total inversion count. Two nested
   loops over n elements give n*(n-1)/2 comparisons, hence quadratic.
TC -> O(n^2), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier exists. The problem goes straight from the
O(n^2) brute-force pair scan to the O(n log n) merge-sort-based count; there is no
sensible approach in between.

#Optimal Approach (count DURING Merge Sort's merge):
WHY MERGE SORT HELPS (the reusable intuition):
- Brute force is O(n^2) because for every left element it rescans all elements to
  its right. If both halves were SORTED, we could count matches with a single
  forward sweep instead of a rescan — and merge sort hands us sorted halves for
  free, since it sorts every sub-range as it goes.
- A pair (i, j) needs i < j. When we merge [low..mid] with [mid+1..high], every
  left-half index is < every right-half index by construction, so counting
  cross-half pairs at each merge and summing over all merges covers every pair
  exactly once.

THE DETAIL THAT'S EASY TO FORGET:
- Inversion's condition is nums[i] > nums[j] — the SAME comparison merge already
  uses to order elements. Because they're identical, the count can ride ALONG
  INSIDE the merge: the moment merge picks a right element over a left one, that's
  exactly an inversion. (Contrast: Reverse Pairs uses nums[i] > 2*nums[j], a
  DIFFERENT threshold, so it must count in a separate pass before merging — see
  reversePairs.py.)
- The "count all remaining left elements at once" shortcut — and why it differs
  from Reverse Pairs: here, the instant we hit nums[right] < nums[left], we don't
  test the rest of the left half one by one. Since the left half is sorted
  ascending, nums[left] and EVERY element after it up to mid are all >= nums[left]
  and therefore all > nums[right] too — so every one of them forms an inversion
  with this right element. We add the whole tail (mid - left + 1) in a single
  step. Reverse Pairs can't take this shortcut because its condition (2*nums[j])
  isn't the comparison the merge makes; there we instead loop over the left half
  and, for each left element, separately accumulate how many right elements satisfy
  the threshold (see reversePairs.py).

DRY RUN — counting one merge step with two SORTED halves (full arr below):

  arr1 (left)  = | 2 | 3 | 4 | 5 |
  arr2 (right) = | 0 | 1 | 6 | 7 |

  Merge with pointers left -> arr1[i], right -> arr2[j]; append the smaller, and
  when a RIGHT value is the smaller one, every remaining left element is > it.

  * left=2 vs right=0 : 0 < 2, and arr1 is sorted so 0 < ALL of [2,3,4,5].
                          | 2 | 3 | 4 | 5 |
                            ^ left            -> +4 in one shot (cnt=4)
                        take 0, advance right.
  * left=2 vs right=1 : 1 < 2, so again 1 < ALL of [2,3,4,5] -> +4 (cnt=8)
                        take 1, advance right.
  * left=2 vs right=6 : 2 <= 6, no inversion; from here 2,3,4,5 all drain out
                        (each <= 6 / 7), adding nothing more.
  This merge adds +8.

- Whole array arr = [5, 3, 2, 4, 1, 6, 0, 7] (total inversions = 14): the smaller
  merges lower in the recursion contribute [5]|[3] +1, [3,5]|[2,4] +3, [1,6]|[0,7]
  +2 = 6, and the top merge above adds 8, giving 6 + 8 = 14 (matches brute force).
- The lesson: at "0 < 2" we added 4 at once instead of comparing 0 against 2, 3, 4
  and 5 one by one — that batch (mid - left + 1) is the whole O(n^2) -> O(n log n)
  win, and it works ONLY because the count condition is the SAME comparison the
  merge already makes (contrast Reverse Pairs, which needs a per-element pass).

STEPS:
1. merge_sort(low, high): split at mid, recurse on both halves (they come back
   sorted and with their internal inversion counts), then merge while counting the
   cross-half inversions. Total = left-count + right-count + cross-count.
2. In merge(): two pointers, left (from low) and right (from mid+1); append the
   smaller value to a temp buffer so the merged range stays sorted.
3. The counting trick: if nums[left] <= nums[right] there's no inversion — take the
   left value. But if nums[right] < nums[left], then nums[right] is smaller than
   nums[left] AND than EVERY remaining left element (left half is sorted), so all
   (mid - left + 1) of them form an inversion with it — add that batch at once.
4. Once a half is exhausted, copy the leftover of the other half into temp, then
   write temp back into nums[low..high] so the range is sorted for the parent.
5. Each cross-half pair is counted exactly once — at the level where its two
   elements first land in opposite halves. Both pointers sweep each half once, so
   it's O(n) per merge level, O(n log n) overall with an O(n) temp buffer.
   NOTE: like any merge sort this sorts nums in place as a side effect, so the
   caller's array order is modified.
TC -> O(n log n), SC -> O(n)

#KEY INSIGHT:
- The merge step already compares the two sorted halves, and inversion's condition
  IS that same comparison — so counting is free: when a right-half element is taken
  before the remaining left-half elements, all (mid - left + 1) of those left
  elements exceed it, a batch counted in O(1). The reason this fold-in works here
  but NOT for Reverse Pairs: there the counting threshold (2*nums[j]) differs from
  the merge's ordering rule, forcing a separate counting pass. Both end O(n log n)
  because a sorted half lets a pointer advance monotonically without backtracking.
"""

from typing import List


class Solution:
    def inversion_of_array_pre_req_merge_sort_brute(self, nums: List[int]) -> int:
        cnt = 0

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > nums[j]:
                    cnt += 1

        return cnt

    def inversion_of_array_pre_req_merge_sort_better(self) -> None:
        # SKIP: no tier between O(n^2) pair scan and O(n log n) merge-sort count
        pass

    def merge(self, nums: List[int], low: int, mid: int, high: int) -> int:
        temp = []
        cnt = 0
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                cnt += mid - left + 1
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]

        return cnt

    def merge_sort(self, nums: List[int], low: int, high: int) -> int:
        cnt = 0
        if low < high:
            mid = (low + high) // 2
            cnt += self.merge_sort(nums, low, mid)
            cnt += self.merge_sort(nums, mid + 1, high)
            cnt += self.merge(nums, low, mid, high)
        return cnt

    def inversion_of_array_pre_req_merge_sort_optimal(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [5, 3, 2, 1, 4]
    print(sol.inversion_of_array_pre_req_merge_sort_brute(nums))
    nums = [5, 3, 2, 1, 4]
    print(sol.inversion_of_array_pre_req_merge_sort_optimal(nums))
