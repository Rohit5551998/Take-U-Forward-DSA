# mypy: disable-error-code="empty-body"
# QUESTION: N meetings in one room
# There is one meeting room in a firm. You are given two arrays `start`
# and `end`, each of size N. For index i, start[i] denotes the starting
# time of the i-th meeting while end[i] denotes its ending time.
# A meeting can be scheduled if the room is free at its starting time
# (i.e., no other meeting is currently being held). Two meetings cannot
# overlap — but a meeting starting at the exact end time of another is
# allowed.
# Find the maximum number of meetings that can be held in the room (and
# optionally, the indices of those meetings).
# Greedy approach: sort meetings by END time ascending; pick a meeting
# whenever its start time >= the last selected meeting's end time.
#
# Examples:
# Input: N = 6, start[] = {1,3,0,5,8,5}, end[] = {2,4,5,7,9,9}
# Output: [1, 2, 4, 5]
# Explanation: These meeting can be conducted in the room.
#
# Input: N = 2, start[] = {1,5}, end[] = {7,8}
# Output: [1]
# Explanation: Any one out of the two meeting can take place.


"""
#Brute Force:
SKIPPED — N meetings is a canonical greedy problem; sort-by-end-time selection
is the only standard approach. The sole alternative is exponential subset
enumeration (try every subset, keep the largest non-overlapping one), which is
not a distinct technique worth a tier.

#Better Approach:
SKIPPED — no intermediate tier exists between the (exponential) brute and the
O(n log n) greedy; the greedy is the single meaningful approach.

#Optimal Approach:
1. Classic activity-selection greedy: to fit the MOST meetings, keep the room
   free as early as possible — so the meeting that ENDS earliest is never a
   worse pick than one ending later.
2. Pack each meeting as a tuple (start, end, original_index + 1) so the 1-based
   index survives the sort (the answer needs indices, not times).
3. Sort all meetings by end time ascending. Python's sort is stable, so equal
   end times keep their input order.
4. Track lastEnd (end time of the last selected meeting), initialised to -1 so
   the first meeting is always takeable.
5. Scan in sorted order; take a meeting only if its start is >= lastEnd (the
   room is free — a meeting may begin exactly when the previous one ends), then
   advance lastEnd to this meeting's end and record its index.
6. The collected indices are a maximal set of non-overlapping meetings.
TC -> O(n log n) (dominated by the sort; the scan is O(n)),
SC -> O(n) (the tuple list plus the result)

#KEY INSIGHT:
- Greedily choosing the earliest-finishing compatible meeting is provably
  optimal: finishing sooner frees the room sooner, which can only allow more
  (never fewer) later meetings. Sorting by end time turns this into a single
  left-to-right pass.
"""

from typing import List


class Solution:
    def n_meetings_in_one_room_brute(self, start: List[int], end: List[int]) -> List[int]:
        # SKIP: only alternative is exponential subset enumeration, not a distinct technique
        pass

    def n_meetings_in_one_room_better(self, start: List[int], end: List[int]) -> List[int]:
        # SKIP: no tier between the exponential brute and the O(n log n) greedy optimal
        pass

    def n_meetings_in_one_room_optimal(self, start: List[int], end: List[int]) -> List[int]:
        meetings = [(start[i], end[i], i + 1) for i in range(0, len(start))]
        result = []

        meetings.sort(key=lambda item: item[1])

        lastEnd = -1

        for i in range(0, len(meetings)):
            if meetings[i][0] >= lastEnd:
                lastEnd = meetings[i][1]
                result.append(meetings[i][2])

        return result


if __name__ == "__main__":
    sol = Solution()
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 5, 7, 9, 9]
    print(sol.n_meetings_in_one_room_optimal(start, end))
