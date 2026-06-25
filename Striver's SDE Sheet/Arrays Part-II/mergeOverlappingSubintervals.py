# QUESTION: Merge Overlapping Subintervals
# Detailed solution for Merge Overlapping Sub-intervals - Problem Statement: Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the intervals.
#
# Examples:
# Input : intervals=[[1,3],[2,6],[8,10],[15,18]]
# Output : [[1,6],[8,10],[15,18]]
# Explanation : Since intervals [1,3] and [2,6] are overlapping we can merge them to form [1,6] intervals.
#
# Input : [[1,4],[4,5]]
# Output : [[1,5]]
# Explanation : Since intervals [1,4] and [4,5] are overlapping we can merge them to form [1,5].


"""
#Brute Force:
1. Sort the intervals by start time so any intervals that overlap end up next to
   (or near) each other — overlap can then only happen moving forward, never back.
2. Walk each interval i and read its start = intervals[i][0], end = intervals[i][1].
3. Skip-if-already-absorbed: if `ans` already has a block whose end reaches this
   start (ans[-1][1] >= start), this interval was swallowed by the previous merge,
   so skip it (continue) to avoid emitting a duplicate block.
4. Otherwise grow this block: with an inner loop j from i+1, while the next
   interval overlaps (end >= intervals[j][0]), extend end = max(end, intervals[j][1]);
   stop at the first interval that doesn't overlap (break).
5. Append the finished [start, end] block to `ans`.
6. Why it's brute: the inner forward scan re-walks intervals that later iterations
   also revisit, so on top of the sort it costs O(n^2) in the worst case.
TC -> O(n log n + n^2) = O(n^2), SC -> O(n) for the output

#Better Approach:
SKIPPED — no distinct "better" tier exists; once you sort, the single-pass
optimal below is the natural solution, so it's a direct brute → optimal jump.

#Optimal Approach:
1. Sort the intervals by start time (same reason: overlaps become adjacent).
2. Make one left-to-right pass, keeping `ans` where ans[-1] is the block currently
   being built.
3. For interval i, check for NO overlap: if `ans` is empty, or the last block ends
   before this interval starts (ans[-1][1] < intervals[i][0]), then it can't merge —
   append intervals[i] as a brand-new block.
4. Otherwise they overlap, so absorb it by stretching the last block's end:
   ans[-1][1] = max(ans[-1][1], intervals[i][1]). (Start needs no update — sorting
   guarantees ans[-1] already has the smaller start.)
5. After the single pass, `ans` holds every merged, non-overlapping interval.
6. Why one comparison suffices: because starts are sorted, a new interval can only
   overlap the MOST RECENT block — anything earlier ended even sooner — so there's
   no need to look further back.
TC -> O(n log n), SC -> O(n) for the output

#KEY INSIGHT:
- Sorting by start collapses the problem to a single pass: each interval only ever
  needs to be compared against the last merged block. Two intervals [a,b] and [c,d]
  overlap iff c <= b, and merging just extends the end to max(b, d).
"""

from typing import List


class Solution:
    def merge_overlapping_subintervals_brute(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for i in range(0, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if ans and ans[-1][1] >= start:
                continue
            for j in range(i + 1, len(intervals)):
                if end >= intervals[j][0]:
                    end = max(end, intervals[j][1])
                else:
                    break
            ans.append([start, end])
        return ans

    def merge_overlapping_subintervals_better(self) -> None:
        # SKIP: no distinct "better" tier — once the intervals are sorted, the
        # single-pass optimal is the natural solution (direct brute -> optimal).
        pass

    def merge_overlapping_subintervals_optimal(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []

        for i in range(0, len(intervals)):
            if not ans or ans[-1][1] < intervals[i][0]:
                ans.append(intervals[i])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])

        return ans


if __name__ == "__main__":
    sol = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(sol.merge_overlapping_subintervals_brute(intervals))
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(sol.merge_overlapping_subintervals_optimal(intervals))
