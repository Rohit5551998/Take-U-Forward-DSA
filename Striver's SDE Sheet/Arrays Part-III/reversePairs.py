# QUESTION: Reverse Pairs
# Given an array of numbers, you need to return the count of reverse pairs. Reverse Pairs are those pairs where i < j and arr[i]>2*arr[j].
#
# Examples:
# Example 1:
# Input: N = 5, array[] = {1,3,2,3,1)
# Output: 2
# Explanation: The pairs are (3, 1) and (3, 1) as from both the pairs the condition arr[i] > 2*arr[j] is satisfied.
#
# Example 2:
# Input: N = 4, array[] = {3,2,1,4}
# Output: 1
# Explaination: There is only 1 pair ( 3 , 1 ) that satisfy the condition arr[i] > 2*arr[j]


"""
#Brute Force:
1. A reverse pair is an ordered pair (i, j) with i < j and nums[i] > 2*nums[j].
   The direct method is to test every such pair explicitly.
2. Fix a left index i, then let j run over every position to its right
   (j from i+1 to end), which enforces i < j exactly once per pair.
3. For each pair check the condition nums[i] > 2*nums[j]; if it holds, the pair
   is a reverse pair, so increment cnt. (Use 2*nums[j] rather than dividing to
   stay in integer arithmetic and avoid rounding.)
4. After all pairs are examined, cnt is the total. Two nested loops over n
   elements give n*(n-1)/2 comparisons, hence quadratic.
TC -> O(n^2), SC -> O(1)

#Better Approach:
SKIPPED — no distinct middle tier exists. Reverse Pairs goes straight from the
O(n^2) brute-force pair scan to the O(n log n) merge-sort-based count; there is no
sensible approach in between.

#Optimal Approach (count BEFORE Merge Sort's merge):
WHY MERGE SORT HELPS (the reusable intuition):
- Brute force is O(n^2) because for every left element it rescans all right
  elements. If both halves were SORTED, we could count matches with a single
  forward sweep instead of a rescan — that's the speedup merge sort hands us for
  free, since merge sort leaves every sub-range sorted after it processes it.
- For a pair (i, j) with i < j we only care that i sits to the LEFT of j. In merge
  sort, whenever we merge [low..mid] with [mid+1..high], every left-half index is
  < every right-half index by construction. So counting cross-half pairs at each
  merge, then summing over all merges, covers every pair exactly once.

THE CATCH THAT'S EASY TO FORGET:
- Reverse Pairs' condition is nums[i] > 2*nums[j], which is NOT the same as the
  comparison merge uses to order elements (nums[i] <= nums[j]). Because the
  thresholds differ (2*nums[j] vs nums[j]), you CANNOT count while merging — the
  merge would advance pointers by the wrong rule. So we count in a SEPARATE pass
  first, then merge normally. (Contrast: plain inversion count uses the very same
  comparison as the merge, so there it can be folded into the merge — see
  inversionOfArrayPreReqMergeSort.py.)
- How the counting differs in practice — and why: in plain inversion, the moment
  one right element is smaller, ALL remaining left elements (from the current left
  pointer to the end of the left half) count at once, because that single merge
  comparison settles them together. Here we can't lean on the merge comparison, so
  we must check the 2*nums[j] condition EXPLICITLY: we loop over each left-half
  element and maintain a right pointer marking how many right-half elements satisfy
  nums[left] > 2*nums[right]. For each individual left element we add that running
  count separately — there is no "whole tail at once" shortcut, the tally is built
  up per left element via its own forward-moving right boundary.

DRY RUN — counting one merge step with two SORTED halves:

  arr1 (left)  = | 6 | 13 | 21 | 25 |
  arr2 (right) = | 1 | 2 | 3 | 4 | 4 | 5 | 9 | 11 | 13 |

  We sweep each left element and push a single right pointer forward (it NEVER
  resets), counting how many arr2 values satisfy  arr1[i] > 2 * arr2[j].

  * left = 6 : advance right while 6 > 2*arr2[j].
                 6 > 2*1=2 yes -> 6 > 2*2=4 yes -> 6 > 2*3=6 NO (stop).
               | 1 | 2 | 3 | ...      checking ends here, because 6 = 2*3.
                         ^ right
               2 values (1, 2) qualify  -> +2

  * left = 13: continue right from where it stopped (value 3); do NOT restart.
                 13 > 6,8,8,10 all yes -> 13 > 2*9=18 NO (stop).
               | 1 2 3 4 4 5 | 9 | ...
                             ^ right
               6 values qualify  -> +6   (running 8)

  * left = 21: 21 > 2*9=18 yes -> 21 > 2*11=22 NO (stop). 7 qualify -> +7 (run 15)
  * left = 25: 25 > 2*11=22 yes -> 25 > 2*13=26 NO (stop). 8 qualify -> +8 (run 23)

  This single merge contributes 23 reverse pairs. Each left element adds its OWN
  count; the right pointer's forward-only motion is what keeps the whole sweep
  O(n) instead of O(n^2).

- WHY the pointer never resets: arr1 is sorted, so a larger left value can only
  satisfy MORE right elements than the previous one — the boundary moves right and
  never back. THIS is the contrast with inversion: there, one comparison settles
  the whole remaining left tail at once; here we must extend the right boundary
  explicitly per left element because the threshold is 2*arr2[j], not arr2[j].

STEPS:
1. merge_sort(low, high): recurse left and right (both ranges become sorted), then
   add count_reverse_pairs(low, mid, high) for the cross-half pairs, then merge to
   keep the whole range sorted for the parent. Sum = left + right + cross.
2. count_reverse_pairs: both halves are already sorted. Use two pointers — left
   over [low..mid], right starting at mid+1.
3. For each left element, advance right while nums[left] > 2*nums[right]. Since the
   right half is sorted ascending, once nums[right] is too big to satisfy it, all
   later right elements are too big as well — so we never move right backward.
4. After the while stops, (right - (mid+1)) right-half elements satisfied the
   condition for THIS left element; add that to cnt.
5. The pointer monotonicity is the trick: as left increases nums[left] grows (left
   half sorted), so the valid right boundary only moves forward — both pointers
   sweep each half at most once, giving O(n) per merge level.
6. merge() then does an ordinary merge (no counting) so parent ranges stay sorted.
   NOTE: sorts nums in place as a side effect, like any merge sort.
TC -> O(n log n), SC -> O(n)

#KEY INSIGHT:
- Sort the two halves, then count with a forward-only two-pointer sweep instead of
  a rescan. The condition nums[i] > 2*nums[j] differs from merge's ordering
  comparison, so counting must happen in its OWN pass BEFORE merging — this is the
  one detail that separates Reverse Pairs from a plain inversion count (where the
  count rides along inside the merge). Both reach O(n log n) because a sorted half
  lets one pointer advance monotonically and never backtrack.
"""

