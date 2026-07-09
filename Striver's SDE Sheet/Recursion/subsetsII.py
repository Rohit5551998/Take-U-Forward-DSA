# mypy: disable-error-code="empty-body"
# QUESTION: Subsets II
# Given an integer array nums which may contain duplicate entries, return the power set
# (all subsets). The solution set must not contain duplicate subsets. Return the subsets
# in any order.
#
# Examples:
# Input: array[] = [1,2,2]
# Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]
# Explanation: We can have subsets ranging from length 0 to 3, which are listed above.
# Also the subset [1,2] appears twice but is printed only once as we require unique subsets.
#
# Input: array[] = [1]
# Output: [ [ ], [1] ]
# Explanation: Only two unique subsets are available.


"""
#Brute Force:
1. Generate the entire power set exactly like plain Subsets: recurse index by
   index, making a "not-pick" call and then a "pick" call, so all 2^n
   include/exclude combinations flow down to the base case.
2. Sort nums first. Duplicates only cause repeated subsets when equal *values*
   sit at different positions — e.g. in [2,1,2] the picks {0,1} and {1,2} both
   have multiset {1,2} but, unsorted, would build tuples (2,1) vs (1,2). Sorting
   forces index-order to equal value-order, so any two subsets with the same
   multiset build the identical tuple.
3. At the base case (index == len(nums)) convert the current subset list to a
   tuple and add it to a set. Tuples are hashable, so the set silently discards
   duplicate subsets (the two different ways of forming [1,2] collapse to one).
4. After recursion finishes, convert each stored tuple back to a list for the
   final answer.
TC -> O(2^n * n): 2^n leaves, each O(n) to build+hash a tuple.
SC -> O(2^n * n) for the set of subsets, plus O(n) recursion depth.

#Better Approach:
SKIPPED — no distinct middle tier. The problem goes straight from "enumerate all
2^n subsets and dedupe with a set" (brute) to "sort + skip duplicates so no set
is needed" (optimal); there is no sensible intermediate.

#Optimal Approach:
1. Sort nums so equal values sit adjacently — this is what lets us detect and
   skip duplicates by a simple neighbour comparison.
2. Model generation differently from the brute: instead of a per-element
   pick/not-pick, every recursive call *is itself* a valid subset. So the first
   line appends a copy of the current `subset` to the answer — [] is captured on
   the very first call.
3. From position `index`, loop i over the remaining elements and treat each as
   "the next element to append", recursing with start = i+1 so every element is
   used at most once down a branch.
4. Duplicate-skip: within one loop level, if i > index (i.e. not the first,
   mandatory choice at this level) and nums[i] == nums[i-1], skip it. The first
   occurrence of a value already spawned the branch that produces every subset
   starting with that value here, so a second identical value would only rebuild
   duplicates — e.g. for [1,2,2] at index after 1, picking the first 2 covers
   [2] and [2,2]; the second 2 is skipped as a starting choice.
5. Append nums[i], recurse, then pop to backtrack and try the next candidate.
TC -> O(2^n * n): up to 2^n subsets, each O(n) to copy into the answer.
SC -> O(n) recursion depth (output not counted); no dedup set required.

#KEY INSIGHT:
- Sorting + the "skip nums[i] when i > index and nums[i] == nums[i-1]" rule
  generates every unique subset exactly once, so no hash set is needed. Passing
  i+1 (not index+1) as the next start is what keeps each element used at most
  once per branch — the exact bug that, when wrong, produced impossible subsets.
"""

from typing import List


class Solution:
    def find_subsets(self, index: int, nums: List[int], subset: List[int], hashSet: set) -> None:
        if index == len(nums):
            # Leaf: store this subset as a tuple so the set can dedupe identical ones
            hashSet.add(tuple(subset))
        else:
            # Branch 1: skip nums[index]
            self.find_subsets(index + 1, nums, subset, hashSet)
            # Branch 2: pick nums[index], recurse, then backtrack
            subset.append(nums[index])
            self.find_subsets(index + 1, nums, subset, hashSet)
            subset.pop()
        return

    def subsets_ii_brute(self, nums: List[int]) -> List[List[int]]:
        hashSet: set = set()
        subset: List[int] = []
        nums.sort()
        self.find_subsets(0, nums, subset, hashSet)
        return [list(item) for item in hashSet]

    def subsets_ii_better(self, nums: List[int]) -> List[List[int]]:
        # SKIP: no distinct middle tier — the jump is directly from set-based
        # dedupe (brute) to sort + skip-duplicates recursion (optimal).
        pass

    def find_subsets_optimal(
        self, index: int, nums: List[int], subset: List[int], ans: List[List[int]]
    ) -> None:
        # Every recursive call is itself a valid subset (empty set on the first call)
        ans.append(list(subset))
        for i in range(index, len(nums)):
            # Skip a duplicate value as a starting choice: only the first occurrence
            # at this level may start a branch (i == index is always allowed)
            if i > index and nums[i - 1] == nums[i]:
                continue
            subset.append(nums[i])
            # Recurse with i+1 (not index+1) so each element is used at most once per branch
            self.find_subsets_optimal(i + 1, nums, subset, ans)
            subset.pop()

    def subsets_ii_optimal(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        subset: List[int] = []
        nums.sort()
        self.find_subsets_optimal(0, nums, subset, ans)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 2]
    print(sol.subsets_ii_brute(nums))
    nums = [1, 2, 2]
    print(sol.subsets_ii_optimal(nums))
