# QUESTION: Minimum number of platforms required for a railway
# We are given two arrays `arr` and `dep` of size N, representing the
# arrival and departure times of N trains that stop at a railway
# station. Find the minimum number of platforms needed so that no train
# has to wait.
# Note: If a train arrives at exactly the same time another train
# departs, they cannot share a platform (they need separate platforms).
# Greedy approach:
#   1. Sort both arrival and departure arrays independently.
#   2. Use two pointers; iterate through merged events. When you see an
#      arrival before the next departure, you need an extra platform; on
#      a departure before the next arrival, you free one.
#   3. Track the running max of simultaneous trains — that's the answer.
#
# Examples:
# Input: N=6,
# arr[] = {9:00, 9:45, 9:55, 11:00, 15:00, 18:00}
# dep[] = {9:20, 12:00, 11:30, 11:50, 19:00, 20:00}
# Output: 3
# Explanation: There are at most three trains at a time. The train at 11:00 arrived but
# the trains which had arrived at 9:45 and 9:55 have still not departed. So we need at
# least three platforms here.
#
# Input : N=2,
# arr[]={10:20,12:00}
# dep[]={10:50,12:30}
# Output: 1
# Explanation: Before the arrival of the new train, the earlier train already departed.
# So we don't require multiple platforms.


"""
#Brute Force:
1. The answer is the peak number of trains present at the same instant — each
   simultaneously-present train needs its own platform. Count, for every train,
   how many trains overlap it, and take the maximum.
2. For train i, start cnt = 1 (itself), then compare it against every later
   train j.
3. Two trains overlap iff one's arrival falls within the other's [arr, dep]
   span: (arr[i] <= arr[j] <= dep[i]) or (arr[j] <= arr[i] <= dep[j]). Bump cnt
   on each overlap.
4. Any peak-concurrency group all pairwise-overlap, and its lowest-index train
   (as i) sees all the others as later j — so maxCnt over all i is the answer.
TC -> O(n^2) (every pair checked), SC -> O(1)

#Better Approach:
1. Model the timeline as events: each arrival is an ("A") marker, each
   departure a ("D") marker, tagged with its time; sort all 2n events by time.
2. Sweep with a running cnt of occupied platforms and two pointers — i over
   arrival events, j over departure events — starting j at the first departure.
3. If the next arrival is <= the next departure, a train needs a platform
   (cnt += 1, advance i to the next "A"); else a train has left
   (cnt -= 1, advance j to the next "D").
4. maxCnt records the peak occupancy across the sweep.
TC -> O(n log n) (sorting 2n events), SC -> O(n) (the events list)

#Optimal Approach:
1. Same peak-occupancy idea, but drop the train identities: sort arrivals and
   departures INDEPENDENTLY into two ordered streams of instants.
2. Two pointers — i over sorted arrivals, j over sorted departures — with cnt =
   platforms currently in use.
3. If arr[i] <= dep[j], the next arrival happens before (or exactly when) the
   earliest-departing train leaves, so it needs a fresh platform: cnt += 1,
   i += 1. The <= is deliberate — a train arriving exactly as another departs
   still can't share (per the problem), so it counts as an overlap.
4. Otherwise the earliest departure comes first and frees a platform:
   cnt -= 1, j += 1.
5. maxCnt tracks the running peak = the minimum platforms needed.
TC -> O(n log n) (the two sorts; the sweep is O(n)), SC -> O(1) beyond sorting

#KEY INSIGHT:
- The answer is just the maximum number of trains present at any single instant.
  Sorting arrivals and departures separately lets a two-pointer sweep replay the
  events in time order and track that peak in O(n) — the trains never need to
  stay paired. Using <= (arrival == departure overlaps) enforces that a train
  arriving exactly when another leaves still needs its own platform.
"""

from typing import List


class Solution:
    def minimum_number_of_platforms_required_for_a_railway_brute(
        self, arr: List[int], dep: List[int]
    ) -> int:
        cnt = maxCnt = 0

        for i in range(0, len(arr)):
            cnt = 1
            for j in range(i + 1, len(arr)):
                if (arr[i] <= arr[j] and arr[j] <= dep[i]) or (
                    arr[j] <= arr[i] and arr[i] <= dep[j]
                ):
                    cnt += 1
            maxCnt = max(maxCnt, cnt)

        return maxCnt

    def minimum_number_of_platforms_required_for_a_railway_better(
        self, arr: List[int], dep: List[int]
    ) -> int:
        timings = []

        for i in range(0, len(arr)):
            timings.append((arr[i], "A"))

        for i in range(0, len(dep)):
            timings.append((dep[i], "D"))

        timings.sort(key=lambda item: item[0])

        cnt = maxCnt = 0
        i = j = 0
        n = len(timings)

        while timings[j][1] != "D" and j < n:
            j += 1

        while i < n and j < n:
            # Next arrival happens on/before the next departure: a train needs a
            # platform, so occupy one and advance i to the following arrival event.
            if timings[i][0] <= timings[j][0]:
                cnt += 1
                i += 1
                while i < n and timings[i][1] != "A":
                    i += 1
            # Next departure happens first: a train leaves, so free a platform
            # and advance j to the following departure event.
            elif timings[i][0] > timings[j][0]:
                cnt -= 1
                j += 1
                while j < n and timings[j][1] != "D":
                    j += 1
            maxCnt = max(maxCnt, cnt)

        return maxCnt

    def minimum_number_of_platforms_required_for_a_railway_optimal(
        self, arr: List[int], dep: List[int]
    ) -> int:
        arr.sort()
        dep.sort()

        i = j = cnt = maxCnt = 0
        n = len(arr)

        while i < n and j < n:
            # Next arrival happens on/before the next departure: a train needs a
            # platform, so occupy one and move to the next arrival.
            if arr[i] <= dep[j]:
                cnt += 1
                i += 1
            # Next departure happens first: a train leaves, so free a platform
            # and move to the next departure.
            else:
                cnt -= 1
                j += 1
            maxCnt = max(maxCnt, cnt)

        return maxCnt


if __name__ == "__main__":
    sol = Solution()
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(sol.minimum_number_of_platforms_required_for_a_railway_brute(arr, dep))
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(sol.minimum_number_of_platforms_required_for_a_railway_better(arr, dep))
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(sol.minimum_number_of_platforms_required_for_a_railway_optimal(arr, dep))
