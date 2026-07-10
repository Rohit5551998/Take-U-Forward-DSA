# mypy: disable-error-code="empty-body"
# QUESTION: Permutation Sequence
# Given N and K, where N is the sequence of numbers from 1 to N (i.e.,
# [1, 2, 3, ..., N]), find the K-th permutation sequence (1-indexed) in
# the lexicographically sorted list of all N! permutations of [1..N].
# Return the permutation as a string.
#
# Examples:
# Example 1:
# Input: N = 3, K = 3
# Output: "213"
# Explanation: The 3! = 6 permutations of [1, 2, 3] in order are:
# "123", "132", "213", "231", "312", "321". The 3rd is "213".
#
# Example 2:
# Input: N = 4, K = 9
# Output: "2314"
#
# Constraints:
# 1 <= N <= 9
# 1 <= K <= N!


"""
#Brute Force (find_permutations + permutation_sequence_brute):
1. Naive idea: if we literally generate ALL permutations, sort them, and index in,
   we get the k-th one by definition. Correct but pays the full n! cost.
2. Build the digit pool ["1".."n"] as strings so the final join is trivial.
3. Generate every permutation via swap-based backtracking: at each position
   `index`, swap each later element into that slot, recurse on index+1, then swap
   back to restore order for the next choice.
4. When index reaches the end, one full permutation is fixed — append a copy.
5. Swap-generation does NOT produce permutations in lexicographic order, so sort
   the collected list explicitly to match the "lexicographically sorted" spec.
6. Return the (k-1)-th entry (k is 1-indexed) joined into a string.
TC -> O(n! * n) to generate + O(n! * n log(n!)) to sort, SC -> O(n! * n) to hold
   all permutations (n = N; there are n! of them, each length n)

#Better Approach:
SKIPPED — there's no middle tier. You either generate everything (brute) or use
the factorial number-system trick to jump straight to the k-th permutation
(optimal); nothing sensible sits between "all n!" and "compute it directly".

#Optimal Approach (permutation_sequence_optimal):
1. Key math: with the digits sorted, fixing the FIRST digit leaves (n-1)!
   permutations. So the first (n-1)! perms start with the smallest digit, the
   next (n-1)! with the second smallest, and so on — the block is decided by
   k // (n-1)!.
2. Work 0-indexed: decrement k by 1 so "k // fact" maps cleanly to an array index.
3. Precompute the candidate list nums = [1..n] (kept sorted) and fact = (n-1)!,
   the block size for the current leading position.
4. Pick the digit at index k // fact — that's which block k falls into — append it
   to the answer, and REMOVE it from nums (it's now used and mustn't repeat).
5. Descend one position: the chosen block has fact perms, so the offset WITHIN it
   is k % fact — set k to that. The sub-problem now has one fewer digit, so the
   new block size is fact // len(nums) (i.e. (m-1)! for the remaining m digits).
6. Repeat until nums is empty; the accumulated string is the k-th permutation.
TC -> O(n^2), SC -> O(n)
   (n positions, and nums.remove / index into nums is O(n) each → n * n)

#KEY INSIGHT:
- The factorial number system: the k-th permutation's digits are read off directly
  by repeatedly dividing k by the block size (n-1)!, (n-2)!, … Each quotient picks
  the next digit from the remaining sorted pool and each remainder becomes the k
  for the smaller sub-problem — so we never enumerate a single wasted permutation.
"""

from typing import List


class Solution:
    def find_permutations(self, nums: List[str], ans: List[List[str]], index: int) -> None:
        if index == len(nums):
            ans.append(list(nums))
            return

        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.find_permutations(nums, ans, index + 1)
            nums[i], nums[index] = nums[index], nums[i]

    def permutation_sequence_brute(self, n: int, k: int) -> str:
        nums = []
        ans = []

        # digit pool ["1".."n"] as strings so the final join is trivial
        for i in range(1, n + 1):
            nums.append(str(i))

        # generate every permutation, then sort into lexicographic order
        # (swap-based generation is NOT lexicographic on its own)
        self.find_permutations(nums, ans, 0)
        ans.sort()

        # k is 1-indexed, so the k-th permutation lives at index k-1
        return "".join(ans[k - 1])

    def permutation_sequence_better(self, n: int, k: int) -> str:
        # SKIP: no middle tier — either enumerate all n! (brute) or jump straight
        # to the k-th via the factorial number system (optimal); nothing between.
        pass

    def permutation_sequence_optimal(self, n: int, k: int) -> str:
        nums = []
        fact = 1
        ans = ""

        # build sorted pool [1..n]; fact ends as (n-1)! = block size for pos 0
        # (each choice of the leading digit fixes (n-1)! permutations)
        for i in range(1, n):
            nums.append(i)
            fact *= i
        nums.append(n)

        # work 0-indexed so k // fact maps directly to an array index
        k -= 1

        # k // fact = which block (which leading digit); append it and drop it
        # from the pool. Then k % fact is the offset inside that block (the k for
        # the smaller sub-problem), and fact // len(nums) shrinks the block size
        # from (m-1)! to (m-2)! as one digit is consumed.
        while True:
            value = nums[(k // fact)]
            ans += str(value)
            nums.remove(value)
            if len(nums) == 0:
                break
            k = k % fact
            fact //= len(nums)

        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 3
    k = 3
    print(sol.permutation_sequence_brute(n, k))
    n = 3
    k = 3
    print(sol.permutation_sequence_optimal(n, k))
