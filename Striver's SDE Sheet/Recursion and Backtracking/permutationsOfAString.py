# mypy: disable-error-code="empty-body"
# QUESTION: Permutations of a String
# Given an array arr of distinct integers, print all possible permutations of the given array.
# A permutation is an arrangement of all the elements of the array into some sequence or order.
# An array of n distinct elements has exactly n! permutations. Return the permutations in any
# order.
#
# Examples:
# Example 1:
# Input: arr = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Explanation: There are 3! = 6 permutations of the 3 distinct elements, and all of them are
# listed.
#
# Example 2:
# Input: arr = [0, 1]
# Output: [[0, 1], [1, 0]]
# Explanation: The 2 distinct elements can be arranged in 2! = 2 different ways.


"""
#Brute Force (find_permutations_brute + permutations_of_a_string_brute):
1. Opposite mental model to the optimal: instead of rearranging nums in place,
   BUILD each permutation from scratch in a separate list `comb`, one element at
   a time. The cost of that is extra bookkeeping space, which is what makes this
   the brute tier.
2. At each recursion step consider EVERY element as the next pick — loop i over
   0..n-1 (not a forward-only index; that would give combinations, not perms).
3. Keep a `visited` set of the values already sitting in `comb`. Skip any element
   already visited — this is what stops an element being reused and is the
   defining extra structure of this approach.
4. Choose: append nums[i] to comb and add it to visited, then recurse to fill the
   next position.
5. Backtrack: after the recursive call, pop nums[i] from comb and remove it from
   visited, so the next i explores a different arrangement from a clean state.
6. Base case: once len(comb) == len(nums) every position is filled, so comb is a
   full permutation — append a COPY (list(comb)) to ans, since comb keeps mutating
   as the recursion backtracks.
7. Because the input is distinct and `visited` blocks reuse, every generated
   permutation is already unique — so ans is a plain list (no set / dedup needed)
   and is returned directly.
TC -> O(n! * n), SC -> O(n) visited + O(n) comb + O(n) recursion + O(n! * n) out
   (n! permutations, each O(n) to build/copy; the O(n) aux is the brute's overhead
    over the optimal's in-place swapping)

#Better Approach:
SKIPPED — no middle tier. The known progression is map-based generation (a
separate output list + a visited/frequency array) as the brute, then the
in-place swap version below as the optimal; nothing sensible sits between them.

#Optimal Approach (find_permutations + permutations_of_a_string_optimal):
1. Goal: emit all n! orderings WITHOUT any auxiliary visited array or a separate
   builder list — mutate nums in place and swap back, so extra space is just the
   recursion stack. That in-place trick is what makes this the optimal tier.
2. `index` is the position currently being decided; nums[0..index-1] is treated
   as already settled for this branch, and we choose what lands at `index`.
3. Loop i from 0 to index: swap nums[i] with nums[index]. This rotates each of
   the candidates sitting in positions 0..index through slot `index`, so every
   element still in play gets its turn at this position across the branches.
4. Recurse with index+1 to decide the remaining positions with that choice fixed.
5. Undo the swap (swap nums[i], nums[index] back) so the array is restored and
   the next i explores a different arrangement — classic backtracking.
6. Base case: when index == len(nums) every slot is assigned, so nums is one
   complete permutation — append a COPY (list(nums)), because nums keeps mutating
   as the recursion unwinds and a reference would later be corrupted.
TC -> O(n! * n), SC -> O(n) recursion stack (aux) + O(n! * n) for the output
   (n! permutations, each costing O(n) to copy into the answer)

#KEY INSIGHT:
- In-place swapping (swap → recurse → swap back) enumerates all permutations with
  NO visited/frequency array and no separate partial-list — only O(n) recursion
  depth of extra space. That's the space win over the map-based brute approach,
  while time stays O(n! * n) since you must still produce every permutation.
"""

from typing import List


class Solution:
    def find_permutations_brute(
        self, nums: List[int], ans: List[List[int]], comb: List[int], visited: set
    ) -> None:
        if len(comb) == len(nums):
            ans.append(list(comb))

        else:
            for i in range(0, len(nums)):
                if nums[i] not in visited:
                    comb.append(nums[i])
                    visited.add(nums[i])
                    self.find_permutations_brute(nums, ans, comb, visited)
                    visited.remove(nums[i])
                    comb.pop()
        return

    def permutations_of_a_string_brute(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        comb: List[int] = []
        visited: set = set()
        self.find_permutations_brute(nums, ans, comb, visited)
        return ans

    def permutations_of_a_string_better(self, nums: List[int]) -> List[List[int]]:
        # SKIP: no middle tier — map/visited-array generation (brute) jumps
        # straight to in-place swapping (optimal); nothing sensible sits between.
        pass

    def find_permutations(self, nums: List[int], ans: List[List[int]], index: int) -> None:
        if index == len(nums):
            ans.append(list(nums))
        else:
            for i in range(0, index + 1):
                nums[i], nums[index] = nums[index], nums[i]
                self.find_permutations(nums, ans, index + 1)
                nums[i], nums[index] = nums[index], nums[i]
        return

    def permutations_of_a_string_optimal(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        self.find_permutations(nums, ans, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permutations_of_a_string_brute(nums))
    nums = [1, 2, 3]
    print(sol.permutations_of_a_string_optimal(nums))
