# mypy: disable-error-code="empty-body"
# QUESTION: Combination Sum II
# Given a collection of candidate numbers (candidates) and an integer target, find all unique
# combinations in candidates where the sum is equal to the target. There can only be one usage
# of each number in a candidates combination, and return the answer in sorted order.
# e.g.: The combinations [1, 1, 2] and [1, 2, 1] are not unique.
#
# Examples:
# Example 1:
# Input: candidates = [2, 1, 2, 7, 6, 1, 5], target = 8
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
# Explanation: The combinations that sum up to target are
# 1 + 1 + 6 => 8; 1 + 2 + 5 => 8; 1 + 7 => 8; 2 + 6 => 8.
#
# Example 2:
# Input: candidates = [2, 5, 2, 1, 2], target = 5
# Output: [[1, 2, 2], [5]]
# Explanation: The combinations that sum up to target are 1 + 2 + 2 => 5; 5 => 5.
#
# Constraints:
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30


"""
#Brute Force (find_combinations + combination_sum_ii_brute):
1. The hard part of this problem vs Combination Sum I is DUPLICATES: the input
   itself can contain repeats, and each element may be used at most once, so we
   must avoid emitting the same combination twice.
2. Brute idea: just generate EVERY subset via pick/not-pick recursion and let a
   set throw away the duplicate combinations afterwards.
3. Sort candidates first so that any two equal combinations become byte-for-byte
   identical once sorted — this is what makes set-dedup work reliably.
4. Recurse with an `index` pointer. Pick branch: if candidates[index] <= target,
   append it and recurse with index+1 (index+1, not index, because each element
   is used at most once).
5. Backtrack by popping, then take the don't-pick branch: recurse with index+1
   and the same target.
6. Base case: when index reaches the end, if target has hit exactly 0 we found a
   valid combination — add tuple(sorted(combination)) to the set so duplicates
   collapse to one entry.
7. Finally convert the set of tuples back to a sorted list of lists.
TC -> O(2^n * k log k), SC -> O(2^n * k) for the set + O(n) recursion stack
  (n = len(candidates), k = avg combination length; the k log k is the per-leaf
   sort, and the set can hold up to ~2^n combinations before dedup)

#Better Approach:
SKIPPED — there is no natural middle tier. The problem goes straight from
"generate everything and dedup with a set" (brute) to "never generate a
duplicate in the first place" (optimal); nothing sensible sits between them.

#Optimal Approach (find_combinations_optimal + combination_sum_ii_optimal):
1. Goal: avoid the set entirely by never producing a duplicate combination. To
   do that we change the recursion shape from pick/not-pick to a for-loop over
   "which element to place next".
2. Sort candidates so equal values sit adjacent — this is the precondition that
   lets us detect and skip duplicate choices at a given position.
3. Success case: the moment target hits 0, record a copy of combination and stop
   descending — the `else` guards the loop so we don't waste iterations trying to
   extend an already-satisfied path. (No index check needed; any path reaching 0
   is valid.)
4. Otherwise, at each recursion level, loop i from `index` to the end, trying each element
   as the next pick. Passing i+1 into the recursion enforces "use each element
   once" while still letting distinct equal values be used together.
5. Duplicate skip: `if i != index and candidates[i-1] == candidates[i]: continue`.
   The first choice at this level (i == index) is always allowed; any LATER i
   equal to its predecessor is skipped, because choosing it here would rebuild a
   combination we already started with the earlier equal value at this position.
6. Sorted early-exit: `elif target - candidates[i] < 0: break`. Since candidates
   are sorted ascending, once one is too big every later one is too — so break
   the whole loop, don't just continue.
7. Otherwise append, recurse with i+1 and reduced target, then pop to backtrack.
TC -> O(2^n * k), SC -> O(k * x) + O(n) recursion stack
  (x = number of unique combinations; no set and no per-leaf sort, so this beats
   brute by the log k factor and the 2^n set storage)

#KEY INSIGHT:
- Duplicates are killed by SKIPPING repeated values at the same recursion depth
  (i != index and candidates[i-1] == candidates[i]), not by deduping after the
  fact. The first occurrence at a position covers every combination that value
  can start; later equal occurrences would only recreate those, so they're
  pruned — turning the set-based brute force into a set-free optimal one.
"""

from typing import List


class Solution:
    def find_combinations(
        self, candidates: List[int], target: int, hashSet: set, combination: List[int], index: int
    ) -> None:
        if index == len(candidates):
            if target == 0:
                hashSet.add(tuple(sorted(combination)))
            return

        if target - candidates[index] >= 0:
            combination.append(candidates[index])
            self.find_combinations(
                candidates, target - candidates[index], hashSet, combination, index + 1
            )
            combination.pop()
        self.find_combinations(candidates, target, hashSet, combination, index + 1)
        return

    def combination_sum_ii_brute(self, candidates: List[int], target: int) -> List[List[int]]:
        hashSet = set()
        combination = []
        candidates.sort()
        self.find_combinations(candidates, target, hashSet, combination, 0)
        return sorted([list(item) for item in hashSet])

    def combination_sum_ii_better(self, candidates: List[int], target: int) -> List[List[int]]:
        # SKIP: no natural middle tier — the problem jumps from "generate all +
        # dedup with a set" (brute) straight to "never generate a duplicate"
        # (optimal); nothing sensible sits between them.
        pass

    def find_combinations_optimal(
        self,
        candidates: List[int],
        target: int,
        ans: List[List[int]],
        combination: List[int],
        index: int,
    ) -> None:
        if target == 0:
            ans.append(list(combination))

        else:
            for i in range(index, len(candidates)):
                if i != index and candidates[i - 1] == candidates[i]:
                    continue
                if target - candidates[i] < 0:
                    break
                combination.append(candidates[i])
                self.find_combinations_optimal(
                    candidates, target - candidates[i], ans, combination, i + 1
                )
                combination.pop()

    def combination_sum_ii_optimal(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combination = []
        candidates.sort()
        self.find_combinations_optimal(candidates, target, ans, combination, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    candidates = [2, 1, 2, 7, 6, 1, 5]
    target = 8
    print(sol.combination_sum_ii_brute(candidates, target))
    candidates = [2, 1, 2, 7, 6, 1, 5]
    target = 8
    print(sol.combination_sum_ii_optimal(candidates, target))
