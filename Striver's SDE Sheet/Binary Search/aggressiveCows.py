# mypy: disable-error-code="empty-body"
# QUESTION: Aggressive Cows
# You are given an array 'arr' of size 'n' which denotes the position of
# stalls. You are also given an integer 'k' which denotes the number of
# aggressive cows. You are given the task of assigning stalls to 'k' cows
# such that the minimum distance between any two of them is the maximum
# possible. Find the maximum possible minimum distance.
#
# Examples:
# Example 1:
# Input Format: N = 6, k = 4, arr[] = {0,3,4,7,10,9}
# Result: 3
# Explanation: The maximum possible minimum distance between any two cows will be 3 when
# 4 cows are placed at positions {0, 3, 7, 10}. Here the distances between cows are 3, 4,
# and 3 respectively. We cannot make the minimum distance greater than 3 in any way.
#
# Example 2:
# Input Format: N = 5, k = 2, arr[] = {4,2,1,3,6}
# Result: 5
# Explanation: The maximum possible minimum distance between any two cows will be 5 when
# 2 cows are placed at positions {1, 6}.


"""
#Brute Force:
1. Same reframing as optimal — the answer is a distance d, and can_place(d)
   greedily tests whether all k cows fit with a minimum gap of d. Both rely on
   sorted stalls, so sort first (and guard k <= n).
2. Instead of binary-searching d, just try every candidate distance linearly
   from 1 up to stalls[-1] - stalls[0] (the largest gap that could ever be the
   answer, i.e. the span between the extreme stalls).
3. For each dist, if can_place(dist) succeeds, record it as ans. Because we
   scan increasing distances and overwrite ans each time, the last successful
   dist is the maximum feasible minimum distance.
TC -> O(N * (max-min)), SC -> O(1)

#Better Approach:
SKIPPED — there is no meaningful middle tier. The brute force is a linear
scan over every candidate distance; the optimal replaces that scan with a
binary search. Nothing sensible sits between "try every distance" and
"binary search the distance", so better collapses into optimal.

#Optimal Approach:
1. Reframe the problem: the answer is a *distance* d (the minimum gap we can
   guarantee between adjacent cows). The key property is monotonicity — if we
   can seat all k cows with a minimum gap of d, we can also seat them with any
   smaller gap (smaller gaps only give more slack). So the feasible distances
   form a prefix [0 .. ans], which is exactly what binary search exploits.
2. Sort the stalls ascending. Once positions are in order, "place each cow as
   early as possible" is a valid greedy — seating a cow at the first stall that
   fits leaves the maximum room for the remaining cows, so it never hurts.
3. Fix the search space for d: low = 0 (a gap of 0 is always trivially
   feasible) and high = stalls[-1] - stalls[0] (the biggest gap possible is the
   span between the two extreme stalls). The answer must lie in [low, high].
   Note low is a distance, NOT a position, so it starts at 0 — independent of
   where the stalls actually sit on the number line.
4. Binary search over d: for each candidate mid, ask can_place(mid) — "can all
   k cows sit at least mid apart?"
5. can_place is the greedy feasibility check: seat the first cow at stalls[0]
   (cnt = 1, lastPlaced = 0). Walk the sorted stalls; whenever the current
   stall is >= mid away from the last seated cow, seat another cow there and
   move lastPlaced forward. If cnt ever reaches k, mid is feasible.
6. If mid is feasible, record it (ans = mid) and reach for a larger gap
   (low = mid + 1); otherwise the gap is too big, so shrink it (high = mid - 1).
   The last feasible mid is the maximum achievable minimum distance.
7. Guard with k <= n — you cannot place more cows than there are stalls; return
   -1 when the input is infeasible.
TC -> O(N log N + N log(max-min)), SC -> O(1)

#KEY INSIGHT:
- Feasibility is monotonic in the distance: a larger required gap is only ever
  harder to satisfy. That turns "find the max min-distance" into "binary search
  the largest distance that still passes a greedy left-to-right placement."
"""

from typing import List


class Solution:
    def aggressive_cows_brute(self, stalls: List[int], k: int) -> int:
        ans = -1

        if k <= len(stalls):
            stalls.sort()
            for dist in range(1, stalls[-1] - stalls[0] + 1):
                if self.can_place(stalls, k, dist):
                    ans = dist

        return ans

    def aggressive_cows_better(self, stalls: List[int], k: int) -> int:
        # SKIP: no meaningful middle tier — the brute force linearly scans every
        # candidate distance and the optimal binary-searches it; nothing sensible
        # sits between the two.
        pass

    def can_place(self, stalls: List[int], k: int, dist: int) -> bool:
        ans = False
        cnt = 1
        lastPlaced = 0

        for i in range(1, len(stalls)):
            if stalls[i] - stalls[lastPlaced] >= dist:
                cnt += 1
                lastPlaced = i

            if cnt == k:
                ans = True
                break

        return ans

    def aggressive_cows_optimal(self, stalls: List[int], k: int) -> int:
        ans = -1
        if k <= len(stalls):
            stalls.sort()
            low, high = 0, stalls[-1] - stalls[0]

            while low <= high:
                mid = low + (high - low) // 2

                if self.can_place(stalls, k, mid):
                    ans = mid
                    low = mid + 1
                else:
                    high = mid - 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4
    print(sol.aggressive_cows_brute(stalls, k))
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4
    print(sol.aggressive_cows_optimal(stalls, k))