from typing import List


class Solution:
    def reverse_pairs_brute(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] > 2 * nums[j]:
                    cnt += 1
        return cnt

    def reverse_pairs_better(self) -> None:
        # SKIP: no tier between O(n^2) pair scan and O(n log n) merge-sort count
        pass

    def count_reverse_pairs(self, nums: List[int], low: int, mid: int, high: int) -> int:
        cnt = 0
        right = mid + 1
        """
        Both halves are sorted. Sweep each left-half element and keep ONE shared
        right pointer that only moves forward (never resets). For a given left
        value, advance right while left > 2*nums[right]; everything it passed
        satisfies the condition, so add (right - (mid+1)) to cnt.
        The pointer can carry over because the left half is sorted ascending: a
        larger left value still satisfies the condition for every right element the
        previous (smaller) left value already accepted, so we only ever extend the
        boundary rightward — giving an O(n) sweep instead of O(n^2).
        """
        for left in range(low, mid + 1):
            while right <= high and nums[left] > 2 * nums[right]:
                right += 1
            cnt += right - (mid + 1)

        return cnt

    def merge(self, nums: List[int], low: int, mid: int, high: int) -> None:
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left <= mid:
            temp.append(nums[left])
            left += 1

        while right <= high:
            temp.append(nums[right])
            right += 1

        for i in range(low, high + 1):
            nums[i] = temp[i - low]

        return

    def merge_sort(self, nums: List[int], low: int, high: int) -> int:
        cnt = 0
        if low < high:
            mid = (low + high) // 2
            cnt += self.merge_sort(nums, low, mid)
            cnt += self.merge_sort(nums, mid + 1, high)
            cnt += self.count_reverse_pairs(nums, low, mid, high)
            self.merge(nums, low, mid, high)
        return cnt

    def reverse_pairs_optimal(self, nums: List[int]) -> int:
        return self.merge_sort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, 2, 3, 1]
    print(sol.reverse_pairs_brute(nums))
    nums = [1, 3, 2, 3, 1]
    print(sol.reverse_pairs_optimal(nums))
