# mypy: disable-error-code="empty-body"
# QUESTION: Combination Sum
# Given an array of distinct integers `candidates` and a target integer
# `target`, return a list of all unique combinations of `candidates`
# where the chosen numbers sum to `target`. You may return the
# combinations in any order.
# The SAME number may be chosen from `candidates` an UNLIMITED number of
# times. Two combinations are unique if the frequency of at least one of
# the chosen numbers is different.
# The test cases are generated such that the number of unique
# combinations that sum up to `target` is less than 150 combinations.
#
# Examples:
# Example 1:
# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]
# Explanation: 2 + 2 + 3 = 7. 7 is itself a candidate.
#
# Example 2:
# Input: candidates = [2, 3, 5], target = 8
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
#
# Example 3:
# Input: candidates = [2], target = 1
# Output: []
#
# Constraints:
# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
#
# Examples:
# Example 1:
# Input: array = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
#  7 is a candidate, and 7 = 7.
#  These are the only two combinations.
#
# Example 2:
# Input: array = [2], target = 1
# Output: []
# Explaination: No combination is possible.


"""
#Brute Force:
SKIPPED — there is no polynomial / non-recursive way to enumerate every
combination that sums to target. Any correct solution must explore the
decision space, so the recursion IS the baseline; there's no cruder tier.

#Better Approach:
SKIPPED — no intermediate approach exists between "try every combination"
and the pick/not-pick recursion below. Sorting only enables an early cut-off,
it doesn't change the algorithm class, so brute == optimal here.

#Optimal Approach (find_combinations + combination_sum_optimal):
1. Sort candidates ascending. This isn't for correctness — it lets us stop
   early: once candidates[index] > current target, every later candidate is
   also too big, so that whole branch is dead and we can just return.
2. Recurse over an `index` pointer with a "pick / don't-pick" choice at each
   step, carrying the running `combination` and the remaining `target`.
3. Success case: if target has been driven down to exactly 0, we've found a
   valid combination — append a COPY (list(combination)) to ans, because the
   working list keeps mutating as recursion unwinds.
4. Pick branch: if candidates[index] <= target (i.e. target - cand >= 0),
   append candidates[index] and recurse WITHOUT advancing index. Staying on
   the same index is what allows the same number to be reused unlimited times.
5. Backtrack: pop the number we just tried so the list is clean for the next
   choice.
6. Don't-pick branch: recurse with index+1 and the SAME target, permanently
   dropping candidates[index] from consideration. This is what generates the
   distinct combinations that don't use the current number.
7. The elif guard doubles as the sorted early-exit: when candidates[index]
   exceeds target neither branch runs, pruning all larger candidates at once.
TC -> O(2^t * k), SC -> O(k * x) + O(t/min) recursion stack
  (t = target, k = avg combination length, x = number of combinations)

#KEY INSIGHT:
- The "reuse a number unlimited times" rule is captured by recursing on the
  SAME index in the pick branch (instead of index+1). Advancing the index
  only happens in the not-pick branch, which is what keeps combinations
  unique and prevents infinite loops.
"""

from typing import List


class Solution:
    def combination_sum_brute(self, candidates: List[int], target: int) -> List[List[int]]:
        # SKIP: no non-recursive baseline exists — enumerating combinations that
        # sum to target inherently requires exploring the decision space.
        pass

    def combination_sum_better(self, candidates: List[int], target: int) -> List[List[int]]:
        # SKIP: no intermediate tier between brute and optimal; sorting only adds
        # an early cut-off, it doesn't change the algorithm class.
        pass

    def find_combinations(
        self,
        candidates: List[int],
        target: int,
        ans: List[List[int]],
        combination: List[int],
        index: int,
    ) -> None:
        if index < len(candidates):
            if target == 0:
                ans.append(list(combination))

            elif target - candidates[index] >= 0:
                combination.append(candidates[index])
                self.find_combinations(
                    candidates, target - candidates[index], ans, combination, index
                )
                combination.pop()
                self.find_combinations(candidates, target, ans, combination, index + 1)
        return

    def combination_sum_optimal(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = []
        candidates.sort()
        self.find_combinations(candidates, target, ans, combination, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(sol.combination_sum_optimal(candidates, target))
